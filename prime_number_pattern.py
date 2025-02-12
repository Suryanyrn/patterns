def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter number of rows: "))
prime_list = []
num = 2  

# Collect required prime numbers
while len(prime_list) < (n * (n + 1)) // 2:
    if is_prime(num):
        prime_list.append(num)
    num += 1

index = 0
for i in range(1, n + 1):
    for j in range(i):
        print(prime_list[index], end=" ")
        index += 1
    print()
