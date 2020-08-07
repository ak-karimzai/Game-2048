from unittest import TestCase, main
from map_2048 import map_2048

class test_map_2048(TestCase):

    ###Движения
    #left()
    def test_is_combined_left(self):
        start = [
            [1, 1, 0, 0],
            [1, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 0, 1, 1]
        ]

        end = [
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0]
        ]

        board = map_2048()
        board.data = start
        board.left()

        self.assertEqual(end, board.data)

    #right()
    def test_is_combined_right(self):
        start = [
            [0, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 0]
        ]
        end = [
            [0, 0, 0, 2],
            [0, 0, 0, 2],
            [0, 0, 0, 2],
            [0, 0, 0, 2]
        ]

        board = map_2048()
        board.data = start
        board.right()

        self.assertEqual(end, board.data)

    #up()
    def test_is_combined_up(self):
        start = [
            [0, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1]
        ]
        end = [
            [2, 2, 2, 2],
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        board = map_2048()
        board.data = start
        board.up()

        self.assertEqual(end, board.data)

    #down()
    def test_is_combined_down(self):
        start = [
            [1, 0, 1, 1],
            [0, 1, 0, 0],
            [0, 1, 1, 1],
            [1, 1, 0, 1]
        ]
        end = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [2, 2, 2, 2]
        ]

        board = map_2048()
        board.data = start
        board.down()

        self.assertEqual(end, board.data)

    ##Движение не происходит
    #left()
    def test_no_move_left(self):
        start = [
            [2, 4, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 4, 8, 2]
        ]

        board = map_2048()
        board.data = start

        self.assertFalse(board.left())

    #right()
    def test_no_move_right(self):
        start = [
            [0, 4, 2, 4],
            [0, 0, 0, 0],
            [2, 8, 16, 8],
            [2, 4, 8, 2]
        ]

        board = map_2048()
        board.data = start

        self.assertFalse(board.right())

    #up()
    def test_no_move_up(self):
        start = [
            [2, 4, 0, 8],
            [4, 2, 0, 0],
            [0, 8, 0, 0],
            [0, 4, 0, 0]
        ]

        board = map_2048()
        board.data = start

        self.assertFalse(board.up())

    def test_no_move_down(self):
        start = [
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [4, 2, 4, 0],
            [2, 4, 8, 2]
        ]

        board = map_2048()
        board.data = start

        self.assertFalse(board.down())


    ###board utilities
    ##reset()
    def test_reset(self):
        start = [
            [1, 2, 0, 0],
            [0, 2, 2, 1],
            [1, 0, 0, 0],
            [2, 0, 1, 1]
        ]

        board = map_2048()
        board.data = start
        board.reset()

        #после вызова reset() на доске находятся
        #два квадрата с 2, поэтому счёт должен быть 0
        self.assertEqual(board.get_score(), 0)

    ##get_space_count()
    #полностью заполнено
    def test_get_space_count_filled(self):
        start = [
            [1, 2, 4, 1],
            [2, 2, 4, 2],
            [4, 4, 1, 1],
            [2, 4, 2, 1]
        ]
        
        board = map_2048()
        board.data = start

        self.assertEqual(board.get_space_count(), 0)

    #не заполнено
    def test_get_space_count(self):
        start = [
            [0, 2, 4, 1],
            [2, 2, 0, 2],
            [4, 0, 1, 1],
            [0, 0, 2, 1]
        ]
        
        board = map_2048()
        board.data = start

        self.assertEqual(board.get_space_count(), 5)
        
    #пусто
    def test_get_space_count_empty(self):
        start = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        
        board = map_2048()
        board.data = start

        self.assertEqual(board.get_space_count(), 16)

    ##get_score()
    #только малозначные (т.е. return = 0)
    def test_get_score_small(self):
        start = [
            [0, 2, 2, 2],
            [2, 1, 1, 1],
            [0, 2, 2, 2],
            [1, 1, 2, 2]
        ]

        board = map_2048()
        board.data = start

        self.assertEqual(board.get_score(), 0)

    #квадраты с >=4
    def test_get_score_middle(self):
        start = [
            [2, 0, 2, 4],
            [2, 4, 4, 2],
            [1, 2, 4, 2],
            [2, 0, 8, 4]
        ]

        board = map_2048()
        board.data = start

        self.assertEqual(board.get_score(), 36)

    #один квадрат с 1024
    def test_get_score_1024(self):
        start = [
            [0, 2, 1, 1],
            [0, 1, 1, 0],
            [0, 0, 1024, 1],
            [2, 1, 2, 2]
        ]

        board = map_2048()
        board.data = start

        self.assertEqual(board.get_score(), 9216) #1024*(10-1)

    ##fill2()
    #заполненная доска
    def test_fill2_filled(self):
        start = [
            [2, 4, 4, 2],
            [4, 4, 8, 4],
            [4, 8, 16, 2],
            [4, 2, 2, 4]
        ]

        board = map_2048()
        board.data = start

        self.assertFalse(board.fill2())

    #одно свободное место
    def test_fill2_almost_filled(self):
        start = [
            [0, 4, 4, 2],
            [4, 4, 8, 4],
            [4, 8, 16, 2],
            [4, 2, 2, 4]
        ]
        end = [
            [2, 4, 4, 2],
            [4, 4, 8, 4],
            [4, 8, 16, 2],
            [4, 2, 2, 4]
        ]

        board = map_2048()
        board.data = start
        board.fill2()

        self.assertEqual(end, board.data)

    #пустая доска    
    def test_fill2_filled(self):
        start = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        copy = [x[:] for x in start]

        board = map_2048()
        board.data = start
        board.fill2()

        self.assertNotEqual(copy, board.data)

    ##is_gameover()
    #заполнено и ходов нет
    def test_gameover_filled_none(self):
        start = [
            [4, 2, 4, 8],
            [2, 4, 8, 4],
            [4, 16, 4, 8],
            [8, 4, 2, 16]
        ]

        board = map_2048()
        board.data = start

        self.assertTrue(board.is_gameover())

    #заполнено и есть один вертикальный ход
    def test_gameover_vertical(self):
        start = [
            [4, 2, 4, 8],
            [2, 4, 8, 4],
            [4, 16, 4, 8],
            [8, 16, 2, 16]
        ]

        board = map_2048()
        board.data = start

        self.assertFalse(board.is_gameover())

    #заполнено и есть один горизонтальный ход
    def test_gameover_horizontal(self):
        start = [
            [4, 2, 4, 8],
            [2, 4, 8, 4],
            [4, 16, 16, 8],
            [8, 4, 2, 16]
        ]

        board = map_2048()
        board.data = start

        self.assertFalse(board.is_gameover())

    #игра только началась
    def test_gameover_new(self):

        board = map_2048()

        self.assertFalse(board.is_gameover())
        
if __name__ == '__main__':
    main()
