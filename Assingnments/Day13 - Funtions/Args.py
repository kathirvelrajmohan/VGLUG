def countEven(*numbers):
    even = 0
    for i in numbers:
        if i % 2 == 0:
            even+=1
        
    return even
print("Enter the space seperated values: ")
numbers = input()
numberlist = list(map(int,numbers.split()))
a = countEven(*numberlist)
print("The count of the even numbers: "+str(a))
            