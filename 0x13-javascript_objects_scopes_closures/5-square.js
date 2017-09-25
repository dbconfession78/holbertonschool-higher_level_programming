#!/usr/bin/node
// the Square class setup to niherit from the rectangle class
const Rectangle = require('./4-rectangle').Rectangle;

function Square(size) {
  Rectangle.call(this, size, size);
}

exports.Square = Square;
