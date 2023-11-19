#!/usr/bin/node

const argv = process.argv;
const firstArgs = Number(argv[2]);

if (!firstArgs) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArgs; i++) {
    let value = '';
    for (let j = 0; j < firstArgs; j++) {
      value += 'X';
    }
    console.log(value);
  }
}
