def fibonacci(n):
    fib_series = [0, 1] # starting with the first two numbers in the series
    
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])  # adding the next number to the series
        
    return fib_series[:n]

# the number of Fibonacci numbers to generate
n = int(input("Enter any number on which do you want to end the fibonacci sereies "))
fib_sequence = fibonacci(n)
print(fib_sequence)