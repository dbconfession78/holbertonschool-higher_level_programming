#!/usr/bin/node
// the Square class setup to niherit from the rectangle class
const Rectangle = require('./4-rectangle').Rectangle;

exports.Square = function Square (size) {
  Rectangle.call(this, size, size);
};

/*
function Square (size) {
	Rectangle.callI(this, size, size);
}

exports.Square = Square;
*/
