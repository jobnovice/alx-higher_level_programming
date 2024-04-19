#!/usr/bin/node

const fs = require('fs');

// check if the file and the string to write is passed to out script
if (process.argv.length !== 4) {
	console.error('Usage: 1-writeme.js filepath StringToWrite');
	process.exit(1);
}

const stringToWrite = process.argv[3];
const filepath = process.argv[2];

fs.writeFile(filepath, stringToWrite, 'utf-8', (err) => {
	if (err){
		process.exit(1);
	}
});