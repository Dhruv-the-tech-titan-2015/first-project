sub_lst=[]
time_lst=[]
def timetable():
    num_of_sub =int(input("enter the number of subjects="))
    b = 0
    while b < num_of_sub:
        print("enter the 1st subject=")
        sub = input()
        sub_lst.append(sub)
        print("enter the time of ", sub, "=")
        time = input()
        time_lst.append(time)
        b+=1
    return sub_lst,time_lst

subject=time1=timetable()
print(subject[0])
print(time1[1])
def subject1():
 try:
  if(subject[0][0] and time1[0][0]):
   print("this lecture is of",subject[0][0])
 except:
     pass
def subject2():
 try:
  if(subject[0][1]):
   print("this lecture is of",subject[0][1])
 except:
     pass
def subject3():
 try:
  if(subject[0][2]):
   print("this lecture is of",subject[0][2])
 except:
    pass
def subject4():
 try:
  if(subject[0][3]):
   print("this lecture is of",subject[0][3])
 except:
     pass
def subject5():
 try:
  if(subject[0][4]):
   print("this lecture is of",subject[0][4])
 except:
    pass

def subject6():
     try:
         if (subject[0][5]):
             print("this lecture is of", subject[0][5])
     except:
         pass
def subject7():
 try:
  if(subject[0][6]):
   print("this lecture is of",subject[0][6])
 except:
    pass

def subject8():
     try:
         if (subject[0][7]):
             print("this lecture is of", subject[0][7])
     except:
         pass
def subject9():
 try:
  if(subject[0][8]):
   print("this lecture is of",subject[0][8])
 except:
    pass
def subject10():
 try:
  if(subject[0][9]):
   print("this lecture is of",subject[0][9])
 except:
    pass