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

    // Function to save the private message to local storage
    function savePrivateMessageToLocalStorage(message, timestamp) {
        storedMessages.push({ message, timestamp });
        localStorage.setItem('chatMessages', JSON.stringify(storedMessages));
    }

    // Listen for new private messages from the server
    socket.on('private_message', function (data) {
        console.log('Received private_message:', data);  // Add this line for debugging

        var messageContainer = document.getElementById('message-container');
        var isUserScrolled = messageContainer.scrollHeight - messageContainer.clientHeight > messageContainer.scrollTop;

        var messageElement = document.createElement('div');
        var timestamp = data.timestamp || new Date().toLocaleTimeString();
        var messageText = `[${timestamp}] [Private] ${data.sender} to ${data.recipient}: ${data.message}`;

        messageElement.innerHTML = `<p>${messageText}</p>`;
        messageContainer.appendChild(messageElement);

        if (!isUserScrolled) {
            messageContainer.scrollTop = messageContainer.scrollHeight - messageContainer.clientHeight;
        }

        // Save the new private message to local storage
        savePrivateMessageToLocalStorage(messageText, timestamp);

        // Emit acknowledgment to the server that the private message is received
        socket.emit('private_message_received', { messageId: data.messageId });
    });

    // Emit request to the server for any missed private messages (acknowledgment not received)
    socket.emit('request_missed_private_messages');

    // Listen for missed private messages from the server
    socket.on('missed_private_messages', function (missedPrivateMessages) {
        missedPrivateMessages.forEach(function (missedPrivateMessage) {
            var timestamp = missedPrivateMessage.timestamp || new Date().toLocaleTimeString();
            addMessageToContainer(missedPrivateMessage.message, timestamp);
        });
    });

    var messageForm = document.getElementById('message-form');
    var messageInput = document.getElementById('message-input');

    messageForm.addEventListener('submit', function (event) {
        event.preventDefault();
        var messageText = messageInput.value.trim();

        // Check if the message is a private message
        if (messageText.startsWith('/private')) {
            var [, recipient, ...textArray] = messageText.split(' ');
            var privateText = textArray.join(' ');

            console.log('Emitting private_message:', { recipient, message: privateText });

            if (recipient && privateText) {
                socket.emit('private_message', { recipient, message: privateText });
            } else {
                console.error('Invalid private message format');
            }
        } else if (messageText !== '') {
            socket.emit('message', messageText);
        }

        messageInput.value = '';
    });

});
