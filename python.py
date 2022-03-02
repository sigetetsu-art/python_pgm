from tkinter import Image
from PIL import Image
import numpy as np

file = open("Image.pgm", "w")

# 元となる画像の読み込み
img = Image.open('buffalo.pgm')
#オリジナル画像の幅と高さを取得
width, height = img.size
# オリジナル画像と同じサイズのImageオブジェクトを作成する
img2 = Image.new('L', (width, height))

img_pixels = []
img_pixels = np.array([[img.getpixel((i,j)) for j in range(height)] for i in range(width)])

file.write("P2\n")
file.write("481 321\n")
file.write("255\n")

for y in range(height):
    for x in range(width):
        s = img_pixels[x][y]
        if(s < 50):
            s = 0
        elif(s < 100):
            s = 100
        elif(s < 150):
            s = 150
        elif(s < 200):
            s = 200
        else:
            s = 255
        file.write(str(s))
        file.write(" ")
        if(x == width - 1):
            file.write("\n")

file.close()   

