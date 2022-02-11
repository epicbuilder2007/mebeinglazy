#import stuff
import time
from random import randint
import argparse
import math

#Arguments
parser = argparse.ArgumentParser(description='what do I even write here')
parser.add_argument('mode', type=int, help='Changes formulas based on the integer given for this argument. 1 is distance formula, 2 is slope formula, 3 is mid-point formula, 4 is section formula')
parser.add_argument('--fp', type=float, nargs=2, help='Coordinates of the first point, determines x1 and y1. No need for the comma, just use Space.')
parser.add_argument('--sp', type=float, nargs=2, help='Coordinates of the second point, determines x2 and y2. No need for the comma, just use Space.')
parser.add_argument('--ratio', type=int, nargs=2, help='Insert ratio when the formula for the mode needs it.')

#Parse Arguments
args = parser.parse_args()

mode = args.mode
x = [args.fp[0], args.sp[0]]
y = [args.fp[1], args.sp[1]]
ratio = args.ratio

if mode == 1:
    dist = math.sqrt(((x[1]-x[0])**2)+((y[1]-y[0])**2))
    print(dist)
    
elif mode == 2:
    slope = (y[1]-y[0])/(x[1]-x[0])
    print(slope)
    
elif mode == 3:
    mid_point_x = (x[0]+x[1])/2
    mid_point_y = (y[0]+y[1])/2
    print(mid_point_x)
    print(mid_point_y)
elif mode == 4:
    section_formula_x = ((ratio[1]*x[0])+(ratio[0]*x[1]))/(ratio[0]+ratio[1])
    section_formula_y = ((ratio[1]*y[0])+(ratio[0]*y[1]))/(ratio[0]+ratio[1])
    print(section_formula_x)
    print(section_formula_y)
elif mode == 5:
    print('You hath uncovered le secret mode, which gives thou le sacred numbre.')
    print('Le council shalt decide thou fate, please waite.')
    time.sleep(randint(1,10))
    print('Ze council hath decided zat {} shalt be thou sacred passage for the day'.format(randint(1,380000)))
else:
    print('no such mode, perhaps in the future there will?')
    
