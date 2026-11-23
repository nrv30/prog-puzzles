def collatz(n):
    term = n
    iterations = 1
    while (term > 1):
        if term % 2 == 0:
            term = term/2
        else:
            term =  3*term+1
        iterations+=1
    return iterations

max_iterations = 0
starting_number = 0
for i in range(1, 1_000_000):
    iterations = collatz(i)
    if  iterations > max_iterations:
        max_iterations = iterations
        starting_number = i
print(starting_number)