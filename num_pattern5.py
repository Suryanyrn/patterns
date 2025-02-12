n = int(input("Enter number of rows: "))
num = 1

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()
