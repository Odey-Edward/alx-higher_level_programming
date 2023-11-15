#!/usr/bin/node

exports.esrever = function (list) {
  const revesed = [];
  let i;

  for (i = (list.length - 1); i >= 0; i--) {
    revesed.push(list[i]);
  }
  return (revesed);
};
