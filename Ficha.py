class Ficha:
    def __init__(self,color,id,x,y):
        self.color = color
        self.id = id
        self.x = x
        self.y = y


    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def setId(self,id):
        self.id = id

    def setX(self, x):
        self.x = x

    def setY(self,y):
        self.y = y
