#import stuff
import time
from random import randint
import argparse
import importlib

#Arguments
parser = argparse.ArgumentParser(description='what do I even write here')
parser.add_argument('mode', type=str, default='5', help='Changes formulas based on the string given for this argument')
parser.add_argument('--fp', type=float, nargs=2, default=[0, 0], help='Coordinates of the first point, determines x1 and y1. No need for the comma, just use Space.')
parser.add_argument('--sp', type=float, nargs=2, default=[0, 0], help='Coordinates of the second point, determines x2 and y2. No need for the comma, just use Space.')
parser.add_argument('--ratio', type=int, nargs=2, default=[0, 0], help='Insert ratio when the formula for the mode needs it.')
parser.add_argument('--x', type=float, nargs=1, default=0, help='Insert x value for when the formula does not use coordinates.')
parser.add_argument('--y', type=float, nargs=1, default=0, help='Insert y value for when the formula does not use coordinates.')

#Parse Arguments
args = parser.parse_args()

mode = args.mode
listx = [args.fp[0], args.sp[0]]
listy = [args.fp[1], args.sp[1]]
x = args.x
y = args.y


ratio = args.ratio #lmao get ratioed

if mode == '5':
    code = randint(1,395634)
    print('You hath uncovered le secret mode, which gives thou le sacred numbre.')
    print('Le council shalt decide thou fate, please waite.')
    time.sleep(randint(1,10))
    print('Ze council hath decided zat {} shalt be thou sacred passage for the day'.format(code))
    print('link: https://nhentai.net/g/{}'.format(code))
    
elif mode != '5':
    importlib.import_module(str("formulas." + mode), package=None)






