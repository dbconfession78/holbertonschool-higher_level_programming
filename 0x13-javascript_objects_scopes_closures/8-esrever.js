#!/usr/bin/node
// returns a reversed list based on the given list
exports.esrever = function (list) {
  let retval = [];
  for (let i = 0; i < list.length; i++) {
    retval.push(list[list.length-i-1]);
  }
  return retval;
};
