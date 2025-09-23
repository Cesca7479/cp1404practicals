"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
"""
x = int(input("Input a number for x: "))
y = int(input("Input a number for y: "))
print(" 1. Show the even numbers from x to y \n "
      "2. Show the odd numbers from x to y \n "
      "3. Show the squares of the numbers from x to y (e.g, if x, y = 2, 4 then: 4 9 16) \n "
      "4. Exit the program")
choice = int(input(">>> "))
range_between = y - x + 1
while choice != 4:
    if choice == 1:
        for i in range(range_between):
            if (x + i) % 2 == 0:
                print(x + i, end=' ')
    elif choice == 2:
        for i in range(range_between):
            if (x + i) % 2 == 1:
                print(x + i, end=' ')
    elif choice == 3:
        for i in range(range_between):
            square = (x + i) ** 2
            print(square, end=' ')
    else:
        print("Invalid input")
    print()
    print(" 1. Show the even numbers from x to y \n "
          "2. Show the odd numbers from x to y \n "
          "3. Show the squares of the numbers from x to y (e.g, if x, y = 2, 4 then: 4 9 16) \n "
          "4. Exit the program")
    choice = int(input(">>> "))
print("Goodbye.")
