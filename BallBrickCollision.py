from graphics import *

def ballBrickCollision(brick,ball,xv,yv):
    """Determine the collision results between a Rectangle and Circle

    Created by Jeremy Porier, 2017/12/05
    ### This code should be considered 'good enough' for most gaming uses, though there are a few corner bounce
    ### scenarios that I acknowledge are not as realistic as they could be

    Keyword arguments:
    brick -- an object created with, or inheriting, the Rectangle class from Zelle's graphics.py library
    ball -- an object created with, or inheriting, the Circle class from Zelle's graphics.py library
    xv -- an integer of the ball's x velocity
    yv -- an integer of the ball's y velocity
    
    This function assumes that:
       1.  The center of the ball never goes into a brick (the function does NOT test this)
       2.  P1 of a Rectangle is always the top left corner
    
    Possible return values:
      'x' means bounce the x axis
      'y' means bounce the y axis
      'xy' indicates a corner hit that should bounce both axis
    """
    
    #do we even have a prayer of hitting this brick?
    if not(brick.getP1().getX() - ball.getRadius() < ball.getCenter().getX() < brick.getP2().getX() + ball.getRadius() and brick.getP1().getY() - ball.getRadius() < ball.getCenter().getY() < brick.getP2().getY() + ball.getRadius()):
        #not a chance, bail out now
        return ''
    
    #calculate the cheapest and most likely hits
    if brick.getP1().getX() <= ball.getCenter().getX() <= brick.getP2().getX():
        #in x range
        if brick.getP1().getY() - ball.getRadius() <= ball.getCenter().getY() <= brick.getP1().getY() or brick.getP2().getY() + ball.getRadius() >= ball.getCenter().getY() >= brick.getP2().getY():
            return 'y'
    elif brick.getP1().getY() <= ball.getCenter().getY() <= brick.getP2().getY():
        #in y range
        if brick.getP1().getX() - ball.getRadius() <= ball.getCenter().getX() <= brick.getP1().getX() or brick.getP2().getX() + ball.getRadius() >= ball.getCenter().getX() > brick.getP2().getX():
            return 'x'

    #No easy to calculate hits, but the ball may have hit one of the corners of the brick
    
    #cp is the closest point on the brick to the ball, and because of the code above it should be one of the corners
    cp = Point(max(brick.getP1().getX(), min(ball.getCenter().getX(), brick.getP2().getX())), max(brick.getP1().getY(), min(ball.getCenter().getY(), brick.getP2().getY())))
    
    #first check to see if the ball has hit the brick
    if (ball.getCenter().getX() - cp.getX())**2 + (ball.getCenter().getY() - cp.getY())**2 <= ball.getRadius()**2:

        #there is a corner hit, now determine which sides were hit
        if brick.getP1().getX() == cp.getX():

            #hit one of the left corners
            if brick.getP1().getY() == cp.getY():
                #top left corner hit
                if xv > 0:
                    if yv > 0:
                        #bounce x and y
                        return 'xy'
                    else:
                        #bounce x only
                        return 'x'
                else:
                    #bounce y only
                    return 'y'
            else:
                #bottom left corner hit
                if xv > 0:
                    if yv < 0:
                        #bounce x and y
                        return 'xy'
                    else:
                        #bounce x only
                        return 'x'
                else:
                    #bounce y only
                    return 'y'
        else:
            #hit one of the right corners
            if brick.getP2().getY() == cp.getY():
                #bottom right corner hit
                if xv < 0:
                    if yv < 0:
                        #bounce x and y
                        return 'xy'
                    else:
                        #bounce x
                        return 'x'
                else:
                    #bounce y
                    return 'y'
            else:
                #top right corner hit
                if xv < 0:
                    if yv > 0:
                        #bounce x and y
                        return 'xy'
                    else:
                        #bounce x
                        return 'x'
                else:
                    #bounce y
                    return 'y'
        return ''
    else:
        #not a hit
        return ''
