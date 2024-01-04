document.addEventListener('DOMContentLoaded', function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('message', function (msg) {
        var messageContainer = document.getElementById('message-container');
        var messageElement = document.createElement('div');
        messageElement.innerHTML = '<p>' + msg + '</p>';
        messageContainer.appendChild(messageElement);
        if (!isUserScrolled) {
            messageContainer.scrollTop = messageContainer.scrollHeight - messageContainer.clientHeight;
        }
    });

    var messageForm = document.getElementById('message-form');
    var messageInput = document.getElementById('message-input');

    messageForm.addEventListener('submit', function (event) {
        event.preventDefault();
        console.log()
        var messageText = messageInput.value.trim();
        if (messageText !== '') {
            socket.emit('message', messageText);
            messageInput.value = '';
        }
    });
});


