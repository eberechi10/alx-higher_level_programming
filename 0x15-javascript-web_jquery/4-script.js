// Write a JavaScript script that toggles the class of the <header>
$(document).ready(function () {
	$("DIV#toggle_header").click(function () {
		$("header").toggleClass("red green");
	});
});
