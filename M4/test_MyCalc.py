
from MyCalc import MyCalc
import pytest
def test_add():
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    assert calc.add(2, 3) == 5

def test_ans_add():
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    calc.ans = 2
    assert calc.add(calc.ans, 3) == 5

def test_subtract():
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    assert calc.subtract(5, 3) == 2

def test_ans_subtract():
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    calc.ans = 5
    assert calc.subtract(calc.ans, 3) == 2

def test_multiply():
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    assert calc.multiply(2, 3) == 6

def test_ans_multiply():
    # UCID: js2679
    # Date: 19-04-2023   
    calc = MyCalc()
    calc.ans = 2
    assert calc.multiply(calc.ans, 3) == 6

def test_divide():
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    assert calc.divide(6, 3) == 2

def test_ans_divide():
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    calc.ans = 6
    assert calc.divide(calc.ans, 3) == 2

def test_divide_by_zero():
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    assert calc.divide(6, 0) == None

test_add()
test_ans_add()
test_subtract()
test_ans_subtract()
test_multiply()
test_ans_multiply()
test_divide()
test_ans_divide()
test_divide_by_zero()
