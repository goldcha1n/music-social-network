window.onload = function() {
    var form = document.getElementById('layout');
    var menuButton = document.getElementById('menu-button');

    form.addEventListener('focusin', function() {
        menuButton.classList.add('active');
    });

    form.addEventListener('focusout', function() {
        menuButton.classList.remove('active');
    });
};
