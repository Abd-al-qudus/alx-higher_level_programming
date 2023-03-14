#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
add(a, b);
