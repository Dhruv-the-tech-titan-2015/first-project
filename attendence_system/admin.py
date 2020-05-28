from datetime import datetime,timedelta
from studentattendence import *
from signal import *
admin_id="Allow"
password=0000
welcome=1
sub_lst=[]
time_lst=[]

def coordinator():
 a=input("enter the admin id=")
 pwd=int(input("enter the password="))
 if(admin_id==a and pwd==password):
     return 1
 else:
     print("Authentication failed!")
def student_db():
    db=[]
    with open("student_database.json", "r") as obj:
      db=json.load(obj)
    std_attendence=0
    ctrl=True
    db_choice=input("do u want to add students press y else n=")
    if db_choice=='y':
        while ctrl:
            std_record = {}
            link_values = []
            std_name=input("enter the student name=")
            std_id=input("enter the student id=")
            link_values.append(std_id)
            std_record[std_name]=link_values
            db.append(std_record)
            with open("student_database.json","w") as obj:
                json.dump(db,obj)
            more_std=input("do u want to add more student press y else n=")
            if more_std=='n':
                ctrl=False






def timetable():
    with open('timetable_subject.json', 'r') as obj:
        sub_lst = json.load(obj)
    with open('timetable_time.json', 'r') as obj:
        time_lst = json.load(obj)
    del sub_lst[:]
    del time_lst[:]
    with open('timetable_subject.json', 'w') as obj:
        json.dump(sub_lst,obj)
    with open('timetable_time.json', 'w') as obj:
        json.dump(time_lst,obj)
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

    with open("timetable_time.json", 'w') as obj:
        json.dump(time_lst, obj)
    with open("timetable_subject.json", 'w') as obj:
        json.dump(sub_lst, obj)
    return sub_lst,time_lst

#subject=time1=timetable()
#print(subject[0])
#print(time1[1])
def subject1():
 try:
  with open("timetable_subject.json","r") as o:
     sub_lst=json.load(o)
  with open("timetable_time.json","r") as o:
     time_lst=json.load(o)

  if(sub_lst[0] and time_lst[0]):
      print("This lecture is of"+sub_lst[0])
      sub = sub_lst[0] + ".json"
      dog(sub)
 except:
     print("error in subject 1")
def subject2():
  try:
      with open("timetable_subject.json", "r") as o:
          sub_lst = json.load(o)
      with open("timetable_time.json", "r") as o:
          time_lst = json.load(o)
      if(sub_lst[1]):
          print("This lecture is of" + sub_lst[1])
          sub = sub_lst[1] + ".json"
          dog(sub)


  except:
     print("error in subject2")
def subject3():

 try:
  with open("timetable_subject.json", "r") as o:
         sub_lst = json.load(o)
  with open("timetable_time.json", "r") as o:
         time_lst = json.load(o)
  if(sub_lst[2]):
      sub = sub_lst[2] + ".json"
      dog(sub)


 except:
    pass
def subject4():

 try:

  if(sub_lst[3]):
   print("this lecture is of",sub_lst[3])

 except:
     pass
def subject5():
 try:
  if(sub_lst[4]):
   print("this lecture is of",sub_lst[4])
   time.sleep(1)
 except:
    pass

def subject6():
     try:
         if (sub_lst[5]):
             print("this lecture is of", sub_lst[5])
             time.sleep(1)
     except:
         pass
def subject7():
 try:
  if(sub_lst[6]):
   print("this lecture is of",sub_lst[6])
   time.sleep(1)
 except:
    pass

def subject8():
     try:
         if (sub_lst[7]):
             print("this lecture is of", sub_lst[7])
             time.sleep(1)
     except:
         pass
def subject9():
 try:
  if(sub_lst[8]):
   print("this lecture is of",sub_lst[8])
   time.sleep(1)
 except:
    pass
def subject10():
 try:
  if(sub_lst[9]):
   print("this lecture is of",sub_lst[9])
   time.sleep(1)
 except:
    pass