#imports the variables
import main
from main import x
from main import y
import math

#actual formula
dist = math.sqrt(((x[1]-x[0])**2)+((y[1]-y[0])**2))
print(dist)
