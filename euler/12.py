# returns a list of all the divisors of n
def factor(n):
    factors = []
    i = 1
    while (i**2 < n):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
        i+=1
    return factors

i = 1
while (True): 
    term = 0
    for j in range(1, i+1):
        term+=j
    if len(factor(term)) >= 500:
        print(term)
        break
    i += 1