def prime(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return i
        i += 1
    return n
def prime(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return i
        i += 1
    return n
def generate_primes_grid(width, height, start):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = ""
    num = start + 1
    for _ in range(height):
        row = []
        while len(row) < width:
            if is_prime(num):
                row.append(num)
            num += 1
        result += ' '.join(map(str, row)) + "\n"

    return result


if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """