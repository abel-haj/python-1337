# The kata variable is always a tuple that contains 5 non-negative integers. The first
# integer contains up to 4 digits, the rest up to 2 digits.

#        0    1  2   3  4
kata = (2019, 9, 25, 3, 30)

# # GPT
# print('{:02}/{:02}/{} {:02}:{:02}'.format(kata[1], kata[2], kata[0], kata[3], kata[4]))


# ME :)
date_str = ''
date_str += str(kata[1]).zfill(2) + '/'
date_str += str(kata[2]).zfill(2) + '/'
date_str += str(kata[0]) + ' '
date_str += str(kata[3]).zfill(2) + ':'
date_str += str(kata[4]).zfill(2)
print(date_str)