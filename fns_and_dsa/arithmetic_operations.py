from operator import add, sub, mul, truediv


op_d = {'add': add, 'subtract': sub, 'multiply': mul, 'divide': truediv}

def perform_operation(num1, num2, operation):
    try:
        return op_d[operation](num1, num2)
    except ZeroDivisionError:
        return 'ERROR: Divided by zero.'
