#A mersenne prime is a prime number that is 1 less than a power of 2
#E.g 127 is 2^7 -1

from math import ceil

def main():
    found = 0
    power = 0
    
    while found < 10:
        if prime(power):
            num = pow(2, power) - 1
            if power > 2:
                if mersenne(num, power):
                    print(f"2^{power} - 1 = {num}")
                    found += 1
            else:
                if prime(num):
                    print(f"2^{power} - 1 = {num}")
                    found += 1
        power += 1


def prime(num):
    flag = True
    
    if num < 2:
        flag = False
    else:
        for i in range(2, ceil(num / 2) + 1):
            if num % i == 0:
                flag = False
                break
    return flag

#Implements the lucas-lehemer test
def mersenne(num, power):
    x = 4
    for i in range(power - 2):
        x = (pow(x, 2) - 2) % num

    if x == 0:
        return True
    return False



main()
