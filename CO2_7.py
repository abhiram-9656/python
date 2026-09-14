#add'ing' at the end of a given string if it is already end with 'ing' then add 'ly'
string = input("Enter a string: ")
length=len(string)
if length>=2:
    if string[-3:]=='ing':
        string+= "ly"
        else:
        string+="ing"
        print("the string =>",string)
    else:
        print("the string is too short")
