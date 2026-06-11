def is_prime(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_factorial(n):
    """Calcula o fatorial de um número."""
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result