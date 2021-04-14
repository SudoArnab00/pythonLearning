class lineman:

    def __init__(self,cor1,cor2):
        self.cor1 = cor1
        self.cor2 = cor2
    
    def line(self):
        x1,y1 = self.cor1
        x2,y2 = self.cor2

        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def sloppy(self):    
        x1,y1 = self.cor1
        x2,y2 = self.cor2

        return (y2-y1)/(x2-x1)

c1 = (3,5)
c2 = (5,2)

myobj = lineman(c1,c2)
print(myobj.line())
print(myobj.sloppy())