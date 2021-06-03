from graphics import *

class PaddleObject:

	def __init__(self, start, width):

		self.start = start
		self.width = width

		self.paddle = Rectangle(Point(self.start - self.width, 600), Point(self.start + self.width, 610))
		self.paddle.setFill('white')

	def shrink(self, currentWidth, location, amount):

		self.currentWidth = currentWidth
		self.location = location
		self.amount = amount

		self.paddle = Rectangle(Point(self.location, 600), Point(self.location + self.currentWidth - self.amount, 610))
		self.paddle.setFill('white')
