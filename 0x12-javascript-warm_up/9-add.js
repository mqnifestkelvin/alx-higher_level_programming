#!/usr/bin/node
function add (a, b) {
  return parseInt(a, 10) + parseInt(b, 10);
}

console.log(add(process.argv[2], process.argv[3]));
