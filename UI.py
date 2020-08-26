import pygame, random, sys
from pygame.locals import *

WINDOWHEIGHT = 360
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (192, 192, 192)
FPS = 40

h = 10

RECT_SIZE = (54, 54)

WINDOWWIDTH = 5*h + 4*RECT_SIZE[0]

# Матрица игрового поля
matr = [[0,0,2,4],
        [2,0,256,32],
        [0,2,64,128],
        [2,8,8,16]]


def matf(x):
    if x > 255:
        return 0
    if x < 0:
        return 0
    return x

def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Выход из программы
                    terminate()
                return

# функция, которая рисует текст
def drawText(text, font, surface, x, y, type):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    if type == 'c':
        textrect.topleft = (x - textrect.width/2, y - textrect.height/2)
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# запустить pygame, создать основное окно
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('2048')

font = pygame.font.SysFont(None, 30)

# Переменные, в которых хранятся счет и рекорд
score = 0
topScore = 0

while True: # the game loop runs while the game part is playing
    windowSurface.fill(BACKGROUNDCOLOR)
    rect_y = 100

    drawText('Счет: %s' % (score), font, windowSurface, 15, 10, '')
    drawText('Рекорд: %s' % (topScore), font, windowSurface, 15, 40, '')

    pygame.draw.rect(windowSurface, (60, 60, 60), (h/2, rect_y - h/2, RECT_SIZE[0]*4 + h*4, RECT_SIZE[1]*4 + h*4))

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

    # Цикл, рисующий клетки игрового поля
    for i in range(4):
        rect_x = h
        for j in range(4):
            rect_color = (255, 255, 255)
            if matr[i][j] != 0:
                rect_color = (255, 255, matf(255 - matr[i][j]*10))
            if (rect_color[2] == 0):
                rect_color = (255, matf(255 - matr[i][j]), 0)
            if (rect_color[1] == 0):
                rect_color = (matf(255 - matr[i][j]/10), 0, 0)

            if (matr[i][j] == 0):
                rect_color = (128, 128, 128)
                pygame.draw.rect(windowSurface, rect_color, (rect_x, rect_y, RECT_SIZE[0], RECT_SIZE[1]))
            else:
                pygame.draw.rect(windowSurface, rect_color, (rect_x, rect_y, RECT_SIZE[0], RECT_SIZE[1]))
                drawText(str(matr[i][j]), pygame.font.SysFont(None, 30), windowSurface, rect_x + 27, rect_y + 27, 'c')

            rect_x += RECT_SIZE[0] + h
        rect_y += RECT_SIZE[0] + h

    pygame.display.update()

    mainClock.tick(FPS)

'''
drawText('ИГРА ОКОНЧЕНА', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Нажмите клавишу "a" чтобы начать заново.', font, windowSurface, (WINDOWWIDTH / 3 - 140), (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()
'''

