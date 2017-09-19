#!/usr/bin/node
// outputs if an argument, arguments or no arguments were passed to this script
const args = process.argv;
if (args.length <= 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
