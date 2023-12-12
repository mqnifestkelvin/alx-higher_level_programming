#!/usr/bin/node
// Prints and logs number of calls
exports.logMe = function (item) {
  if (this.times === undefined) {
    this.times = 0;
  }
  console.log(`${this.times}: ${item}`);
  this.times++;
};
