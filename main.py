#import stuff
import time
from random import randint
import argparse
import importlib

#Arguments
parser = argparse.ArgumentParser(description='what do I even write here')
parser.add_argument('mode', type=str, help='Changes formulas based on the string given for this argument')
parser.add_argument('--fp', type=float, nargs=2, help='Coordinates of the first point, determines x1 and y1. No need for the comma, just use Space.')
parser.add_argument('--sp', type=float, nargs=2, help='Coordinates of the second point, determines x2 and y2. No need for the comma, just use Space.')
parser.add_argument('--ratio', type=int, nargs=2, help='Insert ratio when the formula for the mode needs it.')
parser.add_argument('--x', type=float, nargs=1, help='For equations that do not need 2 x values')
parser.add_argument('--y', type=float, nargs=1, help='For equations that do not need 2 y values')

#Parse Arguments
args = parser.parse_args()

mode = args.mode
x = [args.fp[0], args.sp[0], args.x]
y = [args.fp[1], args.sp[1], args.y]
ratio = args.ratio

if mode == '5':
    print('You hath uncovered le secret mode, which gives thou le sacred numbre.')
    print('Le council shalt decide thou fate, please waite.')
    time.sleep(randint(1,10))
    print('Ze council hath decided zat {} shalt be thou sacred passage for the day'.format(randint(1,394275)))
    
elif mode != '5':
    importlib.import_module(str(mode), package=None)






