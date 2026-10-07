#get a string from an input string where all occurence of first character replaced with "$",except first character

word = input("Enter a string: ")
first = word[0]
result = first + word[1:].replace(first, '$')
print(result)
