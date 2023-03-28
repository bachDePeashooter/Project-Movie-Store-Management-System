import json

class Output:
    def __init__(self, movieList):
        self.__movieList = movieList
    
    def getMovieList(self):
        return self.__movieList
    
    def printMovieList(self):
        for i in self.__movieList:
            print("\nID: " + str(i.getId())
                  + "\nTitle: " + str(i.getTitle())
                  + "\nDuration: " + str(i.getDuration())
                  + '\nCost: ' + str(i.getCost())
                  + '\nQuantity: ' + str(i.getQuantity())
                  )
    
    def List2File(self, filename, lst): 
        with open(filename, "w") as file:
            json.dump(lst, file, default=lambda o: o.__dict__, indent=4)
    
    def exportData(self):
        filename = 'Movie.dt'
        self.List2File(filename,self.__movieList)

            