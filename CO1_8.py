#get a string from an input string where all occurence of first character replaced with "$",except first character

word = input("Enter a string: ")
result = '$' + word[1:]
print(result)
