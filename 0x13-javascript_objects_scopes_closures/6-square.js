#!/usr/bin/node
// Square class inherits from Rectangle class
const Sq_0 = require('./5-square').Square;

function Square (size) {
  Sq_0.call(this, size);
}

Square.prototype = Object.create(Sq_0.prototype);
Square.constructor = Square;

Square.prototype.charPrint = function (c = 'X') {
  for (let i = 0; i < this.height; i += 1) {
    console.log(c.repeat(this.width));
  }
}

exports.Square = Square;
