#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
const characters = [];

request(url, async function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const characterData = JSON.parse(body).characters;
    characters.push(...characterData);
  }
});

let i = 0;
while (i < characters.length) {
  const res = await new Promise((resolve, reject) => {
    request(characters[i], (err, res, html) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(html).name);
      }
    });
  });
  console.log(res);
  i++;
}
