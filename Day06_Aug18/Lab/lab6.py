#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers
def gcd(num1, num2):
    if max(num1, num2) % min(num1, num2) == 0: return min(num1, num2)
    return gcd(min(num1, num2), max(num1, num2) % min(num1, num2))

#Exercise 2
#Write a function that returns prime numbers less than 121
def findprime(num):
    if num == 1: return None
    i = 1
    remainder = []
    while i <= num:
        remainder.append(num % i)
        i += 1
    if remainder.count(0) < 3: print num
    return findprime(num - 1)

def findprime2(num):
    if 'prime' not in globals():
        global prime
        prime = []
    if num == 2:
        result = prime
        del globals()['prime']
        return result
    i = 1
    remainder = []
    while i <= num:
        remainder.append(num % i)
        i += 1
    if remainder.count(0) < 3: prime.append(num - 1)
    return findprime2(num - 1)

# This is the one that only prints
findprime(121)
# This is the one that stores
print findprime2(121)

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html

def tower(disk, source, spare, dest):
    if disk == 1:
        print "Move %s from %s to %s" %(disk, source, dest)
    else:
        tower(disk - 1, source, dest, spare)
        print "Move %s from %s to %s" %(disk, source, dest)
        tower(disk - 1, spare, source, dest)
