#!/usr/bin/node

const { argv } = require('node:process');
const num = Number(argv[2]);

if (!num) {
  console.log(1);
  process.exit();
}
function factorial (number) {
  if (number === 1) {
    return (1);
  }
  return (factorial(number - 1) * number);
}

console.log(factorial(num));
