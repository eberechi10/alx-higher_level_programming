// Write a JavaScript script that fetches and prints
$(document).ready(function () {
	// language translator
	$("INPUT#btn_translate").click(function () {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	});
});
