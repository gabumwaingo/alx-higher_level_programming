#!/usr/bin/node
if (typeof process.argv[2] === 'undefined') {
  console.log('No arguments');
} else {
  console.log(process.argv[2]);
}
