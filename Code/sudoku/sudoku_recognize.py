from PIL import Image, ImageEnhance
import subprocess
import sys

sudoku_image = ' '.join(sys.argv[1:]) or "./20170707000354.png"
print(sudoku_image)

im = Image.open(sudoku_image)
im_w,im_h = im.size
print((im_w,im_h))
"""
if min(im_w,im_h) < 400:
    im = im.resize((800,800), Image.NEAREST)
    im_w,im_h = im.size
print((im_w,im_h))
"""
im = im.convert('L')
"""
WHITE, BLACK = 255, 0
im2 = im.point(lambda x: WHITE if x > 230 else BLACK)
im2 = im2.convert('1')
"""
sharpness =ImageEnhance.Contrast(im)
sharp_img = sharpness.enhance(2.0)

imgdata = sharp_img.getdata()


# Get Grid X
def gridline_x(im_w, im_h):
    line_list = []
    for i in range(im_h):
        i_sum = sum([imgdata[i*im_w + j ] for j in range(im_w) ])
        if i_sum / im_w < 150:
            if not len(line_list):
                line_list.append([i,i])
            elif line_list[-1][1] + 1 < i:
                line_list.append([i,i])
            elif line_list[-1][1] + 1 == i:
                line_list[-1][1] += 1
            else:
                print(i)
    return line_list

# Get Grid Y
def gridline_y(im_w, im_h):
    line_list = []
    for i in range(im_w):
        i_sum = sum([imgdata[j*im_w + i ] for j in range(im_h) ])
        if i_sum / im_w < 150:
            if not len(line_list):
                line_list.append([i,i])
            elif line_list[-1][1] + 1 < i:
                line_list.append([i,i])
            elif line_list[-1][1] + 1 == i:
                line_list[-1][1] += 1
            else:
                print(i)
    return line_list

line_x = gridline_x(im_w, im_h)
line_y = gridline_y(im_w, im_h)

print (line_x)
print (line_y)

sudokuarray = [[""]*9 for i in range(9)]

for i in range(9):
    for j in range(9):
        savename = './tmp/tmp_'+str(i)+str(j)+'.jpg'
        
        imnew = im.crop((line_y[i][1]+3, line_x[j][1]+3, line_y[i+1][0]-3, line_x[j+1][0]-3 ))

        """
        # Two value process
        WHITE, BLACK = 255, 0
        imnew = imnew.point(lambda x: WHITE if x > 210 else BLACK)
        imnew = imnew.convert('1')
        
        imnew = imnew.convert('L')
        sharpness =ImageEnhance.Contrast(imnew)
        sharp_img = sharpness.enhance(2.0)
        sharp_img.save(savename)
        """
        imnew.save(savename)

        imgtmp = Image.open(savename).getdata()
        if sum(imgtmp)/len(imgtmp) < 246:
            shellstr = 'tesseract ' + savename + ' stdout -c tessedit_char_whitelist=0123456789 -psm 10'
            txt = subprocess.check_output(shellstr, shell=True).decode().strip()
            sudokuarray[j][i] = int(txt) if len(txt) else 0
        else:
            sudokuarray[j][i] = 0

board = ["".join([str(j) for j in i ]).replace('0','.') for i in sudokuarray]
print("The input Sudoku:\n")
print("\n".join([" ".join(i) for i in board]),end='\n\n')

from sudoku_solver import Solution
s = Solution()
boardnew = [list(i) for i in board]
s.solveSudoku(boardnew)

print ("The solved Sudoku:\n")
print("\n".join([" ".join(i) for i in boardnew]),end='\n\n')
