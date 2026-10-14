#print out all color from color-list not contined in color-list2

list1 = input("enter color-list1: ").split(',')
list2 = input("enter color-list2: ").split(',')

result = [x for x in list1 if x not in list2]
print(result) 

