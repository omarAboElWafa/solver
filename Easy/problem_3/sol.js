function factorial(num) {
  if (num === 1) return 1;
  else if (num === 0) {
    throw new Error("Error! Factorial of 0 is not valid.");
  } else if (num < 0) {
    throw new Error("Error! Factorial of Negative numbers is not valid.");
  } else {
    let factorial = 1;
    for (let i = 1; i <= num; i++) {
      factorial *= i;
    }
    return factorial;
  }
}
