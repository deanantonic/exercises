"""
 Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

x-o-referee

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
"""
from typing import List

def checkio(game_result: List[str]) -> str:

    for i in range(3):
        row = game_result[i]
        if row == "XXX":
            return "X"
        elif row == "OOO":
            return "O"
        else:
            i += 1

    for j in range(3):
        column = game_result[0][j] + game_result[1][j] + game_result[2][j]
        if column == "XXX":
            return "X"
        elif column == "OOO":
            return "O"
        else:
            j += 1

    d1=game_result[0][0] +  game_result[1][1] +  game_result[2][2]
    d2=game_result[2][0] +  game_result[1][1] +  game_result[0][2]
    diagonals=[d1,d2]

    for k in range(2):
        diagonal = diagonals[k]
        if diagonal == "XXX":
            return "X"
        elif diagonal == "OOO":
            return "O"
        else:
            k += 1

    return "D"



if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
