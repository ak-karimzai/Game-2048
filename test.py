from unittest import TestCase, main
from main import map_2048

class test_map_2048(TestCase):

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
        

if __name__ == '__main__':
    main()