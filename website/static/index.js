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
            applyFontStyle(fontSizeSelect.value + 'px');
            document.execCommand('foreColor', false, 'black');
        });

        function toggleButton(button) {
            button.classList.toggle('clicked');
        }

        function applyFontStyle(fontStyle) {
            editor.focus();

            editor.addEventListener('keypress', function(event) {
                // Check if a printable character is pressed (excluding modifier keys like Shift)
                if (event.key.length === 1 && !event.ctrlKey && !event.altKey) {
                    // Apply the font style to the newly typed character
                    document.execCommand('styleWithCSS', false, true);
                    document.execCommand('fontSize', false, fontStyle);
                    editor.style.color = 'black';
                }
            }, { once: true });
        }
    });
};

// CALENDAR
let calendarPresent = document.querySelector('.calendar-events');


if (calendarPresent){
    document.addEventListener("DOMContentLoaded", function() {
        let currentDate = new Date();
        let currentMonth = currentDate.getMonth();
        let currentYear = currentDate.getFullYear();

        // Function to generate calendar
        function generateCalendar(month, year) {
            let firstDay = new Date(year, month, 1);
            let lastDay = new Date(year, month + 1, 0);
            let totalDays = lastDay.getDate();
            let startingDay = firstDay.getDay();
            let monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
            let monthName = monthNames[month];
            document.getElementById('calendar-month').textContent = monthName + ' ';
            document.getElementById('calendar-year').textContent = year;

            // Fill in the days
            let date = 1;
            let calendarBody = document.getElementById('calendar-body');
            calendarBody.innerHTML = '';
            for (let i = 0; i < 6; i++) {
                let row = calendarBody.insertRow();
                for (let j = 0; j < 7; j++) {
                    let cell = row.insertCell();
                    if (i === 0 && j < startingDay) {
                        // Add empty cells before the first day of the month
                        cell.innerHTML = '';
                    } else if (date > totalDays) {
                        // If all days of the month are added, exit the loop
                        break;
                    } else {
                        cell.innerHTML = date;
                        cell.addEventListener('click', function() {
                            let clickedDate = new Date(currentYear, currentMonth, parseInt(cell.textContent) + 1);
                            showModal(clickedDate);
                        });
                        date++;
                    }
                }
            }
        }

        // Initial generation of calendar
        generateCalendar(currentMonth, currentYear);

        // Function to show the modal
        function showModal(clickedDate) {
            let modal = document.getElementById('event-modal');
            modal.classList.add('show');
            modal.style.display = 'block';
            modal.setAttribute('aria-hidden', 'false');
            document.body.classList.add('modal-open');

            // Set start and end time input fields with the clicked date
            let startTimeInput = document.getElementById('event-start-time');
            let endTimeInput = document.getElementById('event-end-time');
            startTimeInput.value = clickedDate.toISOString().substring(0, 16);
            endTimeInput.value = clickedDate.toISOString().substring(0, 16);
        }

        // Function to hide the modal
        function hideModal() {
            let modal = document.getElementById('event-modal');
            modal.classList.remove('show');
            modal.style.display = 'none';
            modal.setAttribute('aria-hidden', 'true');
            document.body.classList.remove('modal-open');
        }

        // Add submit event listener to the event form
        document.getElementById('event-form').addEventListener('submit', function(e) {
            hideModal();
        });

        document.querySelector('.task-close').addEventListener('click', function() {
            hideModal();
        });

        hideModal();


        // Handling previous month button click
        document.getElementById('prev-month').addEventListener('click', function() {
            currentMonth--;
            if (currentMonth < 0) {
                currentMonth = 11;
                currentYear--;
            }
            generateCalendar(currentMonth, currentYear);
        });

        // Handling next month button click
        document.getElementById('next-month').addEventListener('click', function() {
            currentMonth++;
            if (currentMonth > 11) {
                currentMonth = 0;
                currentYear++;
            }
            generateCalendar(currentMonth, currentYear);
        });
    });
};