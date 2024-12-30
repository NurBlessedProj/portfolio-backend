# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    count = int(input("How many prime numbers would you like to display? "))

    primes = []
    num = 2

    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    print(f"The first {count} prime numbers are: {primes}")


# Run the program
main()
