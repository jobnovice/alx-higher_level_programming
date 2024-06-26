#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const url = process.argv[2];
request(url, function (err, response) {
  if (err) {
    process.exit(1);
  }
  console.log('code:', response.statusCode); // Print the response status code
});
