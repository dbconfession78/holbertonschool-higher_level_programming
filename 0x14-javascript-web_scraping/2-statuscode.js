#!/usr/bin/node
// displays staus code of get request
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
