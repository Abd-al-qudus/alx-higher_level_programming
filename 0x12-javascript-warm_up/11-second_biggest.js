#!/usr/bin/node
const argument = process.argv.slice(2);
const length = argument.length;
if (length === 0 || length === 1) {
  console.log(0);
} else {
  const argList = argument.map(str => parseInt(str));
  for (let i = 0; i < argList.length; i++) {
    let j = 0;
    while (j < argList.length) {
      if (argList[i] < argList[j]) {
        const x = argList[i];
        argList[i] = argList[j];
        argList[j] = x;
      }
      j++;
    }
  }
  let i = argList.length - 2; let j = 0;
  while (j === 0) {
    if (argList[i] === argList[i + 1]) {
      i--;
    } else {
      j = 1;
    }
  }
  console.log(argList[i]);
}
