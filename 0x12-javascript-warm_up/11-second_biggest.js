#!/usr/bin/node
const args = process.argv.slice(2);
const num = args[0];
let list = [];
for (let i = 0; i < args.length; i++) {
  list[i] = parseInt(args[i]);
}

let sec_biggest = function(list) {
  if (list.length <= 1) {
    return (0);
  }
  let max = Math.max.apply(Math, list);
  let newList = [];
  let x = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] != max) {
      newList[x] = list[i];
      x++;
    }  
  }
  return Math.max.apply(Math, newList);
}
const sec_high = sec_biggest(list);
console.log(sec_high);
