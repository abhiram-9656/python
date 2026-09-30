# promt the user for a list of integers .for all value greater than 100,store'100'insted
numbers = list(map(int,input("enter integer:").split()))
for i in range(len(numbers)):
  if numbers[i]>100:
     numbers[i]="over"
print(numbers)
