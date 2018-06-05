#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present
const request = require('request');
const url = process.argv.slice(2)[0];
let count = 0;
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(response.body)['results'];
    for (let i in results) {
      const characters = results[i]['characters'];
      for (let j in characters) {
        if (characters[j].includes('18')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
