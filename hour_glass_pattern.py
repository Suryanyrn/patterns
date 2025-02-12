n = int(input("Enter number of rows: "))

# Upper half
for i in range(n):
    print(" " * i, end="")
    for j in range(i + 1, n + 1):
        print(j, end=" ")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    print(" " * i, end="")
    for j in range(i + 1, n + 1):
        print(j, end=" ")
    print()
