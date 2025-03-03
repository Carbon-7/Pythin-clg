def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for number in range(1, 21):
    if is_prime(number):
        print(number)

#code is AI generated