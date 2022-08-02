#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.char = c;
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      for (i = 0; i < this.height; i++) {
        let str = '';
        let x = 0;
        for (x = 0; x < this.width; x++) {
          str += this.char;
        }
        console.log(str);
      }
    }
  }
};
