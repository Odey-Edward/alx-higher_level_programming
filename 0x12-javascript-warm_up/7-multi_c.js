#!/usr/bin/node

const argv = process.argv;
const firstArgs = Number(argv[2]);

if (!firstArgs) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArgs; i++) {
    console.log('C is fun');
  }
}
