// Dropdown functionality for Log in (toggle on click)
document.addEventListener('DOMContentLoaded', function() {
    var dropbtn = document.getElementById('loginDropBtn');
    var dropdownContent = document.getElementById('loginDropdown');
    // Only run if elements exist
    if (!dropbtn || !dropdownContent) return;
    var dropdown = dropbtn.parentElement;

    // Hide dropdown initially
    dropdownContent.style.display = 'none';

    // Toggle dropdown on click
    dropbtn.addEventListener('click', function(e) {
        e.preventDefault();
        var isOpen = dropdownContent.style.display === 'block';
        dropdownContent.style.display = isOpen ? 'none' : 'block';
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function(e) {
        if (!dropdown.contains(e.target)) {
            dropdownContent.style.display = 'none';
        }
    });

    // Optional: close dropdown on ESC key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            dropdownContent.style.display = 'none';
        }
    });
});
