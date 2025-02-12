n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * i, end="")
    for j in range(i + 1, n + 1):
        print(j, end=" ")
    print()
