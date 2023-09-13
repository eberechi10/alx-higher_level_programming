#!/usr/bin/node

const { dict } = require('./101-data');

const ids = Object.values(dict);
const occurences = Object.keys(dict);

const newDict = {};
ids.forEach(id => {
  newDict[id] = [];

});

let idx = 0;
ids.forEach(id => {
  newDict[id].push(occurences[idx]);
  idx++;
});

console.log(newDict);
