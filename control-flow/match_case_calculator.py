num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):").strip().lower()
match operation:
    case '+':
        result = num1 + num2
        print(f'The result of', num1, '+', num2, '=', result)
    case '-':
        result = num1 - num2
        print(f'The result of', num1, '-', num2, '=', result)
    case '*':
        result = num1 * num2
        print(f'The result of', num1, '*', num2, '=', result)
    case '/':
        result = num1 / num2
        print(f'The result of', num1, '/', num2, '=', result)