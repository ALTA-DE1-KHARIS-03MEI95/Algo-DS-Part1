def primeX(n):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return False
        return True
    count = 0
    number = 2 
    while True:
        if is_prime(number):
            count += 1
            if count == n:
                return number
        number += 1

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29