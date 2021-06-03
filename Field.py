from graphics import *

class Field:
	
	def __init__(self, windowWidth, windowHeight):

		self.windowWidth = windowWidth
		self.windowHeight = windowHeight

		self.topWall = Rectangle(Point(45, 5), Point(windowWidth - 45, 35))
		self.leftWall = Rectangle(Point(5, 5), Point(50, windowHeight + 10))
		self.rightWall = Rectangle(Point(windowWidth - 50, 5), Point(windowWidth - 5, windowHeight + 10))