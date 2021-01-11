import subprocess as s
import winapps
a=int(input("press 1 for making ping request and 2 for checking software="))
if a==1:
 ip=input("Enter the ip=")#enter ip address  127.0.0.1 in this format
 if(s.call(["ping",ip])==0):#pinging using subprocess module
    print ("host is up")
 else:
    print ("host is down")
elif a==2:
 p=input("Enter the programe to be search=")#enter the programe name to be search
 for item in winapps.search_installed(p):# searching programe using 3rd party module
    print(item)
else:
    print("wrong choice")