#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}
const url = process.argv[2];
const characterId = '18';
let played = 0;

request(url, function (err, response, body) {
  if (err) {
    process.exit(1);
  }
  const films = JSON.parse(body);
  for (const film of films.results) {
    for (const char of film.characters) {
      if (char.includes(characterId)) {
        played++;
      }
    }
  }
  console.log(played);
});
