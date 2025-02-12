n = int(input("Enter number of rows: "))

for i in range(n):
    a, b = 1, 1  
    for j in range(i + 1):
        print(a, end=" ")
        a, b = b, a + b  
    print()
