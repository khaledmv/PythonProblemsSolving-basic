#Prime Numbers

# Write a function that returns a list of all prime numbers up to a given number.

def is_prime(n) : 
    if n <= 1 :
        return False
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    return True


def prime_number_up_to(n) : 
    return [x for x in range(2, n+1) if is_prime(x)]

print(prime_number_up_to(20))