#!/usr/bin/node
const args = process.argv.slice(2);
const n = args[0];
if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    console.log('X'.repeat(n))
  }
}
