
# • Punctuation symbols must be removed from the printed list: they are neither part of a word nor a separator
# • The program must contains at least one list comprehension expression.

import sys

if len (sys.argv) == 3:
    # Make a program that takes a string S and an integer N as argument
    S = ''.join([l for l in sys.argv[1] if l.isalnum() or l.isspace()])
    N = sys.argv[2]

    if len(S) > 1 and N.isnumeric():
        N = int(N)
        # • Words are separated from each other by space characters
        word_list = S.split(' ')
        # and print the list of words in S that contains more than N non-punctuation characters.
        print([word for word in word_list if len(word) > N])

    # if the type of any argument is wrong
    else:
        print('ERROR')

# If the number of argument is different from 2
else:

    # the program prints an error message
    print('ERROR')
