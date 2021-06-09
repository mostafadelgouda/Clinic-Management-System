import re
#Validation==============================================================
def stringOk(s):
    a=re.search(r"[A-z\ ]+",s)
    if a:
        if a.group() == s: return True
    return False
def intOk(x):
    a=re.search(r"[0-9]+",x)
    if a:
        if a.group() == x: return True
    return False
def mailOk(x):
    a=re.search(r"[A-z][A-z0-9\.\_\-]+@[A-z]+\.com",x)
    if a:
        if a.group() == x: return True
    return False

#Add======================================================================
def addPatient():
    f=open("data.txt",'a')
    idi=input("Enter your ID ")
    while not intOk(idi):
        print("ID Not Valid")
        idi=input("Enter your ID again ")
    
    name=input("Enter your Name ")
    while not stringOk(name):
        print("Name Not Valid")
        name=input("Enter your Name again ")
        
    phone=input("Enter your Phone Number ")
    while not intOk(phone):
        print("phone Not Valid")
        phone=input("Enter your Phone Number again ")
        
    age=input("Your Age ")
    while not intOk(age):
        print("age Not Valid")
        age=input("Your Age again ")
        
    mail=input("Your Mail ")
    while not mailOk(mail):
        print("Mail Not Valid")
        mail=input("Your Mail again ")
        
    gender=input("Your Gender ")
    while not stringOk(gender):
        print("Gender Not Valid")
        gender=input("Your Gender again ")
    
    f.write(idi+"/"+name+"/"+age+"/"+phone+"/"+mail+"/"+gender+"\n")
    f.close()
    
#search======================================================================
def searchPatient():
    f=open("data.txt",'r')
    idi=input("Enter your ID ")
    for line in f:
        id,name,age,phone,mail,gender=line.split('/')
        if idi==id:
            print("Name: "+name+", Age: "+age+", Phone: "+phone+", mail: "+mail+", Gender: "+gender)
            break
    else:print("Not found")
    f.close()
    
#Display======================================================================
def Dis():
    f=open("data.txt",'r')
    flag=False
    for line in f:
        flag=True
        id,name,age,phone,mail,gender=line.split('/')
        print("Name: "+name+", Age: "+age+", Phone: "+phone+", mail: "+mail+", Gender: "+gender)
    f.close()
    if not flag:
        print("There is no patients to show")

#Deletion======================================================================
def delPatient():
    idi=input("Enter Patient ID ")
    f=open("data.txt",'r')
    li=[]
    for line in f:
        li.append(line)
    f.close()
    flag = False
    ff=open("data.txt",'w')
    for line in li:
        id,name,age,phone,mail,gender=line.split('/')
        if id==idi:
            flag=True
        if id!=idi:
            ff.write(line)
    ff.close()
    if not flag:
        print("Not found")
    else:
        print("operation is done successfully")
#Modification======================================================================
def editPatient():
    idi=input("Enter Patient ID ")
    f=open("data.txt",'r')
    li=[]
    flag=False
    for line in f:
        li.append(line)
    f.close()
    ff=open("data.txt",'w')
    for line in li:
        id,name,age,phone,mail,gender=line.split('/')
        if id!=idi:
            #print(line,line)
            ff.write(line)
        else:
            #f=open("data.txt",'a')
            flag=True
            idi=input("Enter your ID ")
            while not intOk(idi):
                print("ID Not Valid")
                idi=input("Enter your ID again ")
    
            name=input("Enter your Name ")
            while not stringOk(name):
                print("Name Not Valid")
                name=input("Enter your Name again ")
        
            phone=input("Enter your Phone Number ")
            while not intOk(phone):
                print("phone Not Valid")
                phone=input("Enter your Phone Number again ")
        
            age=input("Your Age ")
            while not intOk(age):
                print("age Not Valid")
                age=input("Your Age again ")
        
            mail=input("Your Mail ")
            while not mailOk(mail):
                print("Mail Not Valid")
                mail=input("Your Mail again ")
        
            gender=input("Your Gender ")
            while not stringOk(gender):
                print("Gender Not Valid")
                gender=input("Your Gender again ")
            ff.write(idi+"/"+name+"/"+age+"/"+phone+"/"+mail+"/"+gender+"\n")
    ff.close()
    if not flag:print("Not Found")

#Main======================================================================

#print("Welcome to our program")
while True:
    print("Choose the process you want")
    print("Add new patient => 1")
    print("Delete patient => 2")
    print("Search for patient => 3")
    print("Edit patient information => 4")
    print("Display all information => 5")
    print("Exit => 0")
    ch = int(input())
    if ch==1:
        addPatient()
    elif ch==2:
        delPatient()
    elif ch==3:
        searchPatient()
    elif ch==4:
        editPatient()
    elif ch==5:
        Dis()
    else:
        break

    

    