from graphics import *

class Scoreboard:

	def __init__(self):
		
		self.score = 0
		self.life = 5
		self.scoreLocation = Point(200, 20)
		self.scoreText = "Score: " + str(self.score)

		self.scoreDisplay = Text(self.scoreLocation, self.scoreText)
		self.lifeLocation = Point(400, 20)
		self.lifeText = "Lives: " + str(self.life)
		self.lifeDisplay = Text(self.lifeLocation, self.lifeText)

	def addScore(self):

		self.score += 1
		self.scoreText = "Score: " + str(self.score)
		self.scoreDisplay = Text(self.scoreLocation, self.scoreText)

	def minusLife(self):

		self.life -= 1
		self.lifeText = "Lives: " + str(self.life)
		self.lifeDisplay = Text(self.lifeLocation, self.lifeText)