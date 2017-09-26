#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present
const request = require('request');
const url = 'https://swapi.co/api/people/18';
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(response.body)['films'].length);
  }
});
