
from MyCalc import MyCalc
import pytest
def test_add():
    # UCID: js2679
    # Date: 19-04-2023
    # creates an object calc and tests whether 2+3 is 5 using assert
    calc = MyCalc()
    assert calc.add(2, 3) == 5
    assert calc.add(8, 4) == 12
    assert calc.add(10, 4) == 14


def test_ans_add():
    # UCID: js2679
    # Date: 19-04-2023
    # creates an object calc and assigns answer as 2 and tests whether ans+3 is 5 using assert
    calc = MyCalc()
    calc.ans = 2
    assert calc.add(calc.ans, 3) == 5
    assert calc.add(calc.ans, 3) == 8
    assert calc.add(calc.ans, 3) == 11


def test_subtract():
    # UCID: js2679
    # Date: 19-04-2023
    # creates an object calc and tests whether 5-3 is 2 using assert
    calc = MyCalc()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(2, 1) == 1
    assert calc.subtract(10, 4) == 6

def test_ans_subtract():
    # UCID: js2679
    # Date: 19-04-2023
    # creates an object calc and assigns answer as 5 and tests whether ans-3 is 2 using assert
    calc = MyCalc()
    calc.ans = 5
    assert calc.subtract(calc.ans, 3) == 2
    assert calc.subtract(calc.ans, 1) == 1
    assert calc.subtract(calc.ans, 1) == 0

def test_multiply():
    # UCID: js2679
    # Date: 19-04-2023
    # creates an object calc and tests whether 2*3 is 6 using assert
    calc = MyCalc()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(5, 2) == 10
    assert calc.multiply(12, 2) == 24

def test_ans_multiply():
    # UCID: js2679
    # Date: 19-04-2023  
    # creates an object calc and assigns answer as 2 and tests whether ans*3 is 6 using assert 
    calc = MyCalc()
    calc.ans = 2
    assert calc.multiply(calc.ans, 3) == 6
    assert calc.multiply(calc.ans, 3) == 18
    assert calc.multiply(calc.ans, 3) == 54

def test_divide():
    # UCID: js2679
    # Date: 19-04-2023
    # creates an object calc and tests whether 6/3 is 2 using assert
    calc = MyCalc()
    assert calc.divide(6, 3) == 2
    assert calc.divide(8, 4) == 2
    assert calc.divide(9, 3) == 3

def test_ans_divide():
    # UCID: js2679
    # Date: 19-04-2023
    # creates an object calc and assigns answer as 6 and tests whether ans/3 is 2 using assert
    calc = MyCalc()
    calc.ans = 6
    assert calc.divide(calc.ans, 3) == 2
    assert calc.divide(calc.ans, 2) == 1
    assert calc.divide(calc.ans, 1) == 1

test_add()
test_ans_add()
test_subtract()
test_ans_subtract()
test_multiply()
test_ans_multiply()
test_divide()
test_ans_divide()

