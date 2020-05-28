import json
def student_attendence(subject):
  increment=1
  subject=subject+".json"
  with open(subject,"r") as obj:
    attendence=json.load(obj)

  ex=input("enter your name=")
  ex1=input("enter your id=")
  for i in attendence:
    for key,value in i.items():
        if ex==key and ex1==value[0]:

            try:
             if value[1]:

                value[1] += increment
                print("Authentication Successful!!!")

            except:
                    value.append(increment)


            with open(subject,"w") as obj:
              json.dump(attendence,obj)
#student_attendence()
def student_attendencek(subject):
  increment=1
  subject=subject+".json"
  with open("student_database.json","r") as obj:
    attendence=json.load(obj)

  ex=input("enter your name=")
  ex1=input("enter your id=")
  for i in attendence:
    for key,value in i.items():
        if ex==key and ex1==value[0]:

            try:
             if value[1]:

                value[1] += increment
                print("Authentication Successful!!!")

            except:
                    value.append(increment)


            with open(subject,"w") as obj:
               json.dump(attendence,obj)