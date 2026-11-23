def p0(n):
    answer = 0
    for i in range(1,n):
        square = i**2
        if (i % 2 != 0):
            answer += square
    print(answer)

def p1(n):
    answer = 0
    for i in range(1, n):
        if (i % 3 == 0 or i % 5 == 0):
            answer += i
    print(answer)

from collections import deque
def p2(n):
    answer = 0
    dq = deque([1, 2])
    i = dq[1]
    limit = 4_000_000
    while (i < limit):
        if (i % 2 == 0):
            answer += i
        i = dq.popleft() + dq[0]
        dq.append(i)
    print(answer)

def prime_factors(n, factors):
    divisor = None
    for i in range(2, n+1):
        if n % i == 0:
            divisor = i
            break
    if divisor != None:
        print(f'{divisor} {n // divisor}')
        factors.append(divisor)
        return prime_factors(n//divisor, factors)
    else:
        return factors


def p3(n):
    factors = []
    factors = prime_factors(n, factors)
    largest = 0
    for factor in factors:
        if factor > largest:
            largest = factor
    print(largest)


def p4():
    max_pal = 0
    for i in range (999,99, -1):
        for j in range(999, 99, -1):
            prod = str(i*j)
            if prod == prod[::-1]:
                pal = int(prod)
                if pal > max_pal:
                    max_pal = pal
                else:
                    break
    return max_pal


# Source - https://stackoverflow.com/a
# Posted by Colonel Panic, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-08, License - CC BY-SA 3.0
from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)

from functools import reduce
def p5():
    return reduce(lcm, range(1, 21))

def p6():
    sum_of_squares = 0
    s = 0
    for i in range(1, 101):
        sum_of_squares += i**2
        s += i

    return s**2 - sum_of_squares

from math import log, ceil
def p7(n):
    upper_bound = ceil(n * (log(n) + log(log(n))))
    nums = [True] * upper_bound
    i = 2
    while (i**2 < upper_bound):
        if nums[i] is True:
            print(f'----- {i} -----')
            j = i**2
            counter = 1
            while (j < upper_bound):
                print(j)
                if nums[j] is True:
                    nums[j] = False
                j = i**2 + i*counter
                counter += 1
        i+=1
    answer = [i for i in range(2, len(nums)) if nums[i] is True]
    print(answer)
    print(f'my answer = {answer[n-1]}')
    
def p10(n):
    nums = [True] * n
    i = 2
    while (i**2 < n):
        if nums[i] is True:
            j = i**2
            counter = 1
            while (j < n):
                if nums[j] is True:
                    nums[j] = False
                j = i**2 + i*counter
                counter += 1
        i+=1
        answer = [i for i in range(2, len(nums)) if nums[i] is True]
        for a in answer:
            print(a)

if __name__ == "__main__":
    # part1(485_000)
    # part2(1000)
    # part3(10)
    # factors = p3(600851475143)
    # print(p4())
    # print(p5())
    # print(p6())
    # p7(10_001)
    p10(10)