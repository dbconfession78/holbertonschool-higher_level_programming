#!/usr/bin/node
// a Rectangle constructor with conditional width and height
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
};
