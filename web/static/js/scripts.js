document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.copy-btn').forEach(button => {
        button.addEventListener("click", function() {
            const elementSelector = this.getAttribute('data-copy-target');
            copyToClipboard(elementSelector);
        });
    });
    
    function copyToClipboard(elementSelector) {
        const textArea = document.querySelector(elementSelector);
        if (!textArea) {
            console.error("Copy target not found: ", elementSelector);
            return;
        }

        navigator.clipboard.writeText(textArea.value)
            .then(() => alert("Copied to clipboard!"))
            .catch(err => console.error("Copy failed", err));
    }

    document.querySelectorAll('.save-btn').forEach(button => {
        button.addEventListener("click", function() {
            const elementSelector = this.getAttribute('data-save-target');
            const passwordInput = "#" + this.getAttribute('password-input');
            saveToList(elementSelector, passwordInput);
        });
    });    
    
    function saveToList(elementSelector, password) {
        const textArea = document.querySelector(elementSelector);
        if (!textArea) {
            console.error("Save target not found: ", elementSelector);
            return;
        }
    
        const passInput = document.querySelector(password);
        if (!passInput) {
            console.error("Password input not found: ", password);
            return;
        }
    
        const encryptedPassword = textArea.value;
        const key = passInput.value;
    
        // Construct the request payload
        const payload = {
            key: key,
            encrypted_password: encryptedPassword
        };
    
        // Send the request to the backend
        fetch('/saveEncryptedPassword', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);
            } else if (data.error) {
                alert(data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
})    