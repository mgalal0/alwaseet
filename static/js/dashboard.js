
// document.getElementById("menu-toggle").addEventListener("click", function() {
//     document.getElementById("wrapper").classList.toggle("toggled");
// });

// scripts.js

// document.addEventListener('DOMContentLoaded', function () {
//     const sidebar = document.getElementById('sidebar');
//     const sidebarToggler = document.getElementById('sidebarToggler');

//     sidebarToggler.addEventListener('click', function () {
//         sidebar.classList.toggle('hidden');
//     });
// });

// for slicing the text on dashboard card 
document.addEventListener("DOMContentLoaded", function() {
    const maxLength = 100; // Adjust as needed
    const descElements = document.querySelectorAll('.desc p');

    descElements.forEach(function(descElement) {
        let text = descElement.innerHTML;
        if (text.length > maxLength) {
            text = text.substring(0, maxLength) + '...';
        }
        descElement.innerHTML = text;
    });
});

// to add active class to the dashboard links 
document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll('.links ul li a');

    links.forEach(link => {
        link.addEventListener('click', function(event) {
            // Prevent default link behavior
            event.preventDefault();

            // Remove "active" class from all links
            links.forEach(link => link.classList.remove('active'));

            // Add "active" class to the clicked link
            this.classList.add('active');

            // Navigate to the clicked link's href
            window.location.href = this.href;
        });
    });
});