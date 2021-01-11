"""this answer includes a file test.log for generating
 random logs after execution it will generate files each of 2 mb
  size so don't run it for long time """

import os
p=1
while True:
  a=str(p)+".txt"#logic for creating new file as the limit exceeded
  o = open(a, "a")
  file_size = 0
  while True:#this loop will run untill a file size doesn't reach the 2mb size
    k = open("test.log", "r")
    o = open(a, "a")
    for j in k:
         o.write(j)
    file_size = os.path.getsize(a)#for getting file size
    print(file_size)
    if file_size>=2097152:#for checking file size
        break
  p+=1
