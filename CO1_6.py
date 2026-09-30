# store a list  of first name .count the occurence of  'a' within the list
name = input("enter  the numbers:").split()
count = 0
for name in name:
      count = count + name.lower().count("a")
print("number of a:",count)

