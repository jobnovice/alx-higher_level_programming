#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const id = parseInt(process.argv[2]);
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (err, response) {
  if (err) {
    process.exit(1);
  }
  const film = JSON.parse(response.body);
  const chars = film.characters;

  for (const i of chars) {
    request(i, function (err, response) {
      if (err) {
        process.exit(1);
      }
      const res = JSON.parse(response.body);
      console.log(res.name);
    });
  }
});
