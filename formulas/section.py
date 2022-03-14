import main
from main import listx
from main import listy
from main import ratio

sectionX = ((ratio[1]*listx[0])+(ratio[0]*listx[1]))/(ratio[0]+ratio[1])
sectionY = ((ratio[1]*listy[0])+(ratio[0]*listy[1]))/(ratio[0]+ratio[1])

print(sectionX)
print(sectionY)

