document.addEventListener('DOMContentLoaded', function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Function to add a message to the chat container
    function addMessageToContainer(messageText, timestamp) {
        var messageContainer = document.getElementById('message-container');
        var isUserScrolled = messageContainer.scrollHeight - messageContainer.clientHeight > messageContainer.scrollTop;

        var messageElement = document.createElement('div');

        // Use the provided timestamp or current time if not available
        var formattedTimestamp = timestamp || new Date().toLocaleTimeString();

        messageText = `[${formattedTimestamp}] ${messageText}`;
        messageElement.innerHTML = `<p>${messageText}</p>`;
        messageContainer.appendChild(messageElement);

        if (!isUserScrolled) {
            messageContainer.scrollTop = messageContainer.scrollHeight - messageContainer.clientHeight;
        }
    }

    // Restore stored messages from local storage
    var storedMessages = JSON.parse(localStorage.getItem('chatMessages')) || [];
    storedMessages.forEach(function (message) {
        var timestamp = message.timestamp || new Date().toLocaleTimeString();
        addMessageToContainer(message.message, timestamp);
    });

    // Emit request to the server for any missed messages (acknowledgment not received)
    socket.emit('request_missed_messages');

    // Listen for missed messages from the server
    socket.on('missed_messages', function (missedMessages) {
        missedMessages.forEach(function (missedMessage) {
            var timestamp = missedMessage.timestamp || new Date().toLocaleTimeString();
            addMessageToContainer(missedMessage.message, timestamp);
        });
    });

    // Function to save the message to local storage
    function saveMessageToLocalStorage(message, timestamp) {
        storedMessages.push({ message, timestamp });
        localStorage.setItem('chatMessages', JSON.stringify(storedMessages));
    }

    // Listen for new messages from the server
    socket.on('message', function (data) {
        var timestamp = data.timestamp || new Date().toLocaleTimeString();
        addMessageToContainer(data.message, timestamp);

        // Save the new message to local storage
        saveMessageToLocalStorage(data.message, timestamp);

        // Emit acknowledgment to the server that the message is received
        socket.emit('message_received', { messageId: data.messageId });
    });

    var messageForm = document.getElementById('message-form');
    var messageInput = document.getElementById('message-input');

    messageForm.addEventListener('submit', function (event) {
        event.preventDefault();
        var messageText = messageInput.value.trim();

        if (messageText !== '') {
            socket.emit('message', messageText);
        }

        messageInput.value = '';
    });

});
