document.addEventListener('DOMContentLoaded', function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('message', function (data) {
        var messageContainer = document.getElementById('message-container');
        var isUserScrolled = messageContainer.scrollHeight - messageContainer.clientHeight > messageContainer.scrollTop;

        var messageElement = document.createElement('div');
        var timestamp = new Date().toLocaleTimeString();
        var messageText = data.message;

        messageText = `[${timestamp}] ${messageText}`;

        messageElement.innerHTML = `<p>${messageText}</p>`;
        messageContainer.appendChild(messageElement);

        if (!isUserScrolled) {
            messageContainer.scrollTop = messageContainer.scrollHeight - messageContainer.clientHeight;
        }
    });

    var messageForm = document.getElementById('message-form');
    var messageInput = document.getElementById('message-input');

    messageForm.addEventListener('submit', function (event) {
        event.preventDefault();
        var messageText = messageInput.value.trim();

        // Check if the message is a private message
        if (messageText.startsWith('/private')) {
            var [command, recipient, ...textArray] = messageText.split(' ');
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

    // Update the private message handling
    socket.on('private_message', function (data) {
        var messageContainer = document.getElementById('message-container');
        var isUserScrolled = messageContainer.scrollHeight - messageContainer.clientHeight > messageContainer.scrollTop;

        var messageElement = document.createElement('div');
        var timestamp = new Date().toLocaleTimeString();
        var messageText = `[${timestamp}] [Private] ${data.sender} to ${data.recipient}: ${data.message}`;

        messageElement.innerHTML = `<p>${messageText}</p>`;
        messageContainer.appendChild(messageElement);

        if (!isUserScrolled) {
            messageContainer.scrollTop = messageContainer.scrollHeight - messageContainer.clientHeight;
        }
    });
});
