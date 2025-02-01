function submitUserData() {
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const height = document.getElementById('height').value;
    const weight = document.getElementById('weight').value;
    const gender = document.querySelector('input[name="gender"]:checked').value;
    const activityLevel = document.getElementById('activity-level').value;
    const notes = document.getElementById('notes').value; 
    const goals = document.getElementById('goals').value;

    const userData = {
        name: name,
        age: age,
        height: height,
        weight: weight,
        gender: gender,
        activity_level: activityLevel,
        notes: notes,
        goals: goals
    };

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    });
}

function sendQuestion() {
    const userInput = document.getElementById('question').value;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const chatBox = document.getElementById('chat-box');

        // Add user message
        const userMessage = document.createElement('div');
        userMessage.className = 'message user-message';
        userMessage.innerHTML = `<strong>You:</strong> ${userInput}`;
        chatBox.appendChild(userMessage);

        // Add AI message
        const aiMessage = document.createElement('div');
        aiMessage.className = 'message ai-message';
        aiMessage.innerHTML = `<strong>AI:</strong> ${data.message}`;
        chatBox.appendChild(aiMessage);

        // Scroll to the bottom
        chatBox.scrollTop = chatBox.scrollHeight;

        // Clear input field
        document.getElementById('question').value = '';
    });
}
