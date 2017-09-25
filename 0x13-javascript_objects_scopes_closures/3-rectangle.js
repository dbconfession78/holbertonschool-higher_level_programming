#!/usr/bin/node
exports.Rectangle = function Rectangle(w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }

  Rectangle.prototype.print = function print() {
    for (let i=0; i < this.height; i++) {
      for (let j=0; j < this.width; j++) {
        process.stdout.write('X')
      }
      console.log('')
    }
  };
};
