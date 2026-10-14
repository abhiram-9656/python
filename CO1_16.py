#creat a single string sperated with space from two strings by swapping the chracter  at position 1

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result1 = str2[0] + str1[1:]
result2 = str1[0] + str2[1:]
print(result1, result2)