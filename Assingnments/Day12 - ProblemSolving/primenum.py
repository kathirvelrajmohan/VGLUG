print("Prime numbers between the given numbers")
num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the number 2: "))

if (num1>num2):
	y = num1
	x = num2
else:
	x = num1
	y = num2
for num in range(x,y+1):
	limit = num//2
	count = 2
	for i in range(2,limit+1):
		if num%i == 0:
			break
		else:
			count+=1
	count-=1
	if count == limit:
		print(num)
