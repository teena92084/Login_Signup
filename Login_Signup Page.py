import json
import re
import os
file_exist=os.path.exists("userdetail.json")
print(file_exist)
if file_exist==False:
    dic1={}
    list3=[]
    user=input("signup or login:-")
    if user=="signup":
        name=input("enter user name")
        print("your password length should be between 8-18")
        pas=input("creat a strong password")
        if len(pas)>=5 and len(pas)<=18:
            if re.search("[a-z]",pas) and re.search("[A-Z]",pas) and re.search("[0-9]",pas) and re.search("[@#$%&]",pas):
                pas2=input("confirm password")
                if pas==pas2:
                    print("congrats ",name,"you have succesfully signup")
                    dob=input("enter your date of birth in form of - 00/00/1900__  ")
                    descr=input("description  ")
                    hobbies=input("hobbies  ")
                    gender=input("gender  male of female   ")
                    dic1={}
                    print("congrats ",name,"you have succesfully signup")
                    list1=["name","pas2","dob","descr","hobbies","gender"]
                    list2=[name,pas2,dob,descr,hobbies,gender]
                    i=0
                    while i <len(list2):
                        dic1.update({list1[i]:list2[i]})
                        i+=1
                    dic2={}
                    list4=[]
                    list4.append(dic1)
                    dic2.update({pas:list4})
                    with open("userdetail.json","w") as h:
                        json.dump(dic2,h,indent=3)
                else:
                    print("both password are not same")
            else:
                print("your password is not strong,try again") 
elif file_exist==True:
        list3=[]
        user=input("signup or login:-")
        if user=="signup":
            name=input("enter user name")
            print("your password length should be between 8-18")
            pas=input("creat a strong password")
            with open("userdetail.json","r") as f:
                data=json.load(f)
            if len(pas)>=6 and len(pas)<=18:
                if re.search("[a-z]",pas) and re.search("[A-Z]",pas) and re.search("[0-9]",pas) and re.search("[@#$%&]",pas):
                    pas2=input("confirm password")
                    if pas==pas2:
                        print("congrats ",name,"you have succesfully signup")
                        dob=input("enter your date of birth in form of - 00/00/1900__  ")
                        descr=input("description  ")
                        hobbies=input("hobbies  ")
                        gender=input("gender  male of female   ")
                        print("congrats ",name,"you have succesfully signup")
                        list1=["name","pas2","dob","descr","hobbies","gender"]
                        list2=[name,pas2,dob,descr,hobbies,gender]
                        i=0
                        dic1={}
                        while i <len(list2):
                            dic1.update({list1[i]:list2[i]})
                            i+=1
                        list4=[]
                        list4.append(dic1)
                        data.update({pas:list4})
                        with open("userdetail.json","w") as h:
                            json.dump(data,h,indent=4)
                    else:
                        print("both password are not same")
                else:
                    print("your password is not strong,try again") 
        elif user=="login":
            user_name=input("enter user name")
            password=input("enter password")
            with open("userdetail.json","r") as f:
                data=json.load(f)
            for i in data:
                if i==password:
                    print("user is true")
                    print(data[i])
                # else:
                #     print("sorry your password is wrong")
       




















# from tkinter import*
# from tkinter.ttk import Combobox
# from tkinter.messagebox import*
# import datetime

# from playsound import playsound

# root=Tk()
# Clocking=PhotoImage(file="/home/chhaya/alarmclock.png")
# img=Label(root,image=Clocking)
# img.grid(rowspan=12,column=0)
# def alarm():
#     h=int(c.get())
#     m=int(c1.get())
    
#     showinfo("alarm notication","alarm has been set")
#     print(datetime.datetime.now())
#     while True:
#         if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
#             # for j in range(2):
#                 # playsound('https://musikringtone.com//downloads//5845//')
#                 playsound("https://bestringtones.net//music/download.html?id=14480")
#                 break
# root.title(" my alaram clock")

# l1=Label(root,text="set alarm hour")
# l1.grid(row=0,column=0)
# hour=list(range(1,25))
# c=Combobox(root,values=hour)
# c.grid(row=0,column=10)
 

# l2=Label(root,text="set alarm minute")
# l2.grid(row=1,column=0)
# minute=list(range(1,61))
# c1=Combobox(root,values=minute)
# c1.grid(row=1,column=10 )


# btn=Button(root,text="set alarm",command=alarm)
# btn.grid(row=2,column=2)
# root.mainloop()

                
        
                

