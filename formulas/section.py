import main
from main import x
from main import y
from main import ratio

sectionX = ((ratio[1]*x[0])+(ratio[0]*x[1]))/(ratio[0]+ratio[1])
sectionY = ((ratio[1]*y[0])+(ratio[0]*y[1]))/(ratio[0]+ratio[1])

print(sectionX)
print(sectionY)

