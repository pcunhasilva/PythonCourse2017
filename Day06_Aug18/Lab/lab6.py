#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers
def gcd(num1, num2):
    if max(num1, num2) % min(num1, num2) == 0: return min(num1, num2)
    return gcd(min(num1, num2), max(num1, num2) % min(num1, num2))

#Exercise 2
#Write a function that returns prime numbers less than 121
def findprime(num):
    if num == 1:
        return None
    i = 1
    remainder = []
    while i <= num:
        remainder.append(num % i)
        i += 1
    if remainder.count(0) < 3:
        print num
    return findprime(num - 1)


# def findprime(num):
#     if num == 1:
#         return None
#     i = 1
#     remainder = []
#     while i <= num:
#         remainder.append(num % i)
#         i += 1
#     if remainder.count(0) < 3:
#         return num
#     prime = []
#     prime.append(findprime(num - 1))
#     return prime

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html
