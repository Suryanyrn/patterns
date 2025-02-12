n = int(input("Enter number of rows (odd): "))
num = 1

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(num, end=" ")
            num += 1
        else:
            print(" ", end=" ")
    print()
