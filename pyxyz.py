#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
from timeit import default_timer as timer
import BaseHTTPServer
from urlparse import urlparse, parse_qs
from wand.image import Image
from wand.color import Color
import Image

minx = float('inf'); miny = float('inf'); minz = float('inf')
maxx = float('-inf'); maxy = float('-inf'); maxz = float('-inf')

def fileParse(file):
    global minx; global miny; global minz;
    global maxx; global maxy; global maxz;
    for l in file.readlines ():
          list_values = l.split ()
          xFile = float(list_values[0])
          yFile = float(list_values[1])
          zFile = float(list_values[2])
          minx = min(xFile,minx); miny = min(yFile,miny); minz = min(zFile,minz);
          maxx = max(xFile,maxx); maxy = max(yFile,maxy); maxz = max(zFile,maxz);

def creationImage(files):
    print('min : ', minx, miny, minz)
    print('max : ', maxx, maxy, maxz)

    l = int(maxx - minx); h = int(maxy - miny);
    #creation image... :
    im = Image.new("RGB",(l,h), 'BLACK')

    print('Modification image...')

    for f in range(1,len(files)):
        for l in open(files[f],"r").readlines ():
              list_values = l.split ()
              x = float(list_values[0])
              y = float(list_values[1])
              z = float(list_values[2])
              tempX = int(x - minx)
              tempY = int(maxy - y)
              pixelColor = int(((z - minz) * 255) / (maxz - minz))
              im.putpixel((tempX if tempX == 0 else tempX - 1, tempY if tempY == 0 else tempY - 1), (pixelColor,pixelColor,pixelColor))

    im.save("image.png")
    print('image save... ok')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python dummywms.py image_full_path')
        sys.exit(1)

    print('Start to Convert...')
    for n in range(1,len(sys.argv)):
        filexyz = open(sys.argv[n],"r")
        fileParse(filexyz)
        print(n , '...file xyz .', sys.argv[n] ,'.. done' )
    print('Creation image...')

    creationImage(sys.argv)
    sys.exit(1)
