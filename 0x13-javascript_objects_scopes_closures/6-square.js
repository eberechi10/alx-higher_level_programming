#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let idx = 0; idx < this.height; idx++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
