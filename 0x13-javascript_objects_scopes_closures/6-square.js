#!/usr/bin/node

const oldSquare = require('./5-square');

module.exports = class Square extends oldSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
