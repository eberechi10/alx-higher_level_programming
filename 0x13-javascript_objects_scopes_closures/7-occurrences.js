#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let elm = 0;

  for (let idx = 0; idx < list.length; idx++) {
    elm = (list[idx] === searchElement ? elm + 1 : elm);
  }

  return elm;
};
