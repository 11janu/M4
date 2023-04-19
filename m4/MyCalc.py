# UCID: js2679
# Date: 19-04-2023
import pytest
class MyCalc:
    def __init__(self):
        # UCID: js2679
        # Date: 19-04-2023
        self.ans = 0

    def add(self, x, y):

    # UCID: js2679
    # Date: 19-04-2023
    # x and y values are taken from main method and added here and self.ans is returned to main
        self.ans = x + y
        return self.ans

    def subtract(self, x, y):
        # UCID: js2679
        # Date: 19-04-2023
        # x and y values are taken from main method and subtracted here and self.ans is returned to main
        self.ans = x - y
        return self.ans

    def multiply(self, x, y):
        # UCID: js2679
        # Date: 19-04-2023
        # x and y values are taken from main method and multiplied here and self.ans is returned to main
        self.ans = x * y
        return self.ans

    def divide(self, x, y):
        # UCID: js2679
        # Date: 19-04-2023
        # x and y values are taken from main method and divided here
        # if  the denominator is 0, then error is printed else, x/y is calculated and returned
        if y == 0:
            print("Error: division by zero")
            return None
        else:
            self.ans = x / y
            return self.ans

if __name__ == '__main__':
    # UCID: js2679
    # Date: 19-04-2023
    calc = MyCalc()
    while True:
        user_input = input("Enter a math expression: ")
        if user_input == "exit":
            break
        try:
            result = eval(user_input, {"__builtins__": None}, {"ans": calc.ans})
            print(result)
            calc.ans = result
        except (SyntaxError, ZeroDivisionError) as e:
            print(f"Error: {e}")




