#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

let idx = 0;
const curList = list.map((n) => {
  idx++;
  return n * (idx - 1);
}
);

console.log(curList);
