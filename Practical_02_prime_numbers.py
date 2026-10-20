def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print(n, "is prime" if is_prime(n) else "is not prime")

limit = int(input("Print all primes up to: "))
print([i for i in range(2, limit + 1) if is_prime(i)])
