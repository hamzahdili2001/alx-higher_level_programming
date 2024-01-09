#!/usr/bin/node

const data = require('./101-data.js');

function invertDictionary (inputDict) {
  const outputDict = {};
  for (const userId in inputDict) {
    const occurrences = inputDict[userId];
    if (outputDict[occurrences]) {
      outputDict[occurrences].push(userId);
    } else {
      outputDict[occurrences] = [userId];
    }
  }
  return outputDict;
}

const invertedData = invertDictionary(data.dict);
console.log(invertedData);
