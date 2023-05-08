import sys

if len(sys.argv) == 0:
    print('Usage: python operations.py <number1> <number2>')
if len(sys.argv) != 3:
    print('AssertionError: Exactly two arguments are required')
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print('Sum:         ' + str(a + b))
        print('Difference:  ' + str(abs(a - b)))
        print('Product:     ' + str(a * b))
        if b == 0:
            print('Quotient:    ERROR (division by zero)')
            print('Remainder:   ERROR (modulo by zero)')
        else:
            print('Quotient:    ' + str(a / b))
            print('Remainder:   ' + str(a % b))
    except ValueError:
        print('AssertionError: Only integers')
