const status = document.getElementById("connection-status");
const form = document.getElementById("message-form");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const messages = document.getElementById("messages");

const socket = new WebSocket("ws://localhost:8765");

function showMessage(sender, text, messageType) {
    const item = document.createElement("li");
    const senderLabel = document.createElement("strong");
    const messageText = document.createElement("p");

    item.classList.add("message", messageType);
    senderLabel.textContent = sender;
    messageText.textContent = text;
    item.append(senderLabel, messageText);
    messages.append(item);
    messages.scrollTop = messages.scrollHeight;
}

socket.addEventListener("open", () => {
    status.textContent = "Connecté";
    sendButton.disabled = false;
    messageInput.focus();
});

socket.addEventListener("message", (event) => {
    showMessage("Serveur", event.data, "received");
});

socket.addEventListener("close", () => {
    status.textContent = "Connexion fermée";
    sendButton.disabled = true;
});

socket.addEventListener("error", () => {
    status.textContent = "Erreur de connexion";
});

form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (socket.readyState !== WebSocket.OPEN) {
        return;
    }

    const text = messageInput.value;
    socket.send(text);
    showMessage("Moi", text, "sent");
    messageInput.value = "";
    messageInput.focus();
});
