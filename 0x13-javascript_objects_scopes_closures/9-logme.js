#!/usr/bin/node
// prints current argument count, follow by the new argument
let count = 0;
exports.logMe = function (item) {
  console.log(count++ + ': ' + item);
};
