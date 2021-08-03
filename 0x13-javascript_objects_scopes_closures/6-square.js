#!/usr/bin/node

const SquareA = require('./5-square.js');

module.exports = class Square extends SquareA {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    super.print(c);
  }
};
