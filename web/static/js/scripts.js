document.addEventListener("DOMContentLoaded", function() {
    // Add event listener for the "Copy" button
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

        const text = textArea.value;
        
        if (!navigator.clipboard) {
            // Fallback for browsers without Clipboard API support
            const tempTextArea = document.createElement("textarea");
            document.body.appendChild(tempTextArea);
            tempTextArea.value = text;
            tempTextArea.select();
            document.execCommand("copy");
            document.body.removeChild(tempTextArea);
        } else {
            // Using Clipboard API
            navigator.clipboard.writeText(text).then(function() {
                alert("Copied to clipboard!");
            }, function(error) {
                console.error("Copy failed", error);
            });
        }
    }

    document.querySelectorAll('.save-btn').forEach(button => {
        button.addEventListener("click", function() {
            const elementSelector = this.getAttribute('save-copy-target');
            const password = this.getAttribute('password-input');
            saveToList(elementSelector, password);
        });
    });

    function saveToList(elementSelector, password){
        const textArea = document.querySelector(elementSelector);
        if (!textArea) {
            console.error("Save target not found: ", elementSelector);
            return;
        }

        const passText = document.querySelector(password);
        if(!passText) {
            console.error("Save target not found: ", password);
            return;
        }

        const text = textArea.value;
        const pass = passText.value;

        
    }
});

