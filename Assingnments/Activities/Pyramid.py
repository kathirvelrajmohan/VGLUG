n = int(input("Enter the Number: "))
spaces = n-1
s="A"
for i in range(0,n):
    for j in range(0,spaces):
        print(" ",end="")
    if(i == 0):
        print(s,end="")
    else:
        c = chr(ord(s[-1])+1)
        print(s,end="")
        print(c,end="")
        print(s[::-1],end="")
        s+=c
    for j in range(0,spaces):
        print(" ",end="")
    spaces-=1
    print()