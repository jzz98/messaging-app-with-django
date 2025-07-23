const wsScheme = window.location.protocol === "https:" ? "wss" : "ws";
const userId = window.location.pathname.split("/").pop();
const socket = new WebSocket(`${wsScheme}://127.0.0.1:8001/ws/chat/dialog/${userId}`);

// Mostrar mensaje recibido
socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log("Mensaje recibido:", data.message);
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
const sendBtn = document.getElementById("send-btn"); // botón para enviar mensaje

sendBtn.addEventListener('click', () => {
    const message = messageInput.value;
    const httpEndpoint = window.location.href;

    fetch(httpEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ mensaje: message }),
        credentials: 'include'
    })

});

