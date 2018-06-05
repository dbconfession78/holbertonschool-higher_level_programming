#!/usr/bin/node
// writes a file to a string
const args = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(args[0], args[1], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {

  }
});
