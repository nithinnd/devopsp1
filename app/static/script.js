const questionInput = document.getElementById("question");
const decideButton = document.getElementById("decide-btn");
const roastButton = document.getElementById("roast-btn");
const motivateButton = document.getElementById("motivate-btn");
const resultLabel = document.getElementById("result-label");
const answerElement = document.getElementById("answer");
const confidenceElement = document.getElementById("confidence");
const messageElement = document.getElementById("message");

function setLoadingState(text) {
    resultLabel.textContent = text;
    answerElement.textContent = "Thinking...";
    confidenceElement.textContent = "";
    messageElement.textContent = "";
}

function showError(message) {
    resultLabel.textContent = "That did not work.";
    answerElement.textContent = "Try again";
    confidenceElement.textContent = "";
    messageElement.textContent = message;
}

async function fetchJson(url) {
    const response = await fetch(url);
    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.error || "Something went wrong.");
    }

    return data;
}

async function handleDecision() {
    const question = questionInput.value.trim();

    if (!question) {
        showError("Please enter a question first.");
        questionInput.focus();
        return;
    }

    setLoadingState("Consulting the decision engine...");

    try {
        const data = await fetchJson(`/decide?question=${encodeURIComponent(question)}`);
        resultLabel.textContent = `Question: ${data.question}`;
        answerElement.textContent = data.answer;
        confidenceElement.textContent = `Confidence: ${Math.round(data.confidence * 100)}%`;
        messageElement.textContent = "";
    } catch (error) {
        showError(error.message);
    }
}

async function handleRoast() {
    setLoadingState("Preparing a light roast...");

    try {
        const data = await fetchJson("/random-insult");
        resultLabel.textContent = "Roast delivered.";
        answerElement.textContent = "Respectfully:";
        confidenceElement.textContent = "";
        messageElement.textContent = data.message;
    } catch (error) {
        showError(error.message);
    }
}

async function handleMotivation() {
    setLoadingState("Finding suspiciously useful encouragement...");

    try {
        const data = await fetchJson("/motivation");
        resultLabel.textContent = "Motivation acquired.";
        answerElement.textContent = "Your message:";
        confidenceElement.textContent = "";
        messageElement.textContent = data.message;
    } catch (error) {
        showError(error.message);
    }
}

decideButton.addEventListener("click", handleDecision);
roastButton.addEventListener("click", handleRoast);
motivateButton.addEventListener("click", handleMotivation);

questionInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        handleDecision();
    }
});
