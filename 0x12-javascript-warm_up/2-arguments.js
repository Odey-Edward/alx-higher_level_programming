#!/usr/bin/node

const argv = process.argv;

if (argv[2] == null) {
  console.log('No argument');
} else if (argv[3] != null) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
