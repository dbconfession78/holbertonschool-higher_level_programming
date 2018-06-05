#!/usr/bin/node
// counts the number of occurances in a list
exports.nbOccurences = function (list, searchElement) {
  let retval = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      retval++;
    }
  }
  return retval;
};
