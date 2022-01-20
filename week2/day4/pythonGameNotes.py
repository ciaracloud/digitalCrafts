#IMPORT PYGAME AND ITS MODULES:
# import pygame
# from pygame.locals import * #allows us to use modules without adding pygame.locals prefix

#NEED THIS LINE TO USE PYGAME MODULES:
# pygame.init()

#GAME LOOP(where all the game events occur):
# while True:
#       # Code
#       # Code
#       .
#       .
#       pygame.display.update() #this line updates the game and is included in the game loop

#QUITTING THE GAME LOOP/EVENT OBJECTS:
# while True:
#     pygame.display.update()
#     for event in pygame.event.get(): #An “Event” occurs when the user performs a specific action, such as clicking his mouse or pressing a keyboard button/We can find out which events have happened by calling the pygame.event.get() function
#         if event.type == QUIT: #Side note: If you didn’t import everything from pygame.locals as we did you would have to use pygame.locals.QUIT instead of QUIT
#             pygame.quit() #We call both pygame.quit() and sys.exit() to close the pygame window and the python script respectively
#             sys.exit() #Simply using sys.exit() can cause your IDE to hang due to a bug

#DISPLAY SCREEN:
#For every game, we create a window of a fixed size by passing a tuple containing the width and height. This tuple is then passe into the display.set_mode() function.
# DISPLAYSURF = pygame.display.set_mode((300,300))

#To show a set of co-ordinates, you place both the X and Y values in a tuple, where the first integer is X and second integer is Y.
# pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)

#COLOR OBJECTS:
#create color objects using RGB values
# color1 = pygame.Color(0, 0, 0)         # Black
# color2 = pygame.Color(255, 255, 255)   # White
# color3 = pygame.Color(128, 128, 128)   # Grey
# color4 = pygame.Color(255, 0, 0)       # Red

#We use the fill(color) method to fill in objects. For instance, assigning a rectangle the color green will only turn the borders green. If you use the fill() method and pass a green color object, the rectangle will become completely green.

#PARAMETERS:
#<surface parameter> is the surface object on which pygame will draw the shape.
#<color parameter> is the designated color of the assigned shape.
#The <pointlist parameter> is a tuple containing co-ordinates or “points”. For instance, for a rectangle you will pass a tuple with 4 co-ordinate pairs inside it.
#<width> is an optional parameter that determines the size of the outline of the shape. Takes integer values.
#<start_point> and <end_point> represent a set of co-ordinates. The line begins at one set of co-ordinates and ends at another. Likewise, <center_point> is the origin point of a circle.

# PYGAME DRAWING FUNCTIONS:
# - pygame.draw.polygon(surface, color, pointlist, width)
# - pygame.draw.line(surface, color, start_point, end_point, width)
# - pygame.draw.lines(surface, color, closed, pointlist, width)
# - pygame.draw.circle(surface, color, center_point, radius, width)
# - pygame.draw.ellipse(surface, color, bounding_rectangle, width)
# - pygame.draw.rect(surface, color, rectangle_tuple, width)

#FRAMES PER SECOND
#To limit the amount of times the computer can loop through we use the tick(fps)method where fps is an integer. The tick() method belongs to the pygame.time.Clock class and must be used with an object of this class.
#usually 30-60
# FPS = pygame.time.Clock()
# FPS.tick(60)

#CREATING SHAPES(test):
import pygame, sys
from pygame.locals import *
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300,300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")
 
# Creating Lines and Shapes
pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
 
# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)

#RECTANGLE COORDINATE ORDER:
# 1. The X co-ordinate of the upper left corner of the rectangle, also known as the X co-ordinate from where the Rectangle begins.
# 2. The Y co-ordinate of the upper left corner of the rectangle, also known as the Y co-ordinate from where the Rectangle begins.
# 3. The Width (Length) of the Rectangle in pixels.
# 4. The Height of the Rectangle in pixels.