const imageInput = document.getElementById('imageInput');
const fileNameDisplay = document.getElementById('fileName');

// Update filename when file is selected
imageInput.addEventListener('change', function () {
    if (this.files && this.files[0]) {
        fileNameDisplay.textContent = "✅ Selected: " + this.files[0].name;
    }
});

async function predictImage() {
    const file = imageInput.files[0];
    if (!file) {
        showError("Please select an image first!");
        return;
    }

    // UI States
    toggleLoading(true);
    hideResults();

    // Prepare Data
    const formData = new FormData();
    formData.append("file", file);

    try {
        // Send to FastAPI
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            showResult(result);
        } else {
            showError(result.detail || "Server Error.");
        }

    } catch (error) {
        showError("Connection failed. Ensure the server is running.");
    } finally {
        toggleLoading(false);
    }
}

// --- Helper Functions ---
function showResult(data) {
    document.getElementById('resultArea').classList.remove('hidden');

    // Set Main Prediction
    document.getElementById('predictionText').textContent = formatLabel(data.prediction);
    document.getElementById('confidenceText').textContent = data.confidence;

    // Set Details List
    const detailsList = document.getElementById('detailsList');
    detailsList.innerHTML = '';

    // Sort results by confidence (Highest first)
    const sortedDetails = Object.entries(data.details).sort((a, b) => b[1] - a[1]);

    for (const [key, value] of sortedDetails) {
        const li = document.createElement('li');
        // Format: Label ........ 99.5%
        li.innerHTML = `<span>${formatLabel(key)}</span> <span>${(value * 100).toFixed(2)}%</span>`;
        detailsList.appendChild(li);
    }
}

function formatLabel(word) {
    // Optional: Add Emojis or formatting
    const dict = {
        'Cat': 'Cat 🐱',
        'Dog': 'Dog 🐶',
        'Wild': 'Wild Animal 🐻'
    };
    return dict[word] || word;
}

function showError(msg) {
    const errorArea = document.getElementById('errorArea');
    errorArea.classList.remove('hidden');
    document.getElementById('errorText').textContent = msg;
}

function hideResults() {
    document.getElementById('resultArea').classList.add('hidden');
    document.getElementById('errorArea').classList.add('hidden');
}

function toggleLoading(isLoading) {
    document.getElementById('loading').classList.toggle('hidden', !isLoading);
    document.getElementById('predictBtn').disabled = isLoading;
}