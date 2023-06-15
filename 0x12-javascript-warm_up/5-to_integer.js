#!/usr/bin/node
const n = Math.floor(Number(process.argv[2]));
console.log(isNan(n) ? 'Not a number' : `My number: ${n}`);
