#!/usr/bin/node
// converts a number from base 10 to another number base
exports.converter = function (base) {
  this.base = base;
  return function test (n) {
    return (n.toString(base));
  };
};
