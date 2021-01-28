# Printing Numbers in Right Triangle Shape
n = int(input("Please enter number of rows to print : "))
for x in range(1, n + 1):
    for j in range(1, x + 1):
        print(j, end="")
    print("")
