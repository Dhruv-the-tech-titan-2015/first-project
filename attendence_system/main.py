
import calendar
from admin import *
from datetime import datetime,timedelta
import time
import  schedule
def per_subject_database():#
  with open("timetable_subject.json","r") as ob:
      p=json.load(ob)
  with open("student_database.json","r") as k:
      std=json.load(k)
  for stu in std:
      for key,value in stu.items():
          value.insert(1,0)
  for i in p:
      j=i+".json"
      with open(j,"w") as o:
          json.dump(std,o)
"""def dm():
    end=datetime.now()+timedelta(minutes=10)
    while da   tetime.now()<end:
       a=input("hello=")"""
if(coordinator()):
 student_db()
 print("Do you want to create timetable press y else press n")
 choice=input()
 if choice=='y':
  z=timetable()
  per_subject_database()
 elif choice=='n':
  try:
   with open('timetable_time.json', 'r') as obj:
          time_lst = json.load(obj)

   schedule.every().day.at(time_lst[0]).do(subject1)
   schedule.every().day.at(time_lst[1]).do(subject2)
   schedule.every().day.at(time_lst[2]).do(subject3)
   schedule.every().day.at(time_lst[3]).do(subject4)
   schedule.every().day.at(time_lst[4]).do(subject5)
   schedule.every().day.at(time_lst[5]).do(subject6)
   schedule.every().day.at(time_lst[6]).do(subject7)
   schedule.every().day.at(time_lst[7]).do(subject8)
   schedule.every().day.at(time_lst[8]).do(subject9)
   schedule.every().day.at(time_lst[9]).do(subject10)

  except:
      print("error in calling")

while True:
    schedule.run_pending()
    time.sleep(1)
