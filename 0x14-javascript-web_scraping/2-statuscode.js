#!/usr/bin/node
/*
 * script that display the status code of a GET request.
*/

const request = require('request');
if (process.argv.length > 2) {
  request.get(process.argv[2]).on('response', function (response) {
    console.log('code:', response.statusCode);
  });
}
