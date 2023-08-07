#provide fibanacci series using recursive function
def fib(n,x=0,y=1):
    if(n == 1):
        return str(x)
    else:
        n-=1
        temp = x+y
        return str(x) + " "+ fib(n,x=y,y=temp)
print("-----Fibonaaci series using recursive-----")
n = int(input("Enter the number of outcomes in fibannaci series: "))
print(fib(n))