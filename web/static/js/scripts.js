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

    // Adjusted to handle saving encrypted passwords
    document.querySelectorAll('.save-encrypted-btn').forEach(button => {
        button.addEventListener("click", function() {
            const elementSelector = this.getAttribute('data-save-target');
            saveEncryptedPassword(elementSelector);
        });
    });

    // Adjusted to handle saving decrypted passwords
    document.querySelectorAll('.save-decrypted-btn').forEach(button => {
        button.addEventListener("click", function() {
            const elementSelector = this.getAttribute('data-save-target');
            saveDecryptedPassword(elementSelector);
        });
    });

    function saveEncryptedPassword(elementSelector) {
        const textArea = document.querySelector(elementSelector);
        if (!textArea) {
            console.error("Save target not found: ", elementSelector);
            return;
        }

        const encryptedPassword = textArea.value;

        fetch('/saveEncryptedPassword', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ encryptedPassword: encryptedPassword }),
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

    function saveDecryptedPassword(elementSelector) {
        const passInput = document.querySelector(elementSelector);
        if (!passInput) {
            console.error("Password input not found: ", elementSelector);
            return;
        }

        const decryptedPassword = passInput.value;

        fetch('/saveDecryptedPassword', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ decryptedPassword: decryptedPassword }),
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
});