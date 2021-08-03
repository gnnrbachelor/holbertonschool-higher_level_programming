#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
    let k = 0;
    for (let j = 0; j < this.width; j++) {
      process.stdout.write('X');
      k++;
    }
      if (k === this.width) {
        console.log();
      }
    }
  }
};

