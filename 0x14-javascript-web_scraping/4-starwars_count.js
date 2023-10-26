#!/usr/bin/node

const request = require('request');
const myurl = process.argv[2];

const charId = '18';
let count = 0;

request.get(myurl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const datas = JSON.parse(body);
    datas.results.forEach((film) => {

      film.characters.forEach((character) => {
        if (character.includes(charId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
