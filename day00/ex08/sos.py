import sys

morseCodes = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/',
}

def morse_encode(string):
    for c in string:
        if c.upper() not in morseCodes:
            return print('ERROR')
    for c in string:
        print(morseCodes[c.upper()], end=' ')
    print('')

# If more than one argument are provided, merge them into a single string with each
if __name__ == "__main__":
    if len(sys.argv) > 1:
        morse_encode(' '.join(sys.argv[1:]))
