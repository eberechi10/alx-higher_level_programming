#!/usr/bin/node

function factorial (idx) {
  return idx === 0 || isNaN(idx) ? 1 : idx * factorial(idx - 1);
}

console.log(factorial(Number(process.argv[2])));
