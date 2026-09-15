#accept a list of words and return the length of the longest word
li=[]
limit=int(input("Enter the limit: "))
for i in range(limit):
    word=input("Enter a word: ")
    li.append(word)
print(li)
length=0
longword=""
for i in li:
    if len(i)>length:
        length=len(i)
        longword=i
print(longword)
print(length)