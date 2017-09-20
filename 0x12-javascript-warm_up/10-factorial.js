#!/usr/bin/node
const args = process.argv.slice(2);
num = args[0];

/*
let fact = function(n) {
  if (n == 0 || isNaN(n)) {
    return (1);
  }
  return fact(n - 1) * n;
}
*/

function fact(n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return fact(n - 1) * n;
}


console.log(fact(num));
