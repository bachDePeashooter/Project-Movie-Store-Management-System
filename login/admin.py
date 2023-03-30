from time import *
from .client import Clients
from .ship import Shipper

class Admins :
    def __init__(self) -> None:
        pass

    def newAdmin(self): #create a new admin
        print("\nWelcome to our Movies Store Management\n")
        
        #last name
        while True :
            lastname=str(input("The last name of the new admin : "))
            if len(lastname)!=0:
                break
            else:
                print("Error, invalid last name \n")

        #First name
        while True :
            firstname=str(input("The first name of the new admin: "))
            if len(firstname)!=0:
                break
            else:
                print("Error, invalid first name\n")
        #dob
        while True:
            dob=(input("\nThe date of birth with this format 'dd/mm/yyyy' of the new admin : "))
            if len(dob)==10:
                if dob[2]!="/" or dob[5]!="/":
                    print("Error, invalid format \n")
                elif dob[0].isnumeric()!=True or dob[1].isnumeric()!=True:
                    print("Error, invalid day format \n")
                elif dob[3].isnumeric()!=True or dob[4].isnumeric()!=True:
                    print("Error, invalid mounth format\n")
                elif (dob[6].isnumeric()!=True) or (dob[7].isnumeric()!=True) or (dob[8].isnumeric()!=True) or (dob[9].isnumeric()!=True):
                    print("Error, invalid year format\n")
                else:
                    break

        #delivery address
        address=str(input("\nThe address of the new admin : "))
        
        #password
        password=str(input("\nThe password of the new admin : "))
        
        #Salary
        while True:
            try:
                salary=int(input("\nEnter the salary of the new admin (in $) : "))
                if salary>=0:
                    break
            except ValueError:
                print("This is not a number")
        
        #email
        while True:
            email=str(input("\nThe email address of the new admin : "))
            if ("@" in email) and ("." in email):
                break
            else:
                print("\nError, invalid Format")
                
        #check if this account already exist with this email
        list=[lastname,firstname,dob,address,password,email,str(salary)]
        fileAdmins= open ("Admins.txt","r") 
        nbAdmins=len(fileAdmins.readlines()) 
        fileAdmins= open ("Admins.txt","r")  
        tab=fileAdmins.readline()
        a=0
        while nbAdmins!=0:
            file=tab.split(",")
            tab=fileAdmins.readline()
            if file[0]==list[0]:
                a+=1
            nbAdmins-=1
        fileAdmins.close()
        
        #add admin on .txt
        if a==0:
            with  open ("Admins.txt","a") as fileAdmins:
                list=[lastname,firstname,dob,address,password,email,str(salary)]
                for word in list:
                    fileAdmins.write(str(word)+",")
                fileAdmins.write("\n")
                fileAdmins.close()

    def LoginAdmins(self):
        while True:
       
            fichier=open("Admins.txt","r",encoding='utf-8')  #number of admin
            nbAdmin=len(fichier.readlines())
            nbadmin=nbAdmin
            
            fichier=open("Admins.txt","r",encoding='utf-8') #get the information out of the .txt
            listEmail=[]
            listPassword=[]
            listFirstname=[]
            listlastname=[]
            tab=fichier.readline()
            while nbAdmin!=0:
                list=tab.split(",")
                listFirstname.append(list[0])
                listlastname.append(list[1])
                listEmail.append(list[5])
                listPassword.append(list[4])
                tab=fichier.readline()
                nbAdmin-=1

            email=str(input("\nenter your email address: ")) #ask email and password
            password=str(input("\nenter your password : "))
            print("\nsearching for your account...")
            sleep(1)
            i=0
            y=1
           
            while i<nbadmin: #check if email and password (3 tries) are corrects
                if email==listEmail[i]:
                    print("\nEmail correct")
                    if password==listPassword[i]:
                        sleep(0.5)
                        print("\npassword correct")
                        firstname=listFirstname[i]
                        lastname=listlastname[i]
                        break
                    else:
                        print("\ninvalid password, 2 trials left")
                        password=str(input("\nenter your password : "))
                        if password==listPassword[i]:
                            sleep(0.5)
                            print("\npassword correct")
                            firstname=listFirstname[i]
                            lastname=listlastname[i]
                            break
                        else:
                            print("\ninvalid password, 1 trials left")
                            password=str(input("\nenter your password : "))
                            if password==listPassword[i]:
                                sleep(0.5)
                                print("\npassword correct")
                                firstname=listFirstname[i]
                                lastname=listlastname[i]
                                break
                            else:
                                print("\ninvalid password, disconnecting...")
                                exit()
                else:
                    i+=1

            if i==nbadmin:
                print("\nSorry, no account exists with this email address")
                connection=int(input("\n1) try to connect again \n2) exit \n "))
                if connection== 2:
                    print("\nclosing in progress...")
                    exit()
                elif connection!=2 or connection!=1:
                    print("\nerror, closing in progress...")
                    break
            else:
                print("\nWelcome",firstname,lastname,)
                break
    
    def Informations(self):
        test=0
        while True:
            email=str(input("\nTo access to the information, please enter the email address of this account here  : "))
            if ("@" in email) and ("." in email):
                break
            else:
                print("\nFormat Error")
                
        fileAdmins= open ("Clients.txt","r") 
        nbAdmins=len(fileAdmins.readlines()) 
        fileAdmins= open ("Clients.txt","r")  
        tab=fileAdmins.readline()
        while nbAdmins!=0:
            file=tab.split(",")
            tab=fileAdmins.readline()
            if file[5]==email:
                test+=1
                print("\nHere is all of the informations : ", "\nLastname : ",file[0], "\nFirstname : ",file[1], "\nDate of birth : ",file[2], "\nAddress : ",file[3], "\nPassword : ","******", "\nEmail Address : ",file[5], "\nSalary : ",file[6])
                sleep(3)
                             
            nbAdmins-=1
        fileAdmins.close()
        if test==0:
            print("Sorry, no account was found with this email address")
            
    def VerifyAccount(self):
        while True:
            while True:
                try:
                    who=int(input("\nWhich accounts do you want to see? : \n1)Clients Account \n2)Shipper Account \n3)Admin Account \n4)Back \n"))
                    if who==1 or who==2 or who==3 or who==4 or who==5:
                        break
                    else:
                        print("\nError, Please select 1, 2, 3 or 4")
                except ValueError:
                    print("\nThis is not a number")
            if who==1:
                print("\nThese are all the email addresses of existing clients accounts : ")
                file=open("Clients.txt","r",encoding='utf-8')
                nb=len(file.readlines())
                file=open("Clients.txt","r",encoding='utf-8')
                tab=file.readline()
                email=[]
                while nb!=0:
                    list=tab.split(",")
                    email.append(list[5])
                    tab=file.readline()
                    nb-=1
                for i in email:
                    print(i)
                Clients().Informations()
            if who==2:
                print("\nThese are all the email addresses of existing shipper accounts : ")
                file=open("Shipper.txt","r",encoding='utf-8')
                nb=len(file.readlines())
                file=open("Shipper.txt","r",encoding='utf-8')
                tab=file.readline()
                email=[]
                while nb!=0:
                    list=tab.split(",")
                    email.append(list[5])
                    tab=file.readline()
                    nb-=1
                for i in email:
                    print(i)
                Shipper().Informations()
            if who==3:
                print("\nThese are all the email addresses of existing admin accounts : ")
                file=open("Admins.txt","r",encoding='utf-8')
                nb=len(file.readlines())
                file=open("Admins.txt","r",encoding='utf-8')
                tab=file.readline()
                email=[]
                while nb!=0:
                    list=tab.split(",")
                    email.append(list[5])
                    tab=file.readline()
                    nb-=1
                for i in email:
                    print(i)
                Admins().Informations()
            if who==4:
                break