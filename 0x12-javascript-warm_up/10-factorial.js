#!/usr/bin/node
const num = process.argv.slice(2)[0];
function fact(n) {
  if (isNaN(n) || (n === 0)) {
    return 1;
  }
  return n * fact(n - 1);
}

console.log(fact(num));
