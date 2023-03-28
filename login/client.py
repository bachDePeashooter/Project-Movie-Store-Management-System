from time import *
class Clients :
    def __init__(self) -> None:
        pass
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