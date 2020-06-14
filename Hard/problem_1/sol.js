function maxGap(num) {
  const binNumArr = num.toString(2).split("1").sort();
  const lastindex = binNumArr.length - 1;
  return binNumArr[lastindex].length;
}

var res = maxGap(32);
console.log(res);
