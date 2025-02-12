n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print(j + 1, end=" ")
        else:
            print(" ", end=" ")
    print()
