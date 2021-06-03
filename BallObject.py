from graphics import *

class BallObject:


    def __init__(self, xPos, yPos, radius):

        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        self.newBall = Circle(Point(self.xPos, self.yPos), self.radius)

 

##      Debugging Process

##    def addBall(self, window):
##
##        return self.newBall.draw(window)
##
##    def removeBall(self, window):
##
##        return self.newBall.draw(window)
##
##    def move(self, xVel, yVel):
##
##        return self.newBall.move(xVel, yVel)
##        
##        
##    def ballActive(self, activated):
##
##        speedScale = 10
##        xSpeed = 1
##        ySpeed = 1
##        
##        while (activated):
##
##            self.newBall.move(xSpeed, ySpeed)
##
##            if
            
