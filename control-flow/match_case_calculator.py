num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
op = input('Choose the operation (+, -, *, /): ')

if op == '+':
    print(f'The result is {num1 + num2}.')
elif op == '-':
    print(f'The result is {num1 - num2},')
elif op == '*':
    print(f'The result is {num1 * num2}.')
else: # devision
    if num2 == 0:
        print('Cannot divide by zero.')
    else:
        print(f'The result is {num1 / num2}.')
    
