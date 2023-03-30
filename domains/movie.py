class Movie:
    def __init__(self, id, title, duration, cost, status):
        self.__id = id
        self.__title = title
        self.__duration = duration
        self.__cost = cost
        self.__status = status

    def __str__(self):
        return f'Movie[Id={self.__id}, Title={self.__title}, Duration={self.__duration}, Cost={self.__cost}, Status={self.__status}]'
    
    def setStatus(self, status):
        self.__status = status

    def getId(self):
        return self.__id
    def getStatus(self):
        return self.__status
    def getTitle(self):
        return self.__title
    def getDuration(self):
        return self.__duration
    def getCost(self):
        return self.__cost