# accept a file name from user and print extension of that
filename = input("enter file:")
extension = filename.split('.')[-1]
print("extension:",extension)