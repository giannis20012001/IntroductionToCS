type = input("Input the building block style to use? (e.g., *, x, etc.) : ")
temp = input("Input the number of rows? (e.g., 2, 4, etc.) : ")
n = int(temp)

# outer loop to handle number of rows
# n in this case
for i in range(0, n):

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # printing stars
        print(type + " ", end="")

        # ending line after each row
    print("\r")