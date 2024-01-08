#!/usr/bin/node
const myStr = 'C is fun';
const x = parseInt(process.argv[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log(myStr);
  }
} else {
  console.log('Missing number of occurrences');
}
