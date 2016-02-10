#!/usr/bin/python
from datetime import date
from sectionOne import InvalidInputException

def is_prime(n):
    """is_prime: int [number to test] -> boolean [primality]
    Purpose: Test whether a number is prime or not
    Example: is_prime(15) -> False
    """
    n = get_today()
    if (n < 0) or (n > 31):
        raise InvalidInputException("input must be greater than or equal to 0 and less than 31")

    if (n == 0) or (n == 1):
        return False

    if (n > 1):
        for i in range(2, n):
            if (n % i == 0):
                 return False
        
        return True


def get_today():
    """get_today: -> int [the day]
    Purpose: Get the day of the month
    """
   

def test_is_prime():
    assert is_prime(2) == True, "Boolean failure"
    assert is_prime(1) == False, "Boolean failure"
    assert is_prime(0) == False, "Boolean failure"
    assert is_prime(17) == True, "Boolean failure"


# Please put all other executable code and your asserts to test here
if __name__ == '__main__':
    test_is_prime()
