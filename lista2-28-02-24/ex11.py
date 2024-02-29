# Escreva um programa que identifique todos os números
# primos em uma lista de números inteiros


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_numbers(numbers):
    return [n for n in numbers if is_prime(n)]

print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(prime_numbers([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))