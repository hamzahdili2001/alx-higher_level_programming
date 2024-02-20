#!/usr/bin/node

/*
 *
*/

const request = require('request');
if (process.argv.length > 2) {
	request(`https://swapi-api.alx-tools.com/api/films/${parseInt(process.argv[2], 10)}`, (error, response, body) => {
		if (error) cosole.log(error);
		console.log(JSON.parse(body).title);
	}
	);
}

