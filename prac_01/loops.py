for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print a number of stars.
number_of_stars = int(input("Choose an integer: "))
for i in range(number_of_stars):
    print('*', end='')
print()

# d. print lines of increasing stars. Prints one line at a time in inner loop, increasing the number of stars printed
# depending on the outer lip.
number_of_stars = int(input("Choose an integer: "))
# for i in range(number_of_stars):
#     for n in range(i + 1):
#         print('*', end='')
#     print()
# The above was my original idea, but then I realised you could multiply the characters you print. It is very
# inefficient to have loops or statements nested in each other, and you should always question your code if they are.
for i in range(1, number_of_stars + 1):
    print('*' * i)
