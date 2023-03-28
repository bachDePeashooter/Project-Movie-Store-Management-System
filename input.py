import json
import domains
from output import Output
class Input:
    def __init__(self, movieList):
        self.__movieList = movieList

    def inputMovie(self):
        id = int(input('ID: '))
        title = str(input('Title of the film: '))
        duration = str(input('Duration: '))
        cost = int(input('Cost: '))
        quantity = int(input('Quantity: '))
        movie = domains.Movie(id,title,duration,cost,quantity)
        self.__movieList.append(movie)


    def addMovie(self):
        numberOfMovie = int(input('Enter number of movies u wanna add: '))
        for i in range(numberOfMovie):
            self.inputMovie()
    
    def File2List(self, filename): #read from json file
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    
    def loadData(self):
        filename = 'Movie.dt'
        self.__movieList.clear()
        data = self.File2List(filename)

        for i in data:
            movie = domains.Movie(i['_Movie__id'],
                                 i['_Movie__title'],
                                 i['_Movie__duration'],
                                 i['_Movie__cost'],
                                 i['_Movie__quantity'])
            self.__movieList.append(movie)