from time import *
class Shipper :
    def __init__(self) -> None:
        pass
        
    def newShipper(self): #create a new Shipper
        print("\nWelcome to our Movies Store Management\n")
        
        #last name
        while True :
            lastname=str(input("The last name of the shipper : "))
            if len(lastname)!=0:
                break
            else:
                print("Error, invalid last name \n")

        #First name
        while True :
            firstname=str(input("The first name of the shipper: "))
            if len(firstname)!=0:
                break
            else:
                print("Error, invalid first name\n")
        #dob
        while True:
            dob=(input("\nThe date of birth with this format 'dd/mm/yyyy' of the shipper : "))
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
        address=str(input("\nThe address of the shipper : "))
        
        #password
        password=str(input("\nThe password of the shipper : "))
        
        #email
        while True:
            email=str(input("\nThe email address of the shipper : "))
            if ("@" in email) and ("." in email):
                break
            else:
                print("\nInvalid Format")
                
        #Salary
        while True:
            try:
                salary=int(input("\nEnter the salary of the new shipper (in $) : "))
                if salary>=0:
                    break
            except ValueError:
                print("This is not a number")

        #check if acount already exist with this email
        list=[lastname,firstname,dob,address,password,email]
        fileShipper= open ("Shipper.txt","r") 
        nbShipper=len(fileShipper.readlines()) 
        fileShipper= open ("Shipper.txt","r")  
        tab=fileShipper.readline()
        a=0
        while nbShipper!=0:
            file=tab.split(",")
            tab=fileShipper.readline()
            if file[0]==list[0]:
                a+=1
            nbClients-=1
        fileShipper.close()
        
        #add shipper on .txt
        if a==0:
            with  open ("Shipper.txt","a") as fileShipper:
                list=[lastname,firstname,dob,address,password,email,str(salary)]
                for word in list:
                    fileShipper.write(str(word)+",")
                fileShipper.write("\n")
                fileShipper.close()
        
    def LoginShipper(self):
        
        while True:
       
            fichier=open("Shipper.txt","r",encoding='utf-8')  #number of client
            nbShipper=len(fichier.readlines())
            nbshipper=nbShipper
            
            fichier=open("Shipper.txt","r",encoding='utf-8') #get the information out of the .txt
            listEmail=[]
            listPassword=[]
            listFirstname=[]
            listlastname=[]
            tab=fichier.readline()
            while nbShipper!=0:
                list=tab.split(",")
                listFirstname.append(list[1])
                listlastname.append(list[0])
                listEmail.append(list[5])
                listPassword.append(list[4])
                tab=fichier.readline()
                nbShipper-=1

            email=str(input("\nenter your email address: ")) #ask email and password
            password=str(input("\nenter your password : "))
            print("\nsearching for your account...")
            sleep(1)
            i=0
            y=1
            
            while i<nbshipper: #check if email and password (3 tries) are corrects
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

            if i==nbshipper:
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
            email=str(input("\nTo access to the information, please enter the email address of this account here : "))
            if ("@" in email) and ("." in email):
                break
            else:
                print("\nFormat Error")
                
        fileShipper= open ("Shipper.txt","r") 
        nbShipper=len(fileShipper.readlines()) 
        fileShipper= open ("Shipper.txt","r")  
        tab=fileShipper.readline()
        while nbShipper!=0:
            file=tab.split(",")
            tab=fileShipper.readline()
            if file[5]==email:
                test+=1
                print("\nHere is all of the informations : ", "\nLastname : ",file[0], "\nFirstname : ",file[1], "\nDate of birth : ",file[2], "\nAddress : ",file[3], "\nPassword : ","******", "\nEmail Address : ",file[5], "\nSalary : ",file[6])
                sleep(3)
                             
            nbShipper-=1
        fileShipper.close()
        if test==0:
            print("Sorry, no account was found with this email address")