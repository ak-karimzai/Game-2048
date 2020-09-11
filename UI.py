import pygame, random, sys
from pygame.locals import *
from map_2048 import map_2048

WINDOWHEIGHT = 372
text_color = pygame.Color("#756c63")
BACKGROUNDCOLOR = (251, 248, 239)
FPS = 40

h = 6

RECT_SIZE = (60, 60)

WINDOWWIDTH = int(7*h + 4*RECT_SIZE[0])

map_color = {
    0: ("#cdc1b4", "#756c63", 45),
    2: ("#eee4da", "#756c63", 45),
    4: ("#ede0c8", "#756c63", 45),
    8: ("#f2b179", "#f9f6f2", 45),
    16: ("#f59563", "#f9f6f2", 40),
    32: ("#f67c5f", "#f9f6f2", 40),
    64: ("#f65e3b", "#f9f6f2", 40),
    128: ("#edcf72", "#f9f6f2",35),
    256: ("#edcc61", "#f9f6f2", 35),
    512: ("#e4c02a", "#f9f6f2", 35),
    1024: ("#e2ba13", "#f9f6f2", 30),
    2048: ("#ecc400", "#f9f6f2", 30),
    4096: ("#3d3a33", "#f9f6f2", 30),
}

# Матрица игрового поля
game = map_2048()

butt_press = False

# функция, которая рисует текст
def drawText(text, size, surface, x, y, type, text_color=text_color):
    textobj = pygame.font.SysFont(None, size).render(text, 1, text_color)
    textrect = textobj.get_rect()
    if type == 'c':
        textrect.topleft = (int(x - textrect.width/2), int(y - textrect.height/2))
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def pressent(click, command):
    global butt_press
    
    if click == 1:
            butt_press = True
    if (click == 0)and (butt_press):
        butt_press = False
        if command is not None:
            command()

class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_clr = inactive_color
        self.active_clr = active_color
        
    def draw(self, window, x, y, message, command=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(window, self.inactive_clr, (x, y, self.width, self.height))
        
        if (x <  mouse[0] < x + self.width) and (y <  mouse[1] < y + self.height):
            if click[0] == 1:
                pygame.draw.rect(window, self.active_clr, (x, y, self.width, self.height))

            pressent(click[0], command)
            
        drawText(message, 22, windowSurface, x + self.width/2, y + self.height/2, 'c', (251, 248, 239))

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
    drawText('ИГРА ОКОНЧЕНА', 30, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 20, 'c')
    drawText('Нажмите клавишу любую клавишу', 21, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 10, 'c')
    drawText('чтобы начать заново.', 21, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 30, 'c')
    pygame.display.update()
    waitForPlayerToPressKey()
    game.reset()



# запустить pygame, создать основное окно
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('2048')

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
    drawText('Счет: %s' % (score), 30, windowSurface, 15, 10, '')
    drawText('Рекорд: %s' % (topScore), 30, windowSurface, 15, 40, '')

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
        game_over_text()

    pygame.draw.rect(windowSurface, (187, 173, 160), (h, rect_y - h, RECT_SIZE[0]*4 + h*5, RECT_SIZE[1]*4 + h*5))
    
    button = Button(70, 30, (144, 122, 99), (122, 102, 79))
    
    # Цикл, рисующий клетки игрового поля
    for i in range(4):
        rect_x = h*2
        for j in range(4):
            number = game.data[i][j]
            if number < 4096:
                rect_color = pygame.Color(map_color[number][0])
                numb_color = pygame.Color(map_color[number][1])
                numb_size = map_color[number][2]
            else:
                rect_color = pygame.Color(map_color[4096][0])
                numb_color = pygame.Color(map_color[4096][1])
                numb_size = map_color[4096][2]

            pygame.draw.rect(windowSurface, rect_color, (rect_x, rect_y, RECT_SIZE[0], RECT_SIZE[1]))

            if (game.data[i][j] != 0):
                drawText(str(number), 30, windowSurface, rect_x + RECT_SIZE[0]/2, rect_y + RECT_SIZE[1]/2, 'c', numb_color)

            rect_x += RECT_SIZE[0] + h
        rect_y += RECT_SIZE[0] + h

    button.draw(windowSurface, 200, 30, 'сброс', game.reset)

    pygame.display.update()

    mainClock.tick(FPS)

    
'''
drawText('ИГРА ОКОНЧЕНА', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Нажмите клавишу "a" чтобы начать заново.', font, windowSurface, (WINDOWWIDTH / 3 - 140), (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()
'''

