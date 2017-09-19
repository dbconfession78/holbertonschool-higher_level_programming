#!/usr/bin/node
// outputs if an argument, arguments or no arguments were passed to this script
if (process.argv.length === 2) {
	console.log('No argument');
} else if (process.argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
