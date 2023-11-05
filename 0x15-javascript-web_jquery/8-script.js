// Write a JavaScript script that fetches and lists the title for all movies.
$("document").ready(function () {
    const URL = "https://swapi-api.alx-tools.com/api/films/?format=json";
    $.get(URL, function (data) {
        for (const movie of data.results) {
            $("#list_movies").append("<li>" + movie.title + "</li>");
        }
    });
});
