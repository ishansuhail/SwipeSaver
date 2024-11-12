function toggleChatbox() {
    const chatbox = document.getElementById('chatbox');
    console.log("Sucess!");
    chatbox.style.display = chatbox.style.display === 'none' || chatbox.style.display === '' ? 'flex' : 'none';
}

async function sendMessage() {
    const chatInput = document.getElementById('chat-input');
    const message = chatInput.value.trim();
    if (message === '') return;

    const chatboxContent = document.getElementById('chatbox-content');
    chatboxContent.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    chatInput.value = '';

    
    try {
        const response = await fetch(`/chatbot/?message=${encodeURIComponent(message)}`);
        const data = await response.json();
        chatboxContent.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    } catch (error) {
        chatboxContent.innerHTML += `<p><strong>Bot:</strong> Sorry, there was an error processing your request.</p>`;
    }

    
    chatboxContent.scrollTop = chatboxContent.scrollHeight;
}