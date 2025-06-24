function generatePassword(event) {
    event.preventDefault();

    const letters = document.getElementById('letters').value;
    const symbols = document.getElementById('symbols').value;
    const numbers = document.getElementById('numbers').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `letters=${letters}&symbols=${symbols}&numbers=${numbers}`
    })
    .then(response => response.json())
    .then(data => {
        const result = document.getElementById('result');
        result.style.opacity = 0; // Reset fade
        setTimeout(() => {
            result.innerText = `Generated Password: ${data.password}`;
            result.style.opacity = 1;
        }, 200);
    });
}
