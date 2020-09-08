import pygame, random, sys
from pygame.locals import *
from map_2048 import map_2048

<<<<<<< HEAD
WINDOWHEIGHT = 500
=======
WINDOWHEIGHT = 380
>>>>>>> 1dc03eb3e7e1530deeb98d4751a66b7beba17162
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (192, 192, 192)
FPS = 40

h = 10

<<<<<<< HEAD
RECT_SIZE = (80, 80)
=======
RECT_SIZE = (60, 60)
>>>>>>> 1dc03eb3e7e1530deeb98d4751a66b7beba17162

WINDOWWIDTH = int(5*h + 4*RECT_SIZE[0])

# Матрица игрового поля
game = map_2048()
'''
game.data = [[4, 8, 2, 2],
            [8, 2, 32, 2 ],
            [4, 64, 4, 64], 
            [16, 128, 16, 4]]
'''

def matf(x):
    if x > 255:
        return 0
    if x < 0:
        return 0
    return x

def terminate():
    pygame.quit()
    sys.exit()

def add_to_file(x):
    file = open("2048.txt", "w")
    file.write(str(x))
    file.close()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Выход из программы
                    terminate()
                return

def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    windowSurface.blit(over_text, (int(WINDOWWIDTH / 2), int(WINDOWWIDTH / 2)))

# функция, которая рисует текст
def drawText(text, font, surface, x, y, type):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    if type == 'c':
        textrect.topleft = (int(x - textrect.width/2), int(y - textrect.height/2))
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# запустить pygame, создать основное окно
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('2048')

font = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 21)

# Переменные, в которых хранятся счет и рекорд
file = open("2048.txt", "r")
topScore = int(file.read())
file.close()
score = 0

while True: # the game loop runs while the game part is playing
    windowSurface.fill(BACKGROUNDCOLOR)
    rect_y = 100
    score = game.score
    if score > topScore:
        topScore = score
    drawText('Счет: %s' % (score), font, windowSurface, 15, 10, '')
    drawText('Рекорд: %s' % (topScore), font, windowSurface, 15, 40, '')

    for event in pygame.event.get():
        if event.type == QUIT:
            add_to_file(topScore)
            terminate()
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if game.left():
                    game.fill2()

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if game.right():
                    game.fill2()

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if game.up():
                    game.fill2()

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if game.down():
                    game.fill2()
                    
    if game.is_gameover():
        drawText('ИГРА ОКОНЧЕНА', font, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 20, 'c')
        drawText('Нажмите клавишу любую клавишу', font2, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 10, 'c')
        drawText('чтобы начать заново.', font2, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 30, 'c')
        pygame.display.update()
        waitForPlayerToPressKey()
        game.reset()

    pygame.draw.rect(windowSurface, (60, 60, 60), (int(h/2), int(rect_y - h/2), int(RECT_SIZE[0]*4 + h*4), int(RECT_SIZE[1]*4) + int(h*4)))
        
    # Цикл, рисующий клетки игрового поля
    '''for i in game.data:
        for j in i:
            print(j, end = " ")
        print()'''
    
    for i in range(4):
        rect_x = h
        for j in range(4):
            rect_color = (255, 255, 255)
            if game.data[i][j] != 0:
                rect_color = (255, 255, matf(255 - game.data[i][j]*10))
            if (rect_color[2] == 0):
                rect_color = (255, matf(255 - game.data[i][j]), 0)
            if (rect_color[1] == 0):
                rect_color = (matf(255 - game.data[i][j]/10), 0, 0)

            if (game.data[i][j] == 0):
                rect_color = (128, 128, 128)
                pygame.draw.rect(windowSurface, rect_color, (rect_x, rect_y, RECT_SIZE[0], RECT_SIZE[1]))
            else:
                pygame.draw.rect(windowSurface, rect_color, (rect_x, rect_y, RECT_SIZE[0], RECT_SIZE[1]))
                drawText(str(game.data[i][j]), pygame.font.SysFont(None, 30), windowSurface, rect_x + 27, rect_y + 27, 'c')

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
