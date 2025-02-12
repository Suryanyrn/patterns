n=5
a=""
for i in range(n):
             a=a+str(n-i)
for j in range(n):
             print(" "*(n-j-1),a[(-j-1):])
