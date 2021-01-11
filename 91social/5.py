k=open("file path","r")
lst=(k.read().replace(","," ").split())#replacing comma with space for making splitable
print(len(lst))