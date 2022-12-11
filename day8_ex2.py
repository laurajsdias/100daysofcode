### Coding exercise 2 from day 8 - Prime Number Checker

def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")

    else:
        print(number, "is not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
