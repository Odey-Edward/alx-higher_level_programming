#!/usr/bin/node

const argv = process.argv;
const firstArgs = Number(argv[2]);

if (isNaN(firstArgs)) {
  console.log('Not a number');
} else {
  console.log('My number:', firstArgs);
}
