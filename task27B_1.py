# Pairs from a sequence

# Task 1:
# Given number n, then n numbers.
# You need to print the number of pairs, whose sum is a multiple of 9.
from random import randint

n = randint(400, 8000)
a = [randint(100, 1000) for _ in range(n)]


# ineffective solution O(N*N)
def ne_eff_1(a):
    n = len(a)
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 9 == 0:
                counter += 1
    return counter


# effective solution O(N)
def eff_1(a):
    n = len(a)
    counter = 0
    remainder = [0] * 9
    for i in range(n):
        # counting amount of pairs with current number
        counter += remainder[(9 - a[i] % 9) % 9]
        # recounting statics
        remainder[a[i] % 9] += 1
    return counter


# Task 2:
# Given number n, then n numbers.
# You need to print the number of pairs, whose product is divisible by 15.


# ineffective solution O(N*N)
def ne_eff_2(a):
    n = len(a)
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] * a[j]) % 15 == 0:
                counter += 1
    return counter


def eff_2(a):
    n = len(a)
    counter = 0
    line = [0] * 15
    for i in range(n):
        if a[i] % 15 == 0:
            counter += sum(line)
        elif a[i] % 5 == 0:
            counter += line[3]
        elif a[i] % 3 == 0:
            counter += line[5]
        else:
            counter += line[0]
        line[a[i] % 15] += 1
    return counter


for t in range(1009):
    n = randint(5, 10)
    a = [randint(2, 30) for _ in range(n)]
    if eff_2(a) != ne_eff_2(a):
        print(a, eff_2(a), ne_eff_2(a))
