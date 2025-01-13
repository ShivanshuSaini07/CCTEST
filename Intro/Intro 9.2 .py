import random
number = random.randint(1, 100)
is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))
print(number, is_prime)
