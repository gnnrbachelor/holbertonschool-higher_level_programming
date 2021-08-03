#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const num = list.filter(element => element === searchElement).length;
  return (num);
};
