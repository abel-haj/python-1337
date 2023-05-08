# kata is always a tuple that contains, in the following order:
#    • 2 non-negative integer containing up to 2 digits
#    • 1 decimal
#    • 1 integer
#    • 1 decimal

kata = (0, 4, 132.42222, 10000, 12345.67)

# ME
print('module_{:02d}, ex_{:02d} : {:.2f}, {:.2e}, {:.2e}'.format(kata[0], kata[1], kata[2], kata[3], kata[4]), end='')