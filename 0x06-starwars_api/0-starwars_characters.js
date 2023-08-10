#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, async function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const characterUrl of characters) {
      const characterName = await new Promise((resolve, reject) => {
        request(characterUrl, (err, res, html) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(characterName);
    }
  }
});
