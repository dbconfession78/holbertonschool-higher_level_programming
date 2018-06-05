#!/usr/bin/node
// rectangle constructor
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }

  this.print = function () {
    // prints rectangle uising 'X'
    for (let i = 0; i < this.height; i += 1) {
      console.log('X'.repeat(this.width));
    }
  };

  this.rotate = function () {
    // exchanges width with height
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  };

  this.double = function () {
    // multiplies width and height each by 2
    this.width = this.width * 2;
    this.height = this.height * 2;
  };
};
