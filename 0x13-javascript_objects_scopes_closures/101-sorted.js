#!/usr/bin/node
const oDict = require('./101-dict').dict;
let list = [];
retval = {};

for (key in oDict) {
  const val = oDict[key]
  if (contains(list, val) === false) {
    list.push(val);
  }
}

for (i in list) {
  idList = []
  for (key in oDict) {
    const val = oDict[key];
    if (val === list[i]) {
      idList.push(key);
    }
  }
  retval[list[i]] = idList;
}
console.log(retval);


function contains (list, n) {
  for (i in list) {
    if (list[i] === n) {
      return true;
    }
  }
  return false;
}
