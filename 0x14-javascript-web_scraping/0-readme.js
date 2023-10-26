#!/usr/bin/node

const fs = require('fs');

const file_path = process.argv[2];

fs.readFile(file_path, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {

    console.log(data);
  }
});
