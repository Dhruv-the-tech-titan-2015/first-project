from threading import Timer
import json
import  time
lst=[]
inc=0
def dog(sub):

 def happy():
    print("sorry now you cant give your attendence")
 def dm():
    global inc
    inc=inc+1
    print("\n","times up press two times enter for saving the attendance")
 def pm():
    global inc
    inc=0
 timt=30
 t=Timer(timt,dm)
 t.start()
 z=True

 while z:

  with open(sub, "r") as o:
        att = json.load(o)
  print(att)
  att_incrementer = 1
  name=input("\ninput name=")
  id=input("\nenter the id=")
  for i in att:
        for key,value in i.items():
            if key==name and value[0]==id:
                value[1]+=att_incrementer
        with open(sub, "w") as o:
            json.dump(att, o)
  if inc == 1:#dont know why i am using this 1
     break
  print(lst)
 t.cancel()
 pm()
 happy()
 return 1
