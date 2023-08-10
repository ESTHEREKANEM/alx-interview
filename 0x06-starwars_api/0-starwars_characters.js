#!/usr/bin/node
const request = require('request');

function getMovieCharacters(movieId) {
    const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

    request.get(filmUrl, (error, response, body) => {
        if (error) {
            console.log(`Error fetching film data for Movie ID ${movieId}`);
            return;
        }

        const filmData = JSON.parse(body);
        const characters = filmData.characters;

        console.log(`Characters in ${filmData.title} (Episode ${filmData.episode_id}):`);
        characters.forEach(characterUrl => {
            request.get(characterUrl, (characterError, characterResponse, characterBody) => {
                if (characterError) {
                    console.log(`Error fetching character data for ${characterUrl}`);
                    return;
                }

                const characterData = JSON.parse(characterBody);
                console.log(characterData.name);
            });
        });
    });
}

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <Movie ID>");
    process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
