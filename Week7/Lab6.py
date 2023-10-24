# Lab6
# Author:
import test.py
import math 
## add in functions from test.py's test statements here to make the pytest work


def test_rectangle_area(length, width):
    return length*width

def test_pythagorean_theorem(opposite, adjacent):
    return(math.sqrt(opposite**2 + adjacent**2))
    
def is_even(number):
    return (number%2==0)

def test_find_maximum(num1, num2):
    return max(num1,num2)

def test_grade_calculator(grade):
    if 0<= grade <= 100:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >=60:
            return "D" 
        elif grade >= 50:
            return "F"
        else:
            return "Invalid Score"

def main():
    pass

if __name__ == "__main__":
    main()
