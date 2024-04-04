// FLASH MESSAGES
flashClose = document.querySelectorAll('.close');

flashClose.forEach(function(flashClose) {
    flashClose.addEventListener('click', function() {
        this.parentElement.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        let alertElements = document.querySelectorAll('.alert');
        alertElements.forEach(function(alertElement) {
            alertElement.style.opacity = 0;
            setTimeout(function() {
                alertElement.style.display = 'none';
            }, 1000);
        });
    }, 3000);
});

// CURRENT DATE
let datePresent = document.querySelector('.date');
if (datePresent){
    let currentDate = new Date();

    let formattedDate = currentDate.getFullYear() + '-' + (currentDate.getMonth() + 1) + '-' + currentDate.getDate();

    document.getElementById('current-date').innerHTML = formattedDate;
};

// TEXT CUSTOMIZATIONS
let textCustomizationPresent = document.querySelector('.create-entry');
if (textCustomizationPresent){
    document.addEventListener('DOMContentLoaded', function() {
        let boldButton = document.getElementById('bold');
        let italicButton = document.getElementById('italic');
        let underlineButton = document.getElementById('underline');
        let fontSizeSelect = document.getElementById('font-size');
        let editor = document.getElementById('blog-content');
        let blogContentHidden = document.getElementById('blog-content-hidden');
        
        editor.addEventListener('input', function() {
            blogContentHidden.value = editor.innerHTML;
        });

        boldButton.addEventListener('click', function() {
            toggleButton(boldButton);
            document.execCommand('bold', false, null);
            document.execCommand('foreColor', false, 'black');
        });

        italicButton.addEventListener('click', function() {
            toggleButton(italicButton);
            document.execCommand('italic', false, null);
            document.execCommand('foreColor', false, 'black');
        });

        underlineButton.addEventListener('click', function() {
            toggleButton(underlineButton);
            document.execCommand('underline', false, null);
            document.execCommand('foreColor', false, 'black');
        });

        fontSizeSelect.addEventListener('change', function() {
            // editor.style.fontSize = fontSizeSelect.value + 'px';
            applyFontStyle(fontSizeSelect.value + 'px');
            document.execCommand('foreColor', false, 'black');
        });

        function toggleButton(button) {
            button.classList.toggle('clicked');
        }

        function applyFontStyle(fontStyle) {
            editor.focus(); // Ensure the editor has focus

            // Listen for the keypress event to intercept user input
            editor.addEventListener('keypress', function(event) {
                // Check if a printable character is pressed (excluding modifier keys like Shift)
                if (event.key.length === 1 && !event.ctrlKey && !event.altKey) {
                    // Apply the font style to the newly typed character
                    document.execCommand('styleWithCSS', false, true);
                    document.execCommand('fontSize', false, fontStyle);
                    editor.style.color = 'black';
                }
            }, { once: true }); // Remove the event listener after the first keypress
        }
    });
};