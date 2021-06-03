import math
from Field import *
from random import *
from graphics import *
from Scoreboard import *
from BallObject import *
from BrickObject import *
from PaddleObject import *
from inputlistener import InputListener
from BallBrickCollision import ballBrickCollision

#Figured out how to use the key input file to move my paddle but could not figure out how to 
#change variables from within the click() function to make buttons.


#Added shrinking paddle and the ball gets faster everytime it hits a brick 


#Line 33 is the section to disable abyss


def main():

    isRunning = True
    gameOver = False
    gameRestart = False
    
# Must be set to 1 so the window can load
    level = 1

# Set this to False to disable Abyss
    
    abyssOn = True



    #Turn positive numbers into negative and negative to positive
    def opposite(x):

        return -x

    #Easy way to help me add speed to the ball
    def gainSpeed(gain):

        if(level == 1):
        
            amountOfSpeed = float(0.02)
        
        else:
            amountOfSpeed = float(0.02)

        if(gain >= 0):
            return gain + amountOfSpeed
        else:
            return gain - amountOfSpeed

    def keyPress(key):
        if(key == 'Left'):
            if(paddleObject.paddle.getP1().getX() > 51):

                paddleObject.paddle.move(-40 , 0)

                if(paddleObject.paddle.getP1().getX() < field.leftWall.getP2().getX()):

                    howMuchPaddleMove = field.leftWall.getP2().getX() - paddleObject.paddle.getP1().getX()
                    
                    paddleObject.paddle.move(howMuchPaddleMove, 0)


        elif(key == 'Right'):
            if(paddleObject.paddle.getP2().getX() < windowWidth - 51):

                paddleObject.paddle.move(40 , 0)

                if(paddleObject.paddle.getP2().getX() > field.rightWall.getP1().getX()):

                    howMuchPaddleMove = paddleObject.paddle.getP2().getX() - field.rightWall.getP1().getX()
                    
                    paddleObject.paddle.move(-howMuchPaddleMove, 0)

        else:

            paddleObject.paddle.move(0 , 0)


    def keyRelease(key):
        keyDown = False


    def click(point):
            
        if(point.getX() > restartButton.getP1().getX() and point.getX() < restartButton.getP2().getX()):
           if(point.getY() > restartButton.getP1().getY() and point.getY() < restartButton.getP2().getY()): 
                global gameOver
                gameOver = True

        if(point.getX() > abyssButton.getP1().getX() and point.getX() < abyssButton.getP2().getX()):
           if(point.getY() > abyssButton.getP1().getY() and point.getY() < abyssButton.getP2().getY()): 
                global abyssOn
                gameOver = False


    while(isRunning == True and level <= 3):
        if(level == 1 and gameOver != True):

        #Game Settings

            windowWidth = 600
            windowHeight = 700

            win = GraphWin("BREAKOUT", windowWidth, windowHeight)
            events = InputListener(win)

            backGround = Rectangle(Point(0, 0), Point(windowWidth, windowHeight))
            backGround.draw(win)
            backGround.setFill('black')


        #Field Creation

            field = Field(windowWidth, windowHeight)

            field.topWall.draw(win)
            field.topWall.setFill('white')

            field.leftWall.draw(win)
            field.leftWall.setFill('white')

            field.rightWall.draw(win)
            field.rightWall.setFill('white')


    #Disable Abyss and Restart Button

        restartButton = Rectangle(Point(60, 10), Point(120, 30))
        restartButton.draw(win)

        restartDisplay = Text(Point(90, 20), "Restart")
        restartDisplay.draw(win)

        abyssButton = Rectangle(Point(480, 10), Point(540, 30))
        abyssButton.draw(win)

        abyssDisplay = Text(Point(510, 20), "Abyss")
        abyssDisplay.draw(win)


    #Score/Life Creation and Settings

        # scoreLocation = Point(200, 20)
        # scoreCurrent = 0
        # scoreText = "Score: " + str(scoreCurrent)
        # scoreDisplay = Text(scoreLocation, scoreText)

        # lifeLocation = Point(400, 20)
        # lifeCurrent = 5
        # lifeText = "Lives: " + str(lifeCurrent)
        # lifeDisplay = Text(lifeLocation, lifeText)
        
        scoreboard = Scoreboard()
        scoreboard.scoreDisplay.draw(win)
        scoreboard.lifeDisplay.draw(win)

    #Ball Creation and Settings

        randomBallMovementX = uniform(-2,2)

        if(randomBallMovementX >= -1 and randomBallMovementX < 0):

            randomBallMovementX -= 1

        elif(randomBallMovementX <= 1 and randomBallMovementX > 0):

            randomBallMovementX += 1

        randomBallMovementY = -1

        ballObject = BallObject(300, 400, 6)
        ballObject.newBall.draw(win)
        ballObject.newBall.setFill('white')

        speedScale = 0.25
        xSpeed = float(randomBallMovementX * speedScale)
        ySpeed = float(randomBallMovementY * speedScale)
        
    #Paddle Creation

        paddleObject = PaddleObject(300, 50)
        paddleObject.paddle.draw(win)
            
        #Brick Creation and Settings For level 1

        if(level == 1):

            numOfBricks = 32

            brickXPos = 63
            brickYPos = 60
            brickWidth = 55
            spaceBetween = 25
            brickObject = BrickObject()

            brickColors = ['red', 'blue', 'green', 'yellow', 'purple']

        #Brick Drawing

            for bricks in range(numOfBricks):

                if(bricks == 8):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                elif(bricks == 16):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                elif(bricks == 24):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                brickObject.createBrick(brickXPos, brickYPos, brickWidth, bricks)

                randomNumber = randrange(5)

                brickObject.brickList[bricks].draw(win)
                brickObject.brickList[bricks].setFill(brickColors[randomNumber])

                brickXPos += brickWidth + 5

    #Brick and Ball Creation and Settings For level 2

        elif(level == 2):
            ballObject.newBall.undraw()
            randomBallMovementX = uniform(-2,2)

            if(randomBallMovementX >= -1 and randomBallMovementX < 0):

                randomBallMovementX -= 1

            elif(randomBallMovementX <= 1 and randomBallMovementX > 0):

                randomBallMovementX += 1

            randomBallMovementY = -1

            ballObject = BallObject(300, 400, 6)
            ballObject.newBall.draw(win)
            ballObject.newBall.setFill('white')

            speedScale = 1
            xSpeed = float(randomBallMovementX * speedScale)
            ySpeed = float(randomBallMovementY * speedScale)
            
            numOfBricks = 64

            brickXPos = 63
            brickYPos = 60
            brickWidth = 55
            spaceBetween = 25
            brickObject = BrickObject()

            brickColors = ['red', 'blue', 'green', 'yellow', 'purple']

        #Brick Drawing

            for bricks in range(numOfBricks):

                if(bricks == 8):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                elif(bricks == 16):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                elif(bricks == 24):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween
                
                elif(bricks == 32):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                elif(bricks == 40):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                elif(bricks == 48):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween
                
                elif(bricks == 56):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                elif(bricks == 64):

                    brickXPos = 63
                    brickYPos = brickYPos + spaceBetween

                brickObject.createBrick(brickXPos, brickYPos, brickWidth, bricks)

                randomNumber = randrange(5)

                brickObject.brickList[bricks].draw(win)
                brickObject.brickList[bricks].setFill(brickColors[randomNumber])

                brickXPos += brickWidth + 5
        elif(level == 3):
            youWin = Text(Point(300, 350), "You Win!")
            youWin.draw(win)
            youWin.setSize(20)
            youWin.setFill("white")


    ##Game Running-----------------------------------------------------------------------

        while(gameOver == False and level != 3):

            # print(restartGame)

            paddleCurrentWidth = paddleObject.paddle.getP2().getX() - paddleObject.paddle.getP1().getX()
            
    #Ball Movement--------------------------

            ballObject.newBall.move(xSpeed, ySpeed)


    #Constant Collision Detection

    #Window

            if(ballObject.newBall.getP1().getX() <= 0):
                xSpeed = opposite(xSpeed)
            elif(ballObject.newBall.getP2().getX() >= windowWidth):
                xSpeed = opposite(xSpeed)
            elif(ballObject.newBall.getP1().getY() <= 0):
                ySpeed = opposite(ySpeed)
            elif(ballObject.newBall.getP2().getY() >= windowHeight - 10):
                ySpeed = opposite(ySpeed)


#Abyss Settings-------------------------------------------------------------------------------------------
                if(abyssOn):
                    if(scoreboard.life >= 0):

                        scoreboard.lifeDisplay.undraw()
                        scoreboard.minusLife()
                        scoreboard.lifeDisplay.draw(win)

                    else:
                        gameOver = True
                else:
                    pass

#-----------------------------------------------------------------------------------------------------


    #Bricks 

            for brickCollision in brickObject.brickList:

                collisionResults = ballBrickCollision(brickCollision, ballObject.newBall, xSpeed, ySpeed)


                if(collisionResults == ''):
                    
                    pass

                elif(collisionResults == 'x'):

                    brickObject.brickList.remove(brickCollision)

                    xSpeed = gainSpeed(opposite(xSpeed))
                    ySpeed = gainSpeed(ySpeed)
                    brickCollision.undraw()

                    scoreboard.scoreDisplay.undraw()
                    scoreboard.addScore()
                    scoreboard.scoreDisplay.draw(win)

                elif(collisionResults == 'y'):

                    brickObject.brickList.remove(brickCollision)
                    xSpeed = gainSpeed(xSpeed)
                    ySpeed = gainSpeed(opposite(ySpeed))
                    brickCollision.undraw()

                    scoreboard.scoreDisplay.undraw()
                    scoreboard.addScore()
                    scoreboard.scoreDisplay.draw(win)


                #sometimes ball will hit corner even if theres a brick above or below, which makes the balls movement slightly off
                elif(collisionResults == 'xy'):

                    brickObject.brickList.remove(brickCollision)
                    xSpeed = gainSpeed(opposite(xSpeed))
                    ySpeed = gainSpeed(opposite(ySpeed))
                    brickCollision.undraw()

                    scoreboard.scoreDisplay.undraw()
                    scoreboard.addScore()
                    # scoreText = "Score: " + str(scoreCurrent)
                    # scoreDisplay = Text(scoreLocation, scoreText)
                    scoreboard.scoreDisplay.draw(win)
            

    #Field Collision

            leftWallCollision = ballBrickCollision(field.leftWall, ballObject.newBall, xSpeed, ySpeed)
            rightWallCollision = ballBrickCollision(field.rightWall, ballObject.newBall, xSpeed, ySpeed)
            topWallCollision = ballBrickCollision(field.topWall, ballObject.newBall, xSpeed, ySpeed)

            if(leftWallCollision == 'x'):

                ballObject.newBall.move(10, 0)
                xSpeed = opposite(xSpeed)

            elif(rightWallCollision == 'x'):

                ballObject.newBall.move(-10, 0)
                xSpeed = opposite(xSpeed)

            elif(topWallCollision == 'y'):
                ballObject.newBall.move(0, 5)
                ySpeed = opposite(ySpeed)

                
    #Paddle Collision

            insidePaddle = False

            #Detects to see if paddle is moved and ball gets trapped inside paddle
                
            if(ballObject.newBall.getCenter().getX() > paddleObject.paddle.getP1().getX() and ballObject.newBall.getCenter().getX() < paddleObject.paddle.getP2().getX()):

                if(ballObject.newBall.getCenter().getY() > paddleObject.paddle.getP1().getY() and ballObject.newBall.getCenter().getY() < paddleObject.paddle.getP2().getY()):
                 
                    howMuchBallMove = ballObject.newBall.getCenter().getY() - paddleObject.paddle.getP1().getY()

                    ballObject.newBall.move(0, -howMuchBallMove - 6)
                    
                    ySpeed = opposite(ySpeed)

                    insidePaddle = True

            if(insidePaddle == False):

                paddleCollision = ballBrickCollision(paddleObject.paddle, ballObject.newBall, xSpeed, ySpeed)

                if(paddleCollision == 'x'):

                    xSpeed = opposite(xSpeed)
                    
                    if(paddleCurrentWidth > 70):
                        paddleObject.paddle.undraw()
                        paddleObject.shrink(paddleCurrentWidth, paddleObject.paddle.getP1().getX(), 2)
                        paddleObject.paddle.draw(win)

                    

                elif(paddleCollision == 'y'):

                    ySpeed = opposite(ySpeed)

                    if(paddleCurrentWidth > 70):
                        paddleObject.paddle.undraw()
                        paddleObject.shrink(paddleCurrentWidth, paddleObject.paddle.getP1().getX(), 2)
                        paddleObject.paddle.draw(win)

                elif(paddleCollision == 'xy'):

                    xSpeed = opposite(math.floor(xSpeed) + 2)
                    ySpeed = opposite(ySpeed)

                    if(paddleCurrentWidth > 70):
                        paddleObject.paddle.undraw()
                        paddleObject.shrink(paddleCurrentWidth, paddleObject.paddle.getP1().getX(), 2)
                        paddleObject.paddle.draw(win)

            if(level == 1 and scoreboard.score == 32):
                
                gameOver = True
                paddleObject.paddle.undraw()
                ballObject.newBall.undraw()
                scoreboard.scoreDisplay.undraw()
                scoreboard.lifeDisplay.undraw()

            elif(level == 2 and scoreboard.score == 64):

                gameOver = True
                paddleObject.paddle.undraw()
                ballObject.newBall.undraw()
                scoreboard.scoreDisplay.undraw()
                scoreboard.lifeDisplay.undraw()

            if(scoreboard.life == 0):
                gameOver = True
                isRunning = False
                gameOverText = Text(Point(windowWidth/2, windowHeight/2), "Game Over! Try Again.")
                gameOverText.setSize(20)
                gameOverText.setFill('white')
                gameOverText.draw(win)

            #Input----------------------------------

            events.setKeyPressHandler(keyPress)
            events.setKeyReleaseHandler(keyRelease)
            events.setMouseClickHandler(click)            
            

        level += 1
        gameOver = False
    

    win.getKey()

main()



