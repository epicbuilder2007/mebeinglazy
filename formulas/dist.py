#imports the variables
import main
from main import listx
from main import listy
import math

#actual formula
dist = math.sqrt(((listx[1]-listx[0])**2)+((listy[1]-listy[0])**2))
print(dist)
