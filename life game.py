import pygame as p
import numpy as np

cnextdie = (111, 111, 111)
calive = (33, 33, 33)
cbkgrnd = (222, 222, 222)
cgrid = (218, 218, 218)

def update(surface, matrix, csize):
    nxt = np.zeros((matrix.shape[0], matrix.shape[1]))
    for row, col in np.ndindex(matrix.shape):
        numcalive = np.sum(matrix[row-1:row+2, col-1:col+2]) - matrix[row, col]
        if matrix[row, col] == 1 and numcalive < 2 or numcalive > 3:
            col = cnextdie
        elif (matrix[row, col] == 1 and 2 <= numcalive <= 3) or (matrix[row, col] == 0 and numcalive == 3):
            nxt[row, col] = 1
            col = calive
        col = col if matrix[row, col] == 1 else cbkgrnd
        p.draw.rect(surface, col, (col*csize, row*csize, csize-1, csize-1))
    return nxt


def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0]])
    pos = (3, 3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1] :pos[1]+pattern.shape[1]] = pattern
    return cells


def main(dimx, dimy, cellsize):
    p.init()
    flStartDraw = False
    surface = p.display.set_mode((dimx * cellsize, dimy * cellsize))
    p.display.set_caption("Игра жизнь")

    cells = init(dimx, dimy)

    # FPS = 0
    # clock = p.time.Clock()

    while True:
        surface.fill(cgrid)
        cells = update(surface, cells, cellsize)
        
        sp = pos = None
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit() 
            # elif event.type == p.MOUSEBUTTONDOWN:
            #     pos = event.pos
            #     cells[pos[1]//10][pos[0]//10] = 1
            # elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            #     # clock.tick(0)
            #     flStartDraw = True
            #     sp = event.pos
            # elif event.type == p.MOUSEMOTION:
            #     if flStartDraw:
            #         pos = event.pos  
                    # p.draw.rect(surface, (255, 0, 0), p.Rect(sp[0], sp[1], width, height))
                    # p.display.update()
            elif event.type == p.MOUSEBUTTONUP and event.button == 1:
                flStartDraw = False
                for row in range(sp[1]//10,pos[1]//10):
                        for col in range(sp[0]//10, pos[0]//10):
                            cells[row][col]
            # clock.tick(FPS)
        p.display.update()


if __name__ == "__main__":
    main(100, 75, 10)
