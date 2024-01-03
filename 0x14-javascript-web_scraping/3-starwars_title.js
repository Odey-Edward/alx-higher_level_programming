#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const id = argv[2] + '/';

request('https://swapi-api.alx-tools.com/api/films/' + id, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const jsonData = JSON.parse(body);
  console.log(jsonData.title);
});
