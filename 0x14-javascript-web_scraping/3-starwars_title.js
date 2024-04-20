#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const eop = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${eop}`;

request(url, function (err, response, body) {
  if (err) {
    process.exit(1);
  }
  const r1 = JSON.parse(body);
  console.log(r1.title);
});
