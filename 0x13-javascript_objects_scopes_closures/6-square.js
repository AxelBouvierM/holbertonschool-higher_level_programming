#!/usr/bin/node
const Rectangle = require('./5-square.js');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      for (i = 0; i < this.height; i++) {
        let str = '';
        let x = 0;
        for (x = 0; x < this.width; x++) {
          str += 'C';
        }
        console.log(str);
      }
    }
  }
};
