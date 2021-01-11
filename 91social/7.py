import datetime
k=open("E:/test.log")#file whose content to be copied
#print(k.read())
t=open("E:/dup.txt","w")#file in which the content to be write
t.write('logs Recorded at: %s\n' %datetime.datetime.now())#printing date and time as suffix
for i in k:
   t.write(i)#writing file
t.close()