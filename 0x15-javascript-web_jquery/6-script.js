// Write a JavaScript script that updates the text of the <header>
$(document).ready(
  function () {
      $('DIV#update_header').click(
        function () {
            $('header').text('New header!!!');
        });
});
