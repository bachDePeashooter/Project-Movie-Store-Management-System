class Movie:
    def __init__(self, id, title, duration, cost, quantity):
        self.__id = id
        self.__title = title
        self.__duration = duration
        self.__cost = cost
        self.__quantity = quantity

    def __str__(self):
        return f'Movie[Id={self.__id}, Title={self.__title}, Duration={self.__duration}, Cost={self.__cost}, Quantity={self.__quantity}]'
    
    def set_id(self, quantity):
        self.__quantity = quantity

    def getId(self):
        return self.__id
    def getQuantity(self):
        return self.__quantity
    def getTitle(self):
        return self.__title
    def getDuration(self):
        return self.__duration
    def getCost(self):
        return self.__cost