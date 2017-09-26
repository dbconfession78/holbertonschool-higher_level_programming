#!/usr/bin/node
// returns a reversed list based on the given list
exports.esrever = function (list) {
  let retval = [list.length];
  for (let i=0; i < list.length; i += 1) {
    retval[i] = list[list.length-i-1];
  }
  return (retval);
};

