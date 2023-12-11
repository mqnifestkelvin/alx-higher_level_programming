#!/usr/bin/node
const numericArgs = process.argv.slice(2).map(Number).filter(n => !isNaN(n));
console.log(numericArgs.length < 2 ? 0 : numericArgs.sort((a, b) => b - a)[1]);
