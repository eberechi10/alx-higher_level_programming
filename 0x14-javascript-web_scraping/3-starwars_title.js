#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const myurl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(myurl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);

    console.log(movie.title);
  }
});
