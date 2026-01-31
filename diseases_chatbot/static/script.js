document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    function addMessage(message, isBot = false) {
        console.log('Adding message:', message, 'isBot:', isBot);
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.classList.add(isBot ? 'bot-message' : 'user-message');
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            console.log('Sending message:', message);
            addMessage(message);
            userInput.value = '';

            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Received response:', data);
                addMessage(data.message, data.is_bot);
            })
            .catch(error => {
                console.error('Error:', error);
                addMessage('Sorry, there was an error processing your request.', true);
            });
        }
    }

    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Add an initial bot message
    addMessage("Hello! I'm your Disease Information Assistant. How can I help you today?", true);
});