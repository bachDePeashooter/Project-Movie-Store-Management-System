import json

class Output:
    def __init__(self, saleList):
        self.__saleList = saleList
    
    def getSaleList(self):
        return self.__saleList
    
    def printSaleList(self):
        for i in self.__saleList:
            print("\nID: " + str(i.getId())
                  + "\nTitle: " + str(i.getTitle())
                  + "\nDuration" + str(i.getDuration())
                  + '\nCost' + str(i.getCost())
                  + '\nQuantity' + str(i.getQuantity())
                  )
    
    def List2File(self, filename, lst): 
        with open(filename, "w") as file:
            json.dump(lst, file, default=lambda o: o.__dict__, indent=4)
    
    def exportData(self):
        filename = 'Movie.dt'
        self.List2File(filename,self.__saleList)

            