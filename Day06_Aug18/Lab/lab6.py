#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers
def gcd(num1, num2):
    remainder = max(num1, num2) % min(num1, num2)
    if remainder == 0:
        return min(num1, num2)
    return gcd(min(num1, num2), remainder)

#Exercise 2
#Write a function that returns prime numbers less than 121

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html
