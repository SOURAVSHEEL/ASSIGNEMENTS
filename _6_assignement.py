size = int(input("Enter the size of list: "))
lst = []
for i in range(size):
    elements = int(input("Enter the element of the list: "))
    lst.append(elements)

def sumlist(lst):
    sum=0
    for i in range(len(lst)):
        sum = sum+lst[i]
    return sum
    
print(lst)
print("sum of list: ",sumlist(lst))

