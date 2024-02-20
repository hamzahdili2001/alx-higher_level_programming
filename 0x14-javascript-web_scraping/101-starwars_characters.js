#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movieId = parseInt(process.argv[2], 10);
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Unexpected status code: ${response.statusCode}`);
    } else {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;
      const characterPromises = characters.map(characterUrl => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              reject(new Error(error)); // Use Error object as rejection reason
            } else if (response.statusCode !== 200) {
              reject(new Error(`Unexpected status code: ${response.statusCode}`)); // Use Error object as rejection reason
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData.name);
            }
          });
        });
      });

      Promise.all(characterPromises)
        .then(characterNames => {
          characterNames.forEach(name => console.log(name));
        })
        .catch(error => {
          console.error('Error fetching character data:', error.message);
        });
    }
  });
}
