#!/usr/bin/node
let s;
if (process.argv.length < 3) {
    s = 'No argument\n';
} else if (process.argv.length === 3) {
    s = 'Argument found\n';
} else {
    s = 'Arguments found\n';
}
console.log(s);