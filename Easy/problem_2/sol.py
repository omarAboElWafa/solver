def print_even(n):
    for i in range(0, n):
        if i % 2 == 0:
            print(i)


def print_odd(n):
    for i in range(0, n):
        if i % 2 != 0:
            print(i)


print_even(100)
print_odd(100)
