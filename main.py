import random
import math


# Этот класс является классом инкапсулированным модулем карты

class map_2048():

    def reset(self):
        # Сбросить данные игры
        self.row = 4
        self.col = 4
        self.data = [
                    [0 for i in range(self.col)]
                         for j in range(self.row)
                    ]
        # self.data = [[x + 4 * y for x in range(self.__col)]
        #              for y in range(self.__row)]
        # self.data = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


        self.fill2()
        self.fill2()
    
    def __init__(self):
        self.reset()

    # Получить количество позиций без номеров
    def get_space_count(self):
        #Получить количество квадратов без чисел        
        count = 0

        for r in self.data:
            count += r.count(0)
       
        return count

    # Получить счет игры.
    def get_score(self):
        s = 0
        for r in self.data:
            for c in r:
                s += 0 if c < 4 else c * int((math.log(c, 2) - 1.0))
        return s

    # Заполнит 2 до пустой позиции, если заполнение прошло успешно, 
    # верните True, если оно заполнено, верните False,
    def fill2(self):
        blank_count = self.get_space_count()
        
        if blank_count == 0:
            return False
        
        # Создать случайное местоположение
        pos = random.randrange(0, blank_count)
        offset = 0
        
        for r in self.data:
            for ci in range(self.col):
                if r[ci] == 0:
                    if offset == pos:
                        r[ci] = 2
                        return True
                    offset += 1
    
     # Определить, закончена ли игра
    def is_gameover(self):
        pass
    
    def left(self):
        # moveflag Если цифровой флаг успешно перемещен, если он перемещен, он равен true, 
        # а исходная карта не изменяется, он равен false.
        moveflag = False

        # Переместить все числа влево, чтобы заполнить левое пространство
        for times in range(self.col - 1):
            for r in self.data:
                for c in range(self.col - 1):
                    if r[c] == 0:
                        moveflag = True
                        r[c] = r[c + 1]
                        r[c + 1] = 0
        
        # Определить, есть ли столкновение, если есть столкновение, объединить, результат 
        # объединения находится слева, а справа - заполнить пространство
        for r in self.data:
            for c in range(self.col - 1):
                if r[c] == r[c + 1]:
                    moveflag = True
                    r[c] *= 2
                    r[c + 1] = 0
        
        # Затем переместите все цифры влево,
        #  чтобы заполнить левое пространство
        for times in range(self.col - 1):
            for r in self.data:
                for c in range(self.col - 1):
                    if r[c] == 0:
                        moveflag = True
                        r[c] = r[c + 1]
                        r[c + 1] = 0
        return moveflag

    # Игра с правым сдвигом
    def right(self):
        #сначала reverse делаем чтобы наш data получиться как left и потом 
        # позвим функции left()             
        for r in self.data:
            r.reverse()

        moveflag = self.left()
        
        # обратно в начальном состояние
        for r in self.data:
            r.reverse()
        
        return moveflag
    
    # Движет Игра вверх
    def up(self):
        pass

    def down(self):
        pass