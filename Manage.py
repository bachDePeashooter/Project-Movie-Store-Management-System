from math import *
from input import Input
from output import Output
import domains
import login


class Homepage():
    def __init__(self):
        self.movieList = []
        self.order = []
        self.inputMovieList = Input(self.movieList)
        self.outputMovieList = Output(self.movieList)

    def buyMovie(self):
        self.inputMovieList.loadData() #Take data from file
        self.outputMovieList.printMovieList(self.movieList)
        listOfMovieID = []
        for i in self.movieList:
            ID = str(i.getId())
            listOfMovieID.append(ID)

        while True:
            try:
                choice = str(input('Enter ID of the movie you want: '))
                if choice in listOfMovieID:
                    for x in range (len(listOfMovieID)):
                        if choice == listOfMovieID[x]:
                            print('Purchase sucessfully')
                            self.movieList[x].setStatus('Ready to ship')
                            self.order.append(self.movieList[x])
                            self.movieList.pop(x)
                            self.outputMovieList.List2File('Orders.dt',self.order)
                            self.outputMovieList.exportData()
                            return True
                else:
                    print('Try again please')
            except ValueError:
                print('Try again please')

    def printOrders(self):
        self.order.clear()
        data = self.inputMovieList.File2List('Orders.dt')
        for i in data:
            movie = domains.Movie(i['_Movie__id'],
                                 i['_Movie__title'],
                                 i['_Movie__duration'],
                                 i['_Movie__cost'],
                                 i['_Movie__status'])
            self.order.append(movie)
        self.outputMovieList.printMovieList(self.order)
    
    def takeOrder(self):
        self.printOrders()
        listOfMovieID = []
        for i in self.order:
            ID = str(i.getId())
            listOfMovieID.append(ID)
        
        while True:
            try:
                choice = str(input('Enter ID of the order: '))
                if choice in listOfMovieID:
                    for x in range (len(listOfMovieID)):
                        if choice == listOfMovieID[x]:
                            print('Order recieved successfully')
                            self.order[x].setStatus('Shipped')
                            self.outputMovieList.List2File('Orders.dt',self.order)
                            return True
                        else:
                            print('Try again please')
            except ValueError:
                print('Try again please')

        
    def main(self):
        while True:
            connection = 0
            Login=0
            SignUp=0
            while True: #Log in or Sign up
                try:
                    connection=int(input("1) Login \n2) Sign up \n3) Exit \n"))
                    if connection==1 or connection==2 or connection==3:
                        break
                    else:
                        print("Error, Please select 1 or 2 \n")
                except ValueError:
                    print("Error, this is not a number")
                
            if connection==1: #if Log in
                while True:
                    try:
                        Login=int(input("1) Login as Admin \n2) Login as Client \n3) Login as Shipper \n4) Exit \n"))
                        if Login==1 or Login==2 or Login==3 or Login==4:
                            break
                        else:   
                            print("Error, Please select 1, 2, 3 or 4")
                    except ValueError:
                        print("This is not a number")
            
                if Login==1:
                    login.Admins().LoginAdmins()
                    while True:
                        while True:
                            try:
                                choice=int(input("\nWhat do you whant to do? : \n1) Add an Admin account \n2)Add a Shipper account \n3)Add a movie \n4) Verify account information \n5)See all movie available \n6)Exit \n"))
                                if choice==1 or choice==2 or choice==3 or choice==4 or choice==5 or choice == 6:
                                    break
                                else:
                                    print("Error, Please select 1, 2, 3, 4, 5 or 6")
                            except ValueError:
                                print("This is not a number")
                        if choice==1:
                            login.Admins().newAdmin() # Add an admin
                        if choice==2:
                            login.Shipper().newShipper() # Add a shipper
                        if choice==3:
                            self.inputMovieList.addMovie() # Add a movie
                            self.outputMovieList.exportData()
                        if choice==4:
                            login.Admins().VerifyAccount() #See information of a client (maybe show all email address and the admin can select one to see all information, if enought time, admin could delete the account)
                        if choice==5:
                            self.inputMovieList.loadData() #Take data from file
                            self.outputMovieList.printMovieList(self.movieList) #See all movie still available, if enought time, see all movie rencently sold
                        if choice==6:
                            break
                
                if Login==2:
                    login.Clients().LoginClient()
                    while True:
                        while True:
                            try:
                                choice=int(input("\nWhat do you whant to do? : \n1)See Information \n2)See all movie available \n3)Buy movie \n4)Order status \n5)Exit \n"))
                                if choice==1 or choice==2 or choice==3 or choice==4 or choice==5:
                                    break
                                else:
                                    print("Error, Please select 1, 2, 3 or 4")
                            except ValueError:
                                print("This is not a number")
                        if choice==1:
                            login.Clients().Informations() #See all Informations, if enought time, can change it, except the email address 
                        if choice==2:
                            self.inputMovieList.loadData() #Take data from file
                            self.outputMovieList.printMovieList(self.movieList) #if choice=2, client can see all movie AVAILABLE and then, he can select one, see the price and add to cart
                        if choice==3:
                            self.buyMovie() #if choice=3, client can see his cart, he can delete his cart or validate it, and then choose delivery or pick up in store
                        if choice==4:
                            self.printOrders()
                        if choice==5:
                            break                          
                
                if Login==3:
                    login.Shipper().LoginShipper()
                    while True:
                        while True:
                            try:
                                choice=int(input("\nWhat do you whant to do? : \n1)See His Information \n2)See the orders in progress \n3)Take Order \n4) Exit \n"))
                                if choice==1 or choice==2 or choice==3 or choice==4 or choice==5:
                                    break
                                else:
                                    print("Error, Please select 1, 2, 3, 4 or 5")
                            except ValueError:
                                print("This is not a number")
                        if choice==1:
                            login.Shipper().Informations() #See all Informations, if enought time, can change it, except the email address and salary
                        if choice==2:
                            self.printOrders()
                        if choice == 3:
                            self.takeOrder() #See all orders, customer’s address, amount of each product, total price, then select one, and select as delivred (delete the orders of the list)
                        if choice==4:
                            break
                        
                if Login==4:
                    exit()

            if connection==2: #if Sign up
                while True:
                    SignUp=int(input("\n1) Sign up as Admin \n2) Sign up as Client \n3) Sign up as Shipper \n4) Exit \n"))
                    if SignUp==1 or SignUp==2 or SignUp==3 or SignUp==4:
                        break
                    else:
                        print("Error, Please select 1, 2, 3 or 4 \n")

                if SignUp==1:
                    print("\nSorry, to sign up an admin account you must already be logged in with an existing admin account")
                if SignUp==2:
                    login.Clients().newClient()
                if SignUp==3:
                    print("\nSorry, to sign up a shipper account you must already be logged as admin account")
                if SignUp==4:
                    exit()

            if connection==3:
                exit()
