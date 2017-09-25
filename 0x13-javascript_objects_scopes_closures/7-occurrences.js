#!/usr/bin/node
// counts the number of occurances in a list
exports.nbOccurences = function (list, search_element) {
  let retval = 0;
  for (let i = 0; i < list.length; i += 1) {
    if (list[i] == search_element) {
      retval += 1;
    }
  }
  return retval;
};
