d = {}
print("Dictionary Operations")
print("""Enter 1 for Add the elements
Enter 2 for edit the elements
Enter 3 for delete the elements
Enter 4 for Printing the values
Enter 5 for Exit""")
a = int(input("Enter Your option: "))
while a!= 5:
    if a == 1:
        print("-----Add new Elements in Dictionary-----")
        x = input("Enter the Key: ")
        y = input("Enter the Value: ")
        d[x] = y
    if a == 2:
        print("-----Edit the elements in dictionary-----")
        x = input("Enter the Key that you want to edit: ")
        y = input("Enter the new value for the key: ")
        d[x] = y
    if a == 3:
        print("-----Delete the elements in dictionary-----")
        x = input("Enter the key you want to delete: ")
        del d[x]
        print("The ",x," key is deleted from the dictionary")
    if a == 4:
        print("-----Printing the elements from dictionary-----")
        print(d)
    print(" ")
    a = int(input("Enter your another option: "))
print("Thank You")
