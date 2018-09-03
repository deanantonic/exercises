"""
Maybe you’ve already heard about the simple and addictive game, 2048 (read more about it here). In this task we will look behind the scenes and try to recreate its basic movement functionality.
2048 is played on a simple 4×4 grid with tiles. Player can move tiles left, right, up, and down. If two tiles of the same number collide while moving, they will merge into a tile with the sum value of the two tiles. The resulting tile cannot merge with another tile again in the same move. If we have three tiles of the same number, then first collide tiles which closer to edge in the moving direction (right move - closer to the right edge). Every turn, a new tile will appear in the last empty spot (value 0) on the board with a value of 2. The last empty slot is determined by indexes that are defined in the following order: At the beginning, there's already two numbers on the board.

You are given a game state represented as a 4x4 matrix with numbers that are powers of 2. Players move in a direction (up, down, left, right). You should return the game state after this move.
If the game is won, i.e. 2048 appears on the board, then return the winning matrix: If the game is lose, i.e. nothing change after the player move and there is not a empty spot, then return the losing matrix:

Input: A game state as a list of lists with integers and player's move as a string ('up', 'down', 'left' or 'right').

Output: The game state after player's move as a list of lists with integers or letters.

Preconditions: len(state) == 4
all(len(row) == 4 for row in state)
all(all(x in (0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024) for x in row) for row in state)
"""
win = [['U','W','I','N']]*4
lose = [['G','A','M','E'],['O','V','E','R']]*2
def rotateRight(state):
    return [list(line) for line in zip(*state[::-1])]
def pullLeft(state):
    for i in range(0, 4):
        for j in range(0, 3):
            if state[i][j] != 0:
                for k in range(j+1, 4):
                    if state[i][k] != 0:
                        break
                if state[i][k] == state[i][j]:
                    state[i][j] *= 2
                    state[i][k] = 0
        for j in range(0, 3):
            if state[i][j] == 0:
                for k in range(j+1, 4):
                    if state[i][k] != 0:
                        break
                state[i][j] = state[i][k]
                state[i][k] = 0
    return state
def check(state):
    moved = False
    for i in range(3,-1,-1):
        for j in range(3,-1,-1):
            if not moved and state[i][j] == 0:
                state[i][j] = 2
                moved = True
            if state[i][j] == 2048:
                return win
    if not moved:
        return lose
    return state


def move2048(state, move):
    if move == 'up':
        state = rotateRight(state)
        state = rotateRight(state)
        state = rotateRight(state)
        state = pullLeft(state)
        state = rotateRight(state)
    elif move == 'down':
        state = rotateRight(state)
        state = pullLeft(state)
        state = rotateRight(state)
        state = rotateRight(state)
        state = rotateRight(state)
    elif move == 'left':
        state = pullLeft(state)
    elif move == 'right':
        state = rotateRight(state)
        state = rotateRight(state)
        state = pullLeft(state)
        state = rotateRight(state)
        state = rotateRight(state)
    else:
        pass
    state = check(state)
    return state
