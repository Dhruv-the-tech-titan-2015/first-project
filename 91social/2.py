a="20210114"#date 1
b="20220121"#date 2
r1=int(a[:4])
r2=int(b[:4])
leap=0
for i in range(r1,r2):
 if i%4==0:#this logic is for leap year between the dates
  leap+=1
year=int(b[:4])-int(a[:4])#calculating years
month=int(b[4:6])-int(a[4:6])#calculating months
date=int(b[6:])-int(a[6:])#calculating Date
total_days=year*365+month*30+date#converting into days
print(total_days+leap)#adding leap years with years for getting total number of days