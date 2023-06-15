#!/usr/bin/node
const length = process.argv.length - 2;
if (length === 0 || length === 1) {
  console.log(0);
} else {
  let largest = parseInt(process.argv[2]);
  let secondLargest = parseInt(process.argv[2]);

  for (let i = 3; i < process.argv.length; i++) {
    let current = parseInt(process.argv[i]);

    if (current > largest) {
      secondLargest = largest;
      largest = current;
    } else if (current > secondLargest && current !== largest) {
      secondLargest = current;
    }
  }

  console.log(secondLargest);
}   
