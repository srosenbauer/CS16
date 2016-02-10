#!/usr/bin/python

#*********DO NOT CHANGE THIS CODE****************
class InvalidInputException(Exception):
	
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)

#************************************************


def fibonacci():
    """fibonacci: . -> .
    Purpose: Prints out the first 100 fibonacci numbers
    """
    # Your code goes here. remove the 'pass' when you fill in the method
    pass

def factorial(n):
    """factorial: int [n] -> int [n!]
    Purpose: Returns the factorial of the argument
    Example: factorial(4) -> 24
    """
    #*****DO NOT CHANGE THIS CODE*******
    if n < 0:
        raise InvalidInputException('input must be greater than or equal to 0')
    #***********************************
    # Your code goes here, remove the pass when you fill in the method
    pass

# Please put all other executable code and your asserts to test here
if __name__ == '__main__':
    pass
