#!/usr/bin/node

/*
 *
*/

const request = require('request');
if (process.argv.length > 2) {
  request(process.argv[2], (error, response, body) => {
    if (error) console.log(error);
    const films = JSON.parse(body).results;
    let count = 0;
    const character = 'https://swapi-api.alx-tools.com/api/people/18/';
    for (const film of Object.keys(films)) {
      if (films[film].characters.includes(character, 0)) {
        count++;
      }
    }
    console.log(count);
  });
}
