// Javascript handling file for processText

// Get the form element
const form = document.getElementById("analyze-form");

// Handle the form submission
form.addEventListener("submit", function(event) {
    event.preventDefault();

    // Get the URL from the form input
    const url = document.getElementById("url").value;

    // Send a POST request to the Python script
    fetch("/analyze", {
        method: "POST",
        body: JSON.stringify({ url: url }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        // Display the results in a table
        const table = document.getElementById("output-table");
        table.innerHTML = `
            <tr>
                <th>Key Phrases</th>
                <td>${data.key_phrases.join(", ")}</td>
            </tr>
            <tr>
                <th>Sentiment</th>
                <td>${data.sentiment}</td>
            </tr>
            <tr>
                <th>Entities</th>
                <td>${data.entities.join(", ")}</td>
            </tr>
        `;
    })
    .catch(error => console.error(error));
});
