#!/usr/bin/node

exports.converter = function (base) {
  return (elm) => {
    return elm.toString(base);
  };
};
