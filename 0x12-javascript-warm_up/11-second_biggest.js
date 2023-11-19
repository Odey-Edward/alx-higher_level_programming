#!/usr/bin/node

const argv = process.argv;
const args = argv.slice(2);
let high = 0;
let secondHigh = 0;

if (argv.length <= 3) {
  console.log(0);
  process.exit();
}

for (let i = 0; i < (args.length); i++) {
  if (args[i] > high) {
    high = args[i];
  }
}

for (let i = 0; i < (args.length); i++) {
  if (args[i] < high && args[i] > secondHigh) {
    secondHigh = args[i];
  }
}

console.log(secondHigh);
