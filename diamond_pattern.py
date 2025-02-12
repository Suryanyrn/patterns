n = int(input("Enter number of rows: "))
num = 1

# Upper pyramid
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()

# Lower pyramid
num -= n
for i in range(n - 1, 0, -1):
    num -= i
    print(" " * (n - i), end="")
    temp = num
    for j in range(i):
        print(temp, end=" ")
        temp += 1
    print()
