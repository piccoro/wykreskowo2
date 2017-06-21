import json
import math
import random

xx=[400,800]
ilosc=1000;

def funkcja( l ):
   yy=-0.08*(l-600)**2+4000+random.uniform(-400, 400);
   return yy
dane=[]

for ii in range(0,ilosc+1):
	x=1.0*xx[0]+1.0*ii*(xx[1]-xx[0])/ilosc
	y=funkcja(x)
	dane.append([x,y])

with open('t.json', 'w') as outfile:
    json.dump(dane, outfile)
