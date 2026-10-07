# create a string from given string where first and last character exchanged [eg:python-nythop]


word = input("enter a string: ")
if  len(word) > 1 :
    result = word[-1] + word[1:-1] + word [0]	
else:
     result = word
print(result)
