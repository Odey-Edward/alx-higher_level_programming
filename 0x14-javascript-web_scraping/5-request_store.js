#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const argv = process.argv;

const fileStream = fs.createWriteStream(argv[3]);

request(argv[2])
  .on('error', (error) => {
    console.log(error);
  })
  .pipe(fileStream)
  .on('finish', () => {
    fileStream.end();
  });
