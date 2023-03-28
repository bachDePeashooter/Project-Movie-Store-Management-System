import json
import domains
class Input:
    def __init__(self, saleList):
        self.__saleList = saleList

    def inputMovie(self):
        id = int(input('ID: '))
        title = str(input('Title of the film: '))
        duration = str(input('Duration: '))
        cost = int(input('Cost: '))
        quantity = int(input('Quantity: '))
        movie = domains.Movie(id,title,duration,cost,quantity)
        self.__saleList.append(movie)


    def addMovie(self):
        numberOfMovie = int(input('Enter number of movies u wanna add: '))
        for i in range(numberOfMovie):
            self.inputMovie()
    
    def File2List(self, filename): #read from json file
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    
    def loadData(self):
        self.__saleList.clear()
        filename = 'Movie.dt'
        data = self.File2List(filename)

        for i in data:
            movie = domains.Sale(i['_Sale__id'],
                                 i['_Sale__title'],
                                 i['_Sale__duration'],
                                 i['_Sale__cost'],
                                 i['_Sale__quantity'])
        self.__saleList.append(movie)