#Write a function to return the Fibonacci sequence up to the nth number.

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


print(fibonacci(10))