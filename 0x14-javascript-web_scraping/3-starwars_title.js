#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const base = 'https://swapi.co/api/films/' + args[0];
request.get(base, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(response.body)['title']);
  }
});
