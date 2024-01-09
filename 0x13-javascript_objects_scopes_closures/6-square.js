#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (letter = 'X') {
    for (let i = 0; i < this.height; i++) { console.log(letter.repeat(this.width)); }
  }
};
