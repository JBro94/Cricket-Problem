#import the necessary modules
import random
from random import randrange
import math 
import array
from numpy import ndarray
import time 

#1000 crickets each jump 1 unit initially, the next jump is .9 of the previous jump
#Say for 1000 jumps what is the distance traveled.

xValue = 0.
yValue = 0.
i = 1
j =1
k = 1
dist = 
x = 0.
y = 0.
dx = 0.
dy = 0.
x_out = []
y_out = []

#loop that goes through each cricket that jumped 
while i <= 100: 
#loop that goes through each jump that a specific cricket took 
    while j <= 1000:
        d = .9**(j-1) #this is the distance that the cricket jumped each jump
        theta = 2 * math.pi * random.uniform(0.,1.) #the random direction of the jump
        dx = d*(math.cos(theta)) #calculate the distance traveled in the x direction 
        dy = d*(math.sin(theta)) # calculate the distance treveled in the y direction
        x = x + dx
        y = y + dy
        j += 1

    x_out.append(x)
    y_out.append(y)
    i += 1

while k <= 1000:
    
    
    
    

    
    
    
