n=5
a=""
for i in range(n):
             a=a+str(i+1)
for j in range(n):
             print(" 0 "*(n-j-1),a[j:j+1]," 0 "*j)
