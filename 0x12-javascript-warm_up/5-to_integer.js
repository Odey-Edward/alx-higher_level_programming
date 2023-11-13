#!/usr/bin/node

const { argv } = require('node:process');
const firstArgs = Number(argv[2]);

if (isNaN(firstArgs)) {
  console.log('Not a number');
} else {
  console.log('My number:', firstArgs);
}
