#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const jsonData = JSON.parse(body);
  let count = 0;
  for (const el of jsonData.results) {
    const result = el.characters.find((value) => value.endsWith('/18/'));
    if (result !== undefined) {
      count += 1;
    }
  }
  console.log(count);
});
