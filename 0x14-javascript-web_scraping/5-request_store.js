#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4){
	console.log('Usage: 5-request_store.js URL filepath');
	process.exit(1);
}

const url = process.argv[2];
const filepath = process.argv[3];

request(url).pipe(fs.createReadStream(filepath, 'utf-8', (err) => {
	if (err){
		process.exit(1);
	}
}));