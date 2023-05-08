# The kata variable is always a string whose length is not higher than 42.

kata = "The right format"

# # GPT
print('{:->42}'.format(2), end='')

# # ME :)
# for i in range(42 - len(kata)): print('-', end='')
# print(kata, end='')