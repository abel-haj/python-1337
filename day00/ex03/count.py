import sys

def text_analyzer(*args):
    """
    This function takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters, punctuation characters and spaces
    """

    txt = ''
    if len(args) == 0:
        txt = input('Provide a text: ')
    else:
        if (type(args[0]) is not str):
            print('AssertionError: argument is not a string')
            return
        txt = args[0]

    print('The text contains ' + str(len(txt)) + ' character(s):')
    print('- ' + str(sum(1 for c in txt if c.isupper())) + ' upper letter(s)')
    print('- ' + str(sum(1 for c in txt if c.islower())) + ' lower letter(s)')
    print('- ' + str(sum(1 for c in txt if not c.isalnum() and not c.isspace())) + ' punctuation mark(s)')
    print('- ' + str(sum(1 for c in txt if c.isspace())) + ' space(s)')

if __name__ == '__main__':
    if(len(sys.argv) > 2):
        print('AssertionError: Too many arguments')
        sys.exit()
    elif(len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
