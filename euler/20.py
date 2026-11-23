def factorial(n):
    if n == 2:
        return n
    else:
        return n * factorial(n-1)

def iterative_factorial(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

total = 0
num_str = str(factorial(100))
for i in range(len(num_str)):
    total += int(num_str[i])
print(total)