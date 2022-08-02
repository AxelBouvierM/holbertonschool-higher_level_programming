#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      let str = '';
      let x = 0;
      for (x = 0; x < this.width; x++) {
        str += 'X';
      }
      console.log(str);
    }
  }
};
