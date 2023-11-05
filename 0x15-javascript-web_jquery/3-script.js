// Write a JavaScript script that adds the class red to the <header>
$(document).ready(
  function () {
      $('DIV#red_header').click(
        function () {
            $('header').addClass('red');
        });
});
