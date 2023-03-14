#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let square = '';
  if (size > 1) {
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) {
        square += 'X';
      }
      if (i !== size - 1) {
        square += '\n';
      }
    }
    console.log(square);
  }
  if (size === 1) {
    console.log('X');
  }
}
