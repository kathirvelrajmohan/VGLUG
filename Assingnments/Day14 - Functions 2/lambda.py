#lambda function for providing the cube of the Given number

val = lambda x:x*x if x<=5 else x*x*x
print("Enter the number to print cube if the value is greater than 5 or else it prints cube")
print(val(int(input("Enter the value: "))))