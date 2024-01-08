#!/usr/bin/node
const ints = [];
const length = process.argv.length - 2;
if (process.argv.length <= 3) {
  console.log(1);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    ints.push(process.argv[i]);
  }
  console.log(ints.sort()[length - 2]);
}
