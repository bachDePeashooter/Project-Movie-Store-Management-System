from time import*
import domains
import json

class Admins :
    def __init__(self, MovieList):
        self.__MovieList = MovieList
    def AddMovie(self):
        numberOfMovie = int(input('Enter number of movies u wanna add: '))
        for i in range(numberOfMovie):
            self.inputMovie()
    
    def inputMovie(self):
        id = int(input('ID: '))
        title = str(input('Title of the film: '))
        duration = str(input('Duration: '))
        cost = int(input('Cost: '))
        quantity = int(input('Quantity: '))
        movie = domains.Movie(id,title,duration,cost,quantity)
        self.__saleList.append(movie)
    
    #export list of Movies to file 
    def exportMovie(self):
        with open('Movie.dt') as file:
            json.dump(self.__MovieList, file, default=lambda o: o.__dict__, indent=4 )

    def VerifyAccount(self):
        ()#todo
        
    def AvailableMovie(self):
        ()#todo
        
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
                nbClient-=1

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
    
    
class Clients :
    def Informations(self):
        ()#todo
        
    def Cart(self):
        ()#todo
        
    def SeeMovie(self):
        ()#todo
        
    def newClient(self): #create a new client
        print("\nWelcome to our Movies Store Management\n")
        
        #last name
        while True :
            lastname=str(input("Your last name : "))
            if len(lastname)!=0:
                break
            else:
                print("Error, invalid last name \n")

        #First name
        while True :
            firstname=str(input("Your first name: "))
            if len(firstname)!=0:
                break
            else:
                print("Error, invalid first name\n")
        #dob
        while True:
            dob=(input("\nYour date of birth with this format 'dd/mm/yyyy' : "))
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
        address=str(input("\nYour address : "))
        
        #password
        password=str(input("\nChoose a password : "))
        
        #email
        while True:
            email=str(input("\nyour email address : "))
            if ("@" in email) and ("." in email):
                break
            else:
                print("\nErreur de format")

        #check if acount already exist with this email
        list=[lastname,firstname,dob,address,password,email]
        fileClients= open ("Clients.txt","r") 
        nbClients=len(fileClients.readlines()) 
        fileClients= open ("Clients.txt","r")  
        tab=fileClients.readline()
        a=0
        while nbClients!=0:
            file=tab.split(",")
            tab=fileClients.readline()
            if file[0]==list[0]:
                a+=1
            nbClients-=1
        fileClients.close()
        
        #add client on .txt
        if a==0:
            with  open ("Clients.txt","a") as fileClients:
                list=[lastname,firstname,dob,address,password,email]
                for word in list:
                    fileClients.write(str(word)+",")
                fileClients.write("\n")
                fileClients.close()
        
    def LoginClient(self):
        
        while True:
       
            fichier=open("Clients.txt","r",encoding='utf-8')  #number of client
            nbClient=len(fichier.readlines())
            nbclient=nbClient
            
            fichier=open("Clients.txt","r",encoding='utf-8') #get the information out of the .txt
            listEmail=[]
            listPassword=[]
            listFirstname=[]
            listlastname=[]
            tab=fichier.readline()
            while nbClient!=0:
                list=tab.split(",")
                listFirstname.append(list[1])
                listlastname.append(list[0])
                listEmail.append(list[5])
                listPassword.append(list[4])
                tab=fichier.readline()
                nbClient-=1

            email=str(input("\nenter your email address: ")) #ask email and password
            password=str(input("\nenter your password : "))
            print("\nsearching for your account...")
            sleep(1)
            i=0
            y=1
           
            while i<nbclient: #check if email and password (3 tries) are corrects
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

            if i==nbclient:
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
        
        
            
class Shipper :
    def Informations(self):
        ()#todo
    def Orders(self):
        ()#todo

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
                salary=int(input("\nEnter the salary of the new admin (in $) : "))
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