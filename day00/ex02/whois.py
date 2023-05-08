import sys

len_arg = len(sys.argv)

if len_arg > 2:
    print("AssertionError: more than one argument are provided")
elif len_arg > 1:
    if sys.argv[1].isnumeric():
        # is odd
        if int(sys.argv[1]) == 0:
            print("I'm Zero.")
        elif int(sys.argv[1]) % 2 == 1:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    else:
        print("AssertionError: argument is not an integer")
else:
    print("AssertionError: No argument was provided")