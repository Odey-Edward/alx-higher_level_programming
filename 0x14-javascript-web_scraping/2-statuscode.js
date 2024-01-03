#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', res.statusCode);
});
