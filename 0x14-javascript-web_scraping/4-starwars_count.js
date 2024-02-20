#!/usr/bin/node

/*
 script that prints the number of movies where the character “Wedge Antilles” is present.
*/

const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log(error);
  const data = JSON.parse(body);
  let sum = 0;
  for (const result of data.results) {
    sum += result.characters.filter(value => value.includes('18')).length;
  }
  console.log(sum);
});
