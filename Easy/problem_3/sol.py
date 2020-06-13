def factorial(num):
    if num == 0 or num < 1:
        raise Exception(
            "Invalid Input, 0 or Negative numbers are not allowed.")
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
        return factorial

# better and faster approach to use math.factorial(number)


output = factorial(1)
print(output)
