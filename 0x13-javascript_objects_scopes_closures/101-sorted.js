#!/usr/bin/node
const oDict = require('./101-dict').dict;
let list = [];
let retval = {};

for (let key in oDict) {
  const val = oDict[key];
  if (contains(list, val) === false) {
    list.push(val);
  }
}
list.sort();

for (let i in list) {
  let idList = [];
  for (let key in oDict) {
    const val = oDict[key];
    if (val === list[i]) {
      idList.push(key);
    }
  }
  retval[list[i]] = idList;
}
console.log(retval);


function contains (list, n) {
  for (let i in list) {
    if (list[i] === n) {
      return true;
    }
  }
  return false;
}
