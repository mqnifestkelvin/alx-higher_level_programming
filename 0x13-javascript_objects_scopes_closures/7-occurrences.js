#!/usr/bin/node
// counts number of occurences of element in list
exports.nbOccurences = function (list, searchElement) {
    return list.filter(x => x === searchElement).length;
};