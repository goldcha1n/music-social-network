document.addEventListener('DOMContentLoaded', function() {
  const showCommentsButtons = document.querySelectorAll('.show-comments-button');

  showCommentsButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      const commentsContainer = button.parentElement.querySelector('.comments');
      commentsContainer.classList.toggle('show');
    });
  });
});
