n=int(input("Enter the Number to print the pattern:"))
l=[x for x in range(1,n+1)]
for i in range(n):
             print(l)
             l.append(l[0])
             l.pop(0)
