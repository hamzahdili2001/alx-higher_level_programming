#!/usr/bin/node

const myNumber = parseInt(process.argv[2]);

if (!isNaN(myNumber)) {
  console.log('My number:', myNumber);
} else {
  console.log('Not a number');
}
