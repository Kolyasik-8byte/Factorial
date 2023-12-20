from factorial import Factorial
def test_factorial():
    test_cases = [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800)
    ]
    factorial = Factorial().factorial
    for n, expected_result in test_cases:
        result = factorial(n=n)
        test_string = f"Факторіал числа {n} має бути {expected_result}"
        if result == expected_result:
            print(test_string + " - Ok")
        else:
            print(test_string + f" - Error, отримано {result}")

if __name__ == '__main__':
    test_factorial()