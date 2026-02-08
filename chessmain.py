import pygame
from pygame.locals import *

pieces = {
    'Rb': './images/rookb.png',
    'Rw': './images/rookw.png',
    'Cb': './images/knightb.png',
    'Cw': './images/knightw.png',
    'Bb': './images/bishopb.png',
    'Bw': './images/bishopw.png',
    'Qb': './images/queenb.png',
    'Qw': './images/queenw.png',
    'Kb': './images/kingb.png',
    'Kw': './images/kingw.png',
    'Pb': './images/pawnb.png',
    'Pw': './images/pawnw.png',
}


def draw_table():
    screen.fill((119, 149, 86))
    for j in range(8):
        for i in range(8):
            if x > y:
                if i < 4:
                    pygame.draw.rect(screen, (235, 236, 208), (y/8*j+(x-y)/2, y*(i/4)+y/8*(j%2), square_size, square_size))
                if moves[i][j] == 1:
                    pygame.draw.rect(screen, (112, 146, 190), (y/8*j+(x-y)/2, y/8*i, square_size, square_size))
                elif moves[i][j] == 2:
                    pygame.draw.rect(screen, (255, 72, 75), (y/8*j+(x-y)/2, y/8*i, square_size, square_size))
                posx, posy = y/8*j+(x-y)/2, y/8*i
            else:
                if i < 4:
                    pygame.draw.rect(screen, (235, 236, 208), (x/8*j, x*(i/4)+x/8*(j%2)+(y-x)/2, square_size, square_size))
                if moves[i][j] == 1:
                    pygame.draw.rect(screen, (112, 146, 190), (x/8*j, x/8*i+(y-x)/2, square_size, square_size))
                elif moves[i][j] == 2:
                    pygame.draw.rect(screen, (255, 72, 75), (x/8*j, x/8*i+(y-x)/2, square_size, square_size))
                posx, posy = x/8*j, x/8*i+(y-x)/2
            if table[i][j] == 0:
                continue
            img = pygame.image.load(pieces[table[i][j]])
            img = pygame.transform.scale(img, (square_size, square_size))
            screen.blit(img, (posx, posy))

#moves = 1 if free spot, if you can kill moves = 2
def show_allowed(x, y, alt):
    global moves
    match table[y][x]:
        case 0: pass
        case 'Pb':
            if alt:
                if x-1 != -1: moves[y+1][x-1] = 1
                if x+1 != 8: moves[y+1][x+1] = 1
                return
            if y == 1:
                for i in range(1, 3):
                    if table[y+i][x] == 0:
                        moves[y+i][x] = 1
                    else: break
            else:
                if y+1 != 8 and table[y+1][x] == 0:
                    moves[y+1][x] = 1
            if x-1 != -1 and table[y+1][x-1] != 0:
                if table[y+1][x-1][1:] == 'w':
                    moves[y+1][x-1] = 2
                else:
                    moves[y+1][x-1] = 3
            if x+1 != 8 and table[y+1][x+1] != 0:
                if table[y+1][x+1][1:] == 'w':
                    moves[y+1][x+1] = 2
                else:
                    moves[y+1][x+1] = 3
        case 'Pw':
            if alt:
                if x-1 != -1: moves[y-1][x-1] = 1
                if x+1 != 8: moves[y-1][x+1] = 1
                return
            if y == 6:
                for i in range(1, 3):
                    if table[y-i][x] == 0:
                        moves[y-i][x] = 1
                    else: break
            else:
                if y-1 != -1 and table[y-1][x] == 0:
                    moves[y-1][x] = 1
            if x-1 != -1 and table[y-1][x-1] != 0:
                if table[y-1][x-1][1:] == 'b':
                    moves[y-1][x-1] = 2
                else:
                    moves[y-1][x-1] = 3
            if x+1 != 8 and table[y-1][x+1] != 0:
                if table[y-1][x+1][1:] == 'b':
                    moves[y-1][x+1] = 2
                else:
                    moves[y-1][x+1] = 3
        case 'Rb':
            for i in range(1, 8):
                if y-i < 0: break
                if table[y-i][x] == 0: moves[y-i][x] = 1
                else:
                    if table[y-i][x][1:] == 'w':
                        moves[y-i][x] = 2
                        break
                    else:
                        moves[y-i][x] = 3
                        break
            for i in range(1, 8):
                if y+i > 7: break
                if table[y+i][x] == 0: moves[y+i][x] = 1
                else:
                    if table[y+i][x][1:] == 'w':
                        moves[y+i][x] = 2
                        break
                    else:
                        moves[y+i][x] = 3
                        break
            for i in range(1, 8):
                if x-i < 0: break
                if table[y][x-i] == 0: moves[y][x-i] = 1
                else:
                    if table[y][x-i][1:] == 'w':
                        moves[y][x-i] = 2
                        break
                    else:
                        moves[y][x-i] = 3
                        break
            for i in range(1, 8):
                if x+i > 7: break
                if table[y][x+i] == 0: moves[y][x+i] = 1
                else:
                    if table[y][x+i][1:] == 'w':
                        moves[y][x+i] = 2
                        break
                    else:
                        moves[y][x+i] = 3
                        break
        case 'Rw':
            for i in range(1, 7):
                if y-i < 0: break
                if table[y-i][x] == 0: moves[y-i][x] = 1
                else:
                    if table[y-i][x][1:] == 'b':
                        moves[y-i][x] = 2
                        break
                    else:
                        moves[y-i][x] = 3
                        break
            for i in range(1, 7):
                if y+i > 7: break
                if table[y+i][x] == 0: moves[y+i][x] = 1
                else:
                    if table[y+i][x][1:] == 'b':
                        moves[y+i][x] = 2
                        break
                    else:
                        moves[y+i][x] = 3
                        break
            for i in range(1, 7):
                if x-i < 0: break
                if table[y][x-i] == 0: moves[y][x-i] = 1
                else:
                    if table[y][x-i][1:] == 'b':
                        moves[y][x-i] = 2
                        break
                    else:
                        moves[y][x-i] = 3
                        break
            for i in range(1, 7):
                if x+i > 7: break
                if table[y][x+i] == 0: moves[y][x+i] = 1
                else:
                    if table[y][x+i][1:] == 'b':
                        moves[y][x+i] = 2
                        break
                    else:
                        moves[y][x+i] = 3
                        break
        case 'Cb':
            if y+2 < 8 and x+1 != 8:
                if table[y+2][x+1] == 0:
                    moves[y+2][x+1] = 1
                elif table[y+2][x+1][1:] == 'w':
                    moves[y+2][x+1] = 2
                else: moves[y+2][x+1] = 3
            if y+2 < 8 and x-1 != -1:
                if table[y+2][x-1] == 0:
                    moves[y+2][x-1] = 1
                elif table[y+2][x-1][1:] == 'w':
                    moves[y+2][x-1] = 2
                else: moves[y+2][x-1] = 3
            if y-2 > -1 and x+1 != 8:
                if table[y-2][x+1] == 0:
                    moves[y-2][x+1] = 1
                elif table[y-2][x+1][1:] == 'w':
                    moves[y-2][x+1] = 2
                else: moves[y-2][x+1] = 3
            if y-2 > -1 and x-1 != -1:
                if table[y-2][x-1] == 0:
                    moves[y-2][x-1] = 1
                elif table[y-2][x-1][1:] == 'w':
                    moves[y-2][x-1] = 2
                else: moves[y-2][x-1] = 3
            if y+1 != 8 and x+2 < 8:
                if table[y+1][x+2] == 0:
                    moves[y+1][x+2] = 1
                elif table[y+1][x+2][1:] == 'w':
                    moves[y+1][x+2] = 2
                else: moves[y+1][x+2] = 3
            if y-1 != -1 and x+2 < 8:
                if table[y-1][x+2] == 0:
                    moves[y-1][x+2] = 1
                elif table[y-1][x+2][1:] == 'w':
                    moves[y-1][x+2] = 2
                else: moves[y-1][x+2] = 3
            if y+1 != 8 and x-2 > -1:
                if table[y+1][x-2] == 0:
                    moves[y+1][x-2] = 1
                elif table[y+1][x-2][1:] == 'w':
                    moves[y+1][x-2] = 2
                else: moves[y+1][x-2] = 3
            if y-1 != -1 and x-2 > -1:
                if table[y-1][x-2] == 0:
                    moves[y-1][x-2] = 1
                elif table[y-1][x-2][1:] == 'w':
                    moves[y-1][x-2] = 2
                else: moves[y-1][x-2] = 3
        case 'Cw':
            if y+2 < 8 and x+1 != 8:
                if table[y+2][x+1] == 0:
                    moves[y+2][x+1] = 1
                elif table[y+2][x+1][1:] == 'b':
                    moves[y+2][x+1] = 2
                else: moves[y+2][x+1] = 3
            if y+2 < 8 and x-1 != -1:
                if table[y+2][x-1] == 0:
                    moves[y+2][x-1] = 1
                elif table[y+2][x-1][1:] == 'b':
                    moves[y+2][x-1] = 2
                else: moves[y+2][x-1] = 3
            if y-2 > -1 and x+1 != 8:
                if table[y-2][x+1] == 0:
                    moves[y-2][x+1] = 1
                elif table[y-2][x+1][1:] == 'b':
                    moves[y-2][x+1] = 2
                else: moves[y-2][x+1] = 3
            if y-2 > -1 and x-1 != -1:
                if table[y-2][x-1] == 0:
                    moves[y-2][x-1] = 1
                elif table[y-2][x-1][1:] == 'b':
                    moves[y-2][x-1] = 2
                else: moves[y-2][x-1] = 3
            if y+1 != 8 and x+2 < 8:
                if table[y+1][x+2] == 0:
                    moves[y+1][x+2] = 1
                elif table[y+1][x+2][1:] == 'b':
                    moves[y+1][x+2] = 2
                else: moves[y+1][x+2] = 3
            if y-1 != -1 and x+2 < 8:
                if table[y-1][x+2] == 0:
                    moves[y-1][x+2] = 1
                elif table[y-1][x+2][1:] == 'b':
                    moves[y-1][x+2] = 2
                else: moves[y-1][x+2] = 3
            if y+1 != 8 and x-2 > -1:
                if table[y+1][x-2] == 0:
                    moves[y+1][x-2] = 1
                elif table[y+1][x-2][1:] == 'b':
                    moves[y+1][x-2] = 2
                else: moves[y+1][x-2] = 3
            if y-1 != -1 and x-2 > -1:
                if table[y-1][x-2] == 0:
                    moves[y-1][x-2] = 1
                elif table[y-1][x-2][1:] == 'b':
                    moves[y-1][x-2] = 2
                else: moves[y-1][x-2] = 3
        case 'Bb':
            for i in range(1, 8):
                if y-i < 0 or x-i < 0: break
                if table[y-i][x-i] == 0: moves[y-i][x-i] = 1
                else:
                    if table[y-i][x-i][1:] == 'w':
                        moves[y-i][x-i] = 2
                        break
                    else:
                        moves[y-i][x-i] = 3
                        break
            for i in range(1, 8):
                if y+i > 7 or x+i > 7: break
                if table[y+i][x+i] == 0: moves[y+i][x+i] = 1
                else:
                    if table[y+i][x+i][1:] == 'w':
                        moves[y+i][x+i] = 2
                        break
                    else:
                        moves[y+i][x+i] = 3
                        break
            for i in range(1, 8):
                if x-i < 0 or y+i > 7: break
                if table[y+i][x-i] == 0: moves[y+i][x-i] = 1
                else:
                    if table[y+i][x-i][1:] == 'w':
                        moves[y+i][x-i] = 2
                        break
                    else:
                        moves[y+i][x-i] = 3
                        break
            for i in range(1, 8):
                if x+i > 7 or y-i < 0: break
                if table[y-i][x+i] == 0: moves[y-i][x+i] = 1
                else:
                    if table[y-i][x+i][1:] == 'w':
                        moves[y-i][x+i] = 2
                        break
                    else:
                        moves[y-i][x+i] = 3
                        break
        case 'Bw':
            for i in range(1, 8):
                if y-i < 0 or x-i < 0: break
                if table[y-i][x-i] == 0: moves[y-i][x-i] = 1
                else:
                    if table[y-i][x-i][1:] == 'b':
                        moves[y-i][x-i] = 2
                        break
                    else:
                        moves[y-i][x-i] = 3
                        break
            for i in range(1, 8):
                if y+i > 7 or x+i > 7: break
                if table[y+i][x+i] == 0: moves[y+i][x+i] = 1
                else:
                    if table[y+i][x+i][1:] == 'b':
                        moves[y+i][x+i] = 2
                        break
                    else:
                        moves[y+i][x+i] = 3
                        break
            for i in range(1, 8):
                if x-i < 0 or y+i > 7: break
                if table[y+i][x-i] == 0: moves[y+i][x-i] = 1
                else:
                    if table[y+i][x-i][1:] == 'b':
                        moves[y+i][x-i] = 2
                        break
                    else:
                        moves[y+i][x-i] = 3
                        break
            for i in range(1, 8):
                if x+i > 7 or y-i < 0: break
                if table[y-i][x+i] == 0: moves[y-i][x+i] = 1
                else:
                    if table[y-i][x+i][1:] == 'b':
                        moves[y-i][x+i] = 2
                        break
                    else:
                        moves[y-i][x+i] = 3
                        break
        case 'Qb':
            for i in range(1, 8):
                if y-i < 0: break
                if table[y-i][x] == 0: moves[y-i][x] = 1
                else:
                    if table[y-i][x][1:] == 'w':
                        moves[y-i][x] = 2
                        break
                    else:
                        moves[y-i][x] = 3
                        break
            for i in range(1, 8):
                if y+i > 7: break
                if table[y+i][x] == 0: moves[y+i][x] = 1
                else:
                    if table[y+i][x][1:] == 'w':
                        moves[y+i][x] = 2
                        break
                    else:
                        moves[y+i][x] = 3
                        break
            for i in range(1, 8):
                if x-i < 0: break
                if table[y][x-i] == 0: moves[y][x-i] = 1
                else:
                    if table[y][x-i][1:] == 'w':
                        moves[y][x-i] = 2
                        break
                    else:
                        moves[y][x-i] = 3
                        break
            for i in range(1, 8):
                if x+i > 7: break
                if table[y][x+i] == 0: moves[y][x+i] = 1
                else:
                    if table[y][x+i][1:] == 'w':
                        moves[y][x+i] = 2
                        break
                    else:
                        moves[y][x+i] = 3
                        break
            for i in range(1, 8):
                if y-i < 0 or x-i < 0: break
                if table[y-i][x-i] == 0: moves[y-i][x-i] = 1
                else:
                    if table[y-i][x-i][1:] == 'w':
                        moves[y-i][x-i] = 2
                        break
                    else:
                        moves[y-i][x-i] = 3
                        break
            for i in range(1, 8):
                if y+i > 7 or x+i > 7: break
                if table[y+i][x+i] == 0: moves[y+i][x+i] = 1
                else:
                    if table[y+i][x+i][1:] == 'w':
                        moves[y+i][x+i] = 2
                        break
                    else:
                        moves[y+i][x+i] = 3
                        break
            for i in range(1, 8):
                if x-i < 0 or y+i > 7: break
                if table[y+i][x-i] == 0: moves[y+i][x-i] = 1
                else:
                    if table[y+i][x-i][1:] == 'w':
                        moves[y+i][x-i] = 2
                        break
                    else:
                        moves[y+i][x-i] = 3
                        break
            for i in range(1, 8):
                if x+i > 7 or y-i < 0: break
                if table[y-i][x+i] == 0: moves[y-i][x+i] = 1
                else:
                    if table[y-i][x+i][1:] == 'w':
                        moves[y-i][x+i] = 2
                        break
                    else:
                        moves[y-i][x+i] = 3
                        break
        case 'Qw':
            for i in range(1, 8):
                if y-i < 0: break
                if table[y-i][x] == 0: moves[y-i][x] = 1
                else:
                    if table[y-i][x][1:] == 'b':
                        moves[y-i][x] = 2
                        break
                    else:
                        moves[y-i][x] = 3
                        break
            for i in range(1, 8):
                if y+i > 7: break
                if table[y+i][x] == 0: moves[y+i][x] = 1
                else:
                    if table[y+i][x][1:] == 'b':
                        moves[y+i][x] = 2
                        break
                    else:
                        moves[y+i][x] = 3
                        break
            for i in range(1, 8):
                if x-i < 0: break
                if table[y][x-i] == 0: moves[y][x-i] = 1
                else:
                    if table[y][x-i][1:] == 'b':
                        moves[y][x-i] = 2
                        break
                    else:
                        moves[y][x-i] = 3
                        break
            for i in range(1, 8):
                if x+i > 7: break
                if table[y][x+i] == 0: moves[y][x+i] = 1
                else:
                    if table[y][x+i][1:] == 'b':
                        moves[y][x+i] = 2
                        break
                    else:
                        moves[y][x+i] = 3
                        break
            for i in range(1, 8):
                if y-i < 0 or x-i < 0: break
                if table[y-i][x-i] == 0: moves[y-i][x-i] = 1
                else:
                    if table[y-i][x-i][1:] == 'b':
                        moves[y-i][x-i] = 2
                        break
                    else:
                        moves[y-i][x-i] = 3
                        break
            for i in range(1, 8):
                if y+i > 7 or x+i > 7: break
                if table[y+i][x+i] == 0: moves[y+i][x+i] = 1
                else:
                    if table[y+i][x+i][1:] == 'b':
                        moves[y+i][x+i] = 2
                        break
                    else:
                        moves[y+i][x+i] = 3
                        break
            for i in range(1, 8):
                if x-i < 0 or y+i > 7: break
                if table[y+i][x-i] == 0: moves[y+i][x-i] = 1
                else:
                    if table[y+i][x-i][1:] == 'b':
                        moves[y+i][x-i] = 2
                        break
                    else:
                        moves[y+i][x-i] = 3
                        break
            for i in range(1, 8):
                if x+i > 7 or y-i < 0: break
                if table[y-i][x+i] == 0: moves[y-i][x+i] = 1
                else:
                    if table[y-i][x+i][1:] == 'b':
                        moves[y-i][x+i] = 2
                        break
                    else:
                        moves[y-i][x+i] = 3
                        break
        case 'Kb':
            if alt:
                if y-1 != -1: moves[y-1][x] = 1
                if y+1 != 8: moves[y+1][x] = 1
                if x-1 != -1: moves[y][x-1] = 1
                if x+1 != 8: moves[y][x+1] = 1
                if y-1 != -1 and x+1 != 8: moves[y-1][x+1] = 1
                if y+1 != 8 and x-1 != -1: moves[y+1][x-1] = 1
                if y-1 != -1 and x-1 != -1: moves[y-1][x-1] = 1
                if y+1 != 8 and x+1 != 8: moves[y+1][x+1] = 1
                return
            temp_moves = [[0]*8 for _ in range(8)]
            for j in range(8):
                for i in range(8):
                    if table[j][i] != 0 and table[j][i][1:] == 'w':
                        show_allowed(i, j, True)
            if y-1 != -1 and moves[y-1][x] != 1 and moves[y-1][x] != 3:
                if table[y-1][x] == 0:
                    temp_moves[y-1][x] = 1
                elif table[y-1][x][1:] == 'w':
                    temp_moves[y-1][x] = 2
            if y+1 != 8 and moves[y+1][x] != 1 and moves[y+1][x] != 3:
                if table[y+1][x] == 0:
                    temp_moves[y+1][x] = 1
                elif table[y+1][x][1:] == 'w':
                    temp_moves[y+1][x] = 2
            if x-1 != -1 and moves[y][x-1] != 1 and moves[y][x-1] != 3:
                if table[y][x-1] == 0:
                    temp_moves[y][x-1] = 1
                elif table[y][x-1][1:] == 'w':
                    temp_moves[y][x-1] = 2
            if x+1 != 8 and moves[y][x+1] != 1 and moves[y][x+1] != 3:
                if table[y][x+1] == 0:
                    temp_moves[y][x+1] = 1
                elif table[y][x+1][1:] == 'w':
                    temp_moves[y][x+1] = 2
            if y-1 != -1 and x+1 != 8 and moves[y-1][x+1] != 1 and moves[y-1][x+1] != 3:
                if table[y-1][x+1] == 0:
                    temp_moves[y-1][x+1] = 1
                elif table[y-1][x+1][1:] == 'w':
                    temp_moves[y-1][x+1] = 2
            if y+1 != 8 and x-1 != -1 and moves[y+1][x-1] != 1 and moves[y+1][x-1] != 3:
                if table[y+1][x-1] == 0:
                    temp_moves[y+1][x-1] = 1
                elif table[y+1][x-1][1:] == 'w':
                    temp_moves[y+1][x-1] = 2
            if y-1 != -1 and x-1 != -1 and moves[y-1][x-1] != 1 and moves[y-1][x-1] != 3:
                if table[y-1][x-1] == 0:
                    temp_moves[y-1][x-1] = 1
                elif table[y-1][x-1][1:] == 'w':
                    temp_moves[y-1][x-1] = 2
            if y+1 != 8 and x+1 != 8 and moves[y+1][x+1] != 1 and moves[y+1][x+1] != 3:
                if table[y+1][x+1] == 0:
                    temp_moves[y+1][x+1] = 1
                elif table[y+1][x+1][1:] == 'w':
                    temp_moves[y+1][x+1] = 2
            moves = [[0]*8 for _ in range(8)]
            moves = temp_moves
        case 'Kw':
            if alt:
                if y-1 != -1: moves[y-1][x] = 1
                if y+1 != 8: moves[y+1][x] = 1
                if x-1 != -1: moves[y][x-1] = 1
                if x+1 != 8: moves[y][x+1] = 1
                if y-1 != -1 and x+1 != 8: moves[y-1][x+1] = 1
                if y+1 != 8 and x-1 != -1: moves[y+1][x-1] = 1
                if y-1 != -1 and x-1 != -1: moves[y-1][x-1] = 1
                if y+1 != 8 and x+1 != 8: moves[y+1][x+1] = 1
                return
            temp_moves = [[0]*8 for _ in range(8)]
            for j in range(8):
                for i in range(8):
                    if table[j][i] != 0 and table[j][i][1:] == 'b':
                        #print(table[j][i])
                        show_allowed(i, j, True)
            #print(moves)
            if y-1 != -1 and moves[y-1][x] != 1 and moves[y-1][x] != 3:
                if table[y-1][x] == 0:
                    temp_moves[y-1][x] = 1
                elif table[y-1][x][1:] == 'b':
                    temp_moves[y-1][x] = 2
            if y+1 != 8 and moves[y+1][x] != 1 and moves[y+1][x] != 3:
                if table[y+1][x] == 0:
                    temp_moves[y+1][x] = 1
                elif table[y+1][x][1:] == 'b':
                    temp_moves[y+1][x] = 2
            if x-1 != -1 and moves[y][x-1] != 1 and moves[y][x-1] != 3:
                if table[y][x-1] == 0:
                    temp_moves[y][x-1] = 1
                elif table[y][x-1][1:] == 'b':
                    temp_moves[y][x-1] = 2
            if x+1 != 8 and moves[y][x+1] != 1 and moves[y][x+1] != 3:
                if table[y][x+1] == 0:
                    temp_moves[y][x+1] = 1
                elif table[y][x+1][1:] == 'b':
                    temp_moves[y][x+1] = 2
            if y-1 != -1 and x+1 != 8 and moves[y-1][x+1] != 1 and moves[y-1][x+1] != 3:
                if table[y-1][x+1] == 0:
                    temp_moves[y-1][x+1] = 1
                elif table[y-1][x+1][1:] == 'b':
                    temp_moves[y-1][x+1] = 2
            if y+1 != 8 and x-1 != -1 and moves[y+1][x-1] != 1 and moves[y+1][x-1] != 3:
                if table[y+1][x-1] == 0:
                    temp_moves[y+1][x-1] = 1
                elif table[y+1][x-1][1:] == 'b':
                    temp_moves[y+1][x-1] = 2
            if y-1 != -1 and x-1 != -1 and moves[y-1][x-1] != 1 and moves[y-1][x-1] != 3:
                if table[y-1][x-1] == 0:
                    temp_moves[y-1][x-1] = 1
                elif table[y-1][x-1][1:] == 'b':
                    temp_moves[y-1][x-1] = 2
            if y+1 != 8 and x+1 != 8 and moves[y+1][x+1] != 1 and moves[y+1][x+1] != 3:
                if table[y+1][x+1] == 0:
                    temp_moves[y+1][x+1] = 1
                elif table[y+1][x+1][1:] == 'b':
                    temp_moves[y+1][x+1] = 2
            moves = [[0]*8 for _ in range(8)]
            moves = temp_moves

def check_if_king_atacked(side):
    global moves, kingb_index, kingw_index
    temp = moves
    moves = [[0]*8 for _ in range(8)]
    for j in range(8):
        for i in range(8):
            if table[j][i] != 0 and table[j][i][1:] == side:
                show_allowed(i, j, True)
                if side == 'w':
                    if moves[kingb_index[0]][kingb_index[1]] == 2:
                        moves = temp
                        return j, i
                else:
                    if moves[kingw_index[0]][kingw_index[1]] == 2:
                        moves = temp
                        return j, i
    moves = temp
    return None

changer = {'b':'w',
           'w':'b'}
def check_if_mate(side):
    global moves, table, temp_kingb, temp_kingw, kingb_index, kingw_index
    attacker = check_if_king_atacked(side)
    moves = [[0]*8 for _ in range(8)]
    #print(attacker)
    if attacker == None:
        #print('False1')
        return False
    show_allowed(attacker[1], attacker[0], alt=True)
    attacker_moves = moves
    #print(attacker_moves)
    moves = [[0]*8 for _ in range(8)]
    for j in range(8):
        for i in range(8):
            if table[j][i] != 0 and table[j][i][1:] == changer[side]:
                show_allowed(i, j, alt=True)
                selected_moves = moves
                moves = [[0]*8 for _ in range(8)]
                if selected_moves[attacker[0]][attacker[1]] == 2:
                    table[attacker[0]][attacker[1]], table[j][i] = table[j][i], table[attacker[0]][attacker[1]]
                    temp_figure = table[j][i]
                    table[j][i] = 0
                    attackert = check_if_king_atacked(side)
                    moves = [[0]*8 for _ in range(8)]
                    table[attacker[0]][attacker[1]], table[j][i] = table[j][i], table[attacker[0]][attacker[1]]
                    table[attacker[0]][attacker[1]] = temp_figure
                    if attackert == None:
                        #print('False2')
                        return False
                for n in range(8):
                    for m in range(8):
                        if attacker_moves[n][m] == selected_moves[n][m] == 1:
                            #print(n, m)
                            #print(j, i)
                            table[n][m], table[j][i] = table[j][i], table[n][m]
                            temp_figure = table[j][i]
                            table[j][i] = 0
                            if table[n][m] == 'Kb':
                                temp_kingb = kingb_index
                                kingb_index = (n, m)
                            elif table[n][m] == 'Kw':
                                temp_kingw = kingw_index
                                kingw_index = (n, m)
                            #print(f'kingb:{kingb_index}')
                            attackert = check_if_king_atacked(side)
                            #print(f'attackert{attackert}')
                            moves = [[0]*8 for _ in range(8)]
                            table[n][m], table[j][i] = table[j][i], table[n][m]
                            table[n][m] = temp_figure
                            if table[j][i] == 'Kb':
                                kingb_index = temp_kingb
                            elif table[j][i] == 'Kw':
                                kingw_index = temp_kingw
                            if attackert == None:
                                #print('False3')
                                return False
    moves = [[0]*8 for _ in range(8)]
    return True








table = [
         ['Rb', 'Cb', 'Bb', 'Qb', 'Kb', 'Bb', 'Cb', 'Rb'],
         ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
         [ 0,    0,    0,    0,    0,    0,    0,    0  ],
         [ 0,    0,    0,    0,    0,    0,    0,    0  ],
         [ 0,    0,    0,    0,    0,    0,    0,    0  ],
         [ 0,    0,    0,    0,    0,    0,    0,    0  ],
         ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
         ['Rw', 'Cw', 'Bw', 'Qw', 'Kw', 'Bw', 'Cw', 'Rw']
         ]


moves = [[0]*8 for _ in range(8)]


#initialize
pygame.init()

#window
screen = pygame.display.set_mode((720, 720), RESIZABLE)
x, y = 720, 720
size = min(x, y)
square_size = size/8
pygame.display.set_caption("Chess")
draw_table()
pygame.display.update()

#gameloopp
end = 0
running = True
last_pressed = (-1, -1)
kingb_index = (0, 4)
temp_kingb = (0, 4)
kingw_index = (7, 4)
temp_kingw = (7, 4)
order = 0
orders = {'b':1,
    'w':0}
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if end != 0:
                continue
                if screen.get_size() != (x, y):
                    x, y = screen.get_size()
                    size = min(x, y)
                    square_size = size/8
                    draw_table()
                    pygame.display.update()
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if x > y:
                            mouse_x = int((mouse_x-(x-y)/2)//(size/8))
                            mouse_y = int(mouse_y//(size/8))
                        else:
                            mouse_x = int(mouse_x//(size/8))
                            mouse_y = int((mouse_y-(y-x)/2)//(size/8))
                            if moves[mouse_y][mouse_x] != 0:
                                table[mouse_y][mouse_x], table[last_pressed[0]][last_pressed[1]] = table[last_pressed[0]][last_pressed[1]], table[mouse_y][mouse_x]
                                temp_figure = table[last_pressed[0]][last_pressed[1]]
                                table[last_pressed[0]][last_pressed[1]] = 0
                                if table[mouse_y][mouse_x] == 'Kb':
                                    temp_kingb = kingb_index
                                    kingb_index = (mouse_y, mouse_x)
                                elif table[mouse_y][mouse_x] == 'Kw':
                                    temp_kingw = kingw_index
                                    kingw_index = (mouse_y, mouse_x)

            if table[mouse_y][mouse_x][1:] == 'b':
                attacker = check_if_king_atacked('w')
                if attacker != None:
                    table[last_pressed[0]][last_pressed[1]] = temp_figure
                    table[mouse_y][mouse_x], table[last_pressed[0]][last_pressed[1]] = table[last_pressed[0]][last_pressed[1]], table[mouse_y][mouse_x]
                    kingb_index = temp_kingb
                    continue
            else:
                attacker = check_if_king_atacked('b')
                if attacker != None:
                    table[last_pressed[0]][last_pressed[1]] = temp_figure
                    table[mouse_y][mouse_x], table[last_pressed[0]][last_pressed[1]] = table[last_pressed[0]][last_pressed[1]], table[mouse_y][mouse_x]
                    kingw_index = temp_kingw
                    continue

            table[last_pressed[0]][last_pressed[1]] = 0
            moves = [[0]*8 for _ in range(8)]

            if table[mouse_y][mouse_x][1:] == 'b':
                show_allowed(kingw_index[1], kingw_index[0], False)
                if moves == [[0]*8 for _ in range(8)]:
                    if check_if_mate('b'):
                        end = 1
                else: moves = [[0]*8 for _ in range(8)]

            else:
                show_allowed(kingb_index[1], kingb_index[0], False)
                if moves == [[0]*8 for _ in range(8)]:
                    if check_if_mate('w'):
                        end = 2
                else: moves = [[0]*8 for _ in range(8)]

            order += 1
                    elif (mouse_y, mouse_x) == last_pressed:
                        moves = [[0]*8 for _ in range(8)]
                        last_pressed = (-1, -1)
                    elif table[mouse_y][mouse_x] != 0:
                        if orders[table[mouse_y][mouse_x][1:]] == order%2:
                            last_pressed = (mouse_y, mouse_x)
                            moves = [[0]*8 for _ in range(8)]
                            #print(mouse_y, mouse_x)
                            show_allowed(mouse_x, mouse_y, False)
                            #print(moves)
                            draw_table()
                            pygame.display.update()
                            pygame.time.delay(50)
                            if end == 1:
                                Font = pygame.font.SysFont('chalkduster.ttf', size//16)
                                text = Font.render('Black won', True, (23, 23, 23))
                                textRect = text.get_rect()
                                textRect.center = (size/2, size/2)
                                screen.blit(text, textRect)
                                pygame.display.update()
                            elif end == 2:
                                Font = pygame.font.SysFont('chalkduster.ttf', size//16)
                                text = Font.render('White won', True, (195, 195, 195))
                                textRect = text.get_rect()
                                textRect.center = (size/2, size/2)
                                screen.blit(text, textRect)
                                pygame.display.update()



    #draw
    #pygame.display.update()


# Quit Pygame
pygame.quit()
