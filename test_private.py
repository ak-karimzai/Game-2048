from map_2048 import map_2048

def display_map(map):
    for c in range(map.col):
        for r in range(map.row):
            print(map.data[c][r], end = "  ")
        print()

def main():
    game = map_2048()
    game.reset()

    while True:
        map = game.data
        cell_width = game.col

        print("Score: ", game.get_score())
        print('\n'.join(
            ' '.join(
                str(c).rjust(cell_width)
                for c in r
            )
            for r in map
        ))

        if not game.is_gameover:
            print("No available moves left, game over.")
            break

        print("W, A, S, D - move")
        print("Q - exit")

        try:
            c = input("> ")
        except (EOFError, KeyboardInterrupt):
            break

        if c in ('a', 'A'):
            game.left()
            game.fill2()
        elif c in ('d', 'D'):
            game.right()
            game.fill2()
        elif c in ('w', 'W'):
            game.up()
            game.fill2()
        elif c in ('s', 'S'):
            game.down()
            game.fill2()
        elif c in ('q', 'Q'):
            break

    print("Bye!")


if __name__ == '__main__':
    main()