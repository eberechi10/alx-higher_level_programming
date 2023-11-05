// Write a JavaScript script that adds, removes and clears LI elements
$(document).ready(function () {
	// a new element is added to the list
	$("#add_item").click(function () {
		$("<li>").text("Item").appendTo("ul.my_list");
	});
	//  element is removed from the list
	$("#remove_item").click(function () {
		$("ul.my_list li:last-child").remove();
	});
	$("#clear_list").click(function () {
		$("ul.my_list").empty();
	});
});
