#!/usr/bin/node
const { argv } = require('process');

if (!argv[2] || !parseInt(argv[2])) {
  console.log('Missing size');
}

const elm = parseInt(argv[2]);
if (elm > 0) {
  for (let i = 0; i < elm; i++) {
    console.log('X'.repeat(elm));
  }
}
