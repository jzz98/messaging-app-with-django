const wsScheme = window.location.protocol === "https:" ? "wss" : "ws";
const socket = new WebSocket(`${wsScheme}://127.0.0.1:8001/ws/chat/dialog/${userId}`);

// Mostrar mensaje recibido
socket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    const chatBox = document.getElementById("chat-box");

    const bubble = document.createElement("div");
    bubble.className = "chat-bubble received";

    const content = document.createElement("div");
    content.className = "message-content";
    content.textContent = data.message;

    const time = document.createElement("div");
    time.className = "message-time";
    const now = new Date();
    time.textContent = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});

    bubble.appendChild(content);
    bubble.appendChild(time);

    chatBox.appendChild(bubble);
    chatBox.scrollTop = chatBox.scrollHeight; // hace scroll al fondo
};


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const messageInput = document.getElementById("mensaje");
const sendBtn = document.getElementById("send-btn");

sendBtn.addEventListener('click', () => {
    const message = messageInput.value.trim();
    const chatBox = document.getElementById("chat-box");

    if (!chatBox) {
        console.error("❌ No se encontró el elemento con id='chat-box'");
        return;
    }

    if (!message) {
        console.warn("⚠️ Mensaje vacío, no se envía ni se muestra.");
        return;
    }

    // Crear burbuja
    const bubble = document.createElement("div");
    bubble.className = "chat-bubble sent";

    const content = document.createElement("div");
    content.className = "message-content";
    content.textContent = message;

    const time = document.createElement("div");
    time.className = "message-time";
    const now = new Date();
    time.textContent = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});

    bubble.appendChild(content);
    bubble.appendChild(time);

    chatBox.appendChild(bubble);
    chatBox.scrollTop = chatBox.scrollHeight;

    console.log("✅ Mensaje agregado al DOM:", message);

    // Enviar por WebSocket (opcional)
    if (socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({
            type: "chat.message",
            message: message,
        }));
    }

    // Enviar por HTTP (opcional)
    fetch(window.location.href, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ mensaje: message }),
        credentials: 'include'
    });

    messageInput.value = '';
});
