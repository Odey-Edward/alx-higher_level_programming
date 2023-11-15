#!/usr/bin/node

const argv = process.argv;

if (argv[2] == null) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
