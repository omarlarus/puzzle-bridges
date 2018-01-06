from pyx import *
from ponti import *

DIMESIONS=7
NUM_ISLANDS=9

canv = canvas.canvas()

UNIT=1
CIRCLE=0.25

ROWS = 2
COLS = 3

for r in range(0,ROWS):
    for c in range(0,COLS):
        posX = r*(DIMESIONS+3)*UNIT
        posY = c*(DIMESIONS+3)*UNIT
        canv.stroke(path.rect(posX, posY, (DIMESIONS+2)*UNIT, (DIMESIONS+2)*UNIT))
        matrix = buildMatrix(DIMESIONS,NUM_ISLANDS)
        for x in range(0,DIMESIONS):
            for y in range(0,DIMESIONS):
                if matrix[x][y] > 0:
                    px = posX+1+x*UNIT
                    py = posY+1+y*UNIT
                    canv.stroke(path.circle(px, py, CIRCLE))
                    t = canv.text(px-(CIRCLE/2), py-(CIRCLE/2), str(int(matrix[x][y])))
        


canv.writePDFfile("ponti",page_paperformat=document.paperformat.A4)