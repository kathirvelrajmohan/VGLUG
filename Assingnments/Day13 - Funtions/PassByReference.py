#pass by reference
def add(lst):
    lst.append(5)
    
lst = [1,2,3,4]
print(lst)
add(lst)
print(lst)