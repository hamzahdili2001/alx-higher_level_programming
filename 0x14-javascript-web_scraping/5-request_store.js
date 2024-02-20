#!/usr/bin/node

/*
 script that prints the number of movies where the character “Wedge Antilles” is present.
*/

const fs = require('fs');
const request = require('request');
if (process.argv.length > 3) {
  request(process.argv[2], (error, response, body) => {
    if (error) console.log(error);
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) console.log('fs error: ', err);
    });
  });
}
