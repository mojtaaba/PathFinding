class node:
  def __init__(this,X,Y,walkable):
        this.Walkable = walkable
        this.X = Y
        this.Y = Y
        this.Parent=null
        this.G=G
        this.H=H 

  def getF(self):
        return G+h

  def getDistance(self,otherNode):
        distanceX = abs(self.X-self.X)
        distanceY = abs(self.Y-self.Y)
        return 14*min(distanceY,distanceX) + 10*abs(distanceX-distanceY)
  def toString():
        print(X+" "+Y+" "+Walkable) 