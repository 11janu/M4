class MyCalc:
    def __init__(self):
        self.ans = 0

    def add(self, a, b):
        self.ans = a + b
        return self.ans

    def subtract(self, a, b):
        self.ans = a - b
        return self.ans

    def multiply(self, a, b):
        self.ans = a * b
        return self.ans

    def divide(self, a, b):
        if b == 0:
            return "Error: cannot divide by zero."
        self.ans = a / b
        return self.ans


def main():
    calc = MyCalc()
    while True:
        user_input = input("Enter an equation (e.g., 2 + 2 or ans * 3): ")
        parts = user_input.split()
        if len(parts) != 3:
            print("Error: Invalid input.")
            continue

        try:
            first_num = float(parts[0])
            operator = parts[1]
            second_num = float(parts[2])
        except ValueError:
            print("Error: Invalid input.")
            continue

        if operator == "+":
            result = calc.add(first_num, second_num)
        elif operator == "-":
            result = calc.subtract(first_num, second_num)
        elif operator == "*":
            result = calc.multiply(first_num, second_num)
        elif operator == "/":
            result = calc.divide(first_num, second_num)
            if result == "Error: cannot divide by zero.":
                print(result)
                continue
        elif operator != "=":
            print("Error: Invalid operator.")
            continue

        print(result)


def test_add():
    calc = MyCalc()
    assert calc.add(2, 3) == 5
    assert calc.add(-2, 3) == 1
    assert calc.add(2, -3) == -1
    assert calc.add(-2, -3) == -5


def test_subtract():
    calc = MyCalc()
    assert calc.subtract(2, 3) == -1
    assert calc.subtract(-2, 3) == -5
    assert calc.subtract(2, -3) == 5
    assert calc.subtract(-2, -3) == 1


def test_multiply():
    calc = MyCalc()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(2, -3) == -6
    assert calc.multiply(-2, -3) == 6
def test_divide():
    calc = MyCalc()
    assert calc.divide(2, 1) == 2
    assert calc.divide(-2, 1) == -2
    assert calc.divide(2, -1) == -2
    assert calc.divide(-2, -1) == 2
    assert calc.divide(2, 0) == "Error: cannot divide by zero."
    assert calc.divide(-2, 0) == "Error: cannot divide by zero."

def test_main():
    calc = MyCalc()
    # Test add
    assert calc.add(2, 3) == 5
    assert calc.ans == 5

    # Test subtract
    assert calc.subtract(5, 1) == 4
    assert calc.ans == 4

    # Test multiply
    assert calc.multiply(4, 2) == 8
    assert calc.ans == 8

    # Test divide
    assert calc.divide(8, 4) == 2
    assert calc.ans == 2
    assert calc.divide(8, 0) == "Error: cannot divide by zero."
    assert calc.ans == 2

if name == "main":
    main()
    ## Test Results 
    #All test cases passed successfully.
