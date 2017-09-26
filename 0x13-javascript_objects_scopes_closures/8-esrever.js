#!/usr/bin/node
// returns a reversed list based on the given list
exports.esrever = function (list) {
  let retval = [];
  for (let i = list.length - 1; i >= 0; i--) {
//  for (let i = 0; i < list.length; i++) {
    retval.push(list[i]);
  }
  return retval;
};
