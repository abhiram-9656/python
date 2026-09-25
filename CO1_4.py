#count the ocurrences of each word in aline of test
text=input("enter the line of text:")
words=text.split()
for word in set(words):
    print(word,":",words.count(word))
