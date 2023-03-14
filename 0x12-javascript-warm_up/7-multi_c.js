#!/usr/bin/node
const times = process.argv[2];
if (times === 0 || isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  if (times >= 1) {
    for (let i = 0; i < times; i++) {
      console.log('C is fun');
    }
  }
}
