from PIL import Image
from math import *

# Functions here
DIM = 1024    

def red(i, j):
    i+=sin(4*pi*j/DIM)*DIM/84;i=max(1,min(i,DIM-1))
    return ceil(4+sin(8*pi*i/DIM)*sin(8*pi*j/DIM)*3)*32

def green(i, j):
    return red(i,j)

def blue(i, j):
    return red(i,j)-cos(4*pi*i/DIM)*16

img = Image.new('RGB', (1024, 1024), "black")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = (int(red(i,j)),int(green(i,j)),int(blue(i,j)))

img.save('image.jpg', 'JPEG')

