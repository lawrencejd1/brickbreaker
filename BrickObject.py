from graphics import *

class BrickObject:

	def __init__(self):

		self.brickList = []

	def createBrick(self, xPos, yPos, width, name):


		self.xPos = xPos
		self.yPos = yPos
		self.width = width

		self.name = Rectangle(Point(self.xPos, self.yPos), Point(self.xPos + self.width, self.yPos + 20))
		

		self.brickList.append(self.name)

	def destroyBrick(self, brickNumber):

		self.brickNumber = brickNumber

		self.brickList.remove(self.brickNumber)





