import json

class Output:
    def __init__(self, movieList):
        self.__movieList = movieList
    
    def getMovieList(self):
        return self.__movieList
    
    def printMovieList(self, lst):
        for i in lst:
            print("\nID: " + str(i.getId())
                  + "\nTitle: " + str(i.getTitle())
                  + "\nDuration: " + str(i.getDuration())
                  + '\tCost: ' + str(i.getCost()) + '$'
                  + '\tStatus: ' + str(i.getStatus())
                  )
    
    def List2File(self, filename, lst): 
        with open(filename, "w") as file:
            json.dump(lst, file, default=lambda o: o.__dict__, indent=4)
    
    def exportData(self):
        filename = 'Movie.dt'
        self.List2File(filename,self.__movieList)

            