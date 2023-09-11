#!/usr/bin/node

const { argv } = require('process');

if (!argv[2] || !parseInt(argv[2])) {
  console.log('Missing number of occurrencies');
}

const num = parseInt(argv[2]);
if (num > 0) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
