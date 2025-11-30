// animate webpage title
let originalTitle = document.title;
let title = originalTitle;
let position = 0;

let spacer = " ".repeat(1);
title = spacer + title + spacer;

function animateTitle() {
    document.title = title.slice(position);
    position++;
    if (position >= title.length - 1) {
        position = 0;
    }
}

setInterval(animateTitle, 200);

// Handle button clicks to execute Python programs
document.addEventListener("DOMContentLoaded", function() {
    const button1 = document.getElementById("button1");
    const button2 = document.getElementById("button2");
    const textSection = document.querySelector(".text-section p");

    /**
     * Execute a Python program via API call
     * @param {string} endpoint - The API endpoint to call
     * @param {HTMLElement} button - The button element that was clicked
     */
    function executeProgram(endpoint, button) {
        // Disable button and show loading state
        const originalText = button.textContent;
        button.disabled = true;
        button.textContent = "Running...";
        button.style.opacity = "0.6";
        button.style.cursor = "wait";

        // Make POST request to execute the program
        fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            // Re-enable button
            button.disabled = false;
            button.textContent = originalText;
            button.style.opacity = "1";
            button.style.cursor = "pointer";

            // Update text section with result
            if (data.status === "success") {
                // Don't show success message, just show the output directly
                textSection.innerHTML = data.output ? `<pre>${data.output}</pre>` : "";
                textSection.style.color = "#e0e0e0";
            } else {
                textSection.innerHTML = `<strong>Error:</strong><br>${data.message}<br><br>${data.error ? `<pre>${data.error}</pre>` : ""}`;
                textSection.style.color = "#f44336";
            }
        })
        .catch(error => {
            // Re-enable button on error
            button.disabled = false;
            button.textContent = originalText;
            button.style.opacity = "1";
            button.style.cursor = "pointer";

            // Show error message
            textSection.innerHTML = `<strong>Error:</strong><br>Failed to execute program: ${error.message}`;
            textSection.style.color = "#f44336";
            console.error("Error:", error);
        });
    }

    // Add click event listeners
    if (button1) {
        button1.addEventListener("click", function() {
            executeProgram("/execute_button1", button1);
        });
    }

    if (button2) {
        button2.addEventListener("click", function() {
            executeProgram("/execute_button2", button2);
        });
    }
});