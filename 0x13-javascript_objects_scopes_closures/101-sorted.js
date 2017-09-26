#!/usr/bin/node
const oDict = require('./101-data').dict;
let fDict = {};

for (let key in oDict) {
  const count = oDict[key];
  if (!(count in fDict)) {
    fDict[count] = [key];
  } else {
    fDict[count].push(key);
  }
}
console.log(fDict);
