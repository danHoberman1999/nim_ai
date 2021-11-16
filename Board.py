'''
Daniel Hoberman
CPSC323
Homework #7: Game of Nim Part 2
Update to fix issues with ability to play
finished 11/14/21

Adjusts my initial nim algorithm. Gives it the ability to play against other opponents.
'''


# Defines the player making moves
class Board():

    '''
    Prints the board
    '''
    def print_board(self, state):
        for row, val in enumerate(state):
            print(row +1, " ", end='')
            for num in range(val[0]):
                print("|", end=' ')
            print('\n')

    '''
    Checks to see if the game has reached a game over state
    '''
    def game_over(self, state):
        total = 0
        for row in state:
            total += row[0]
        
        if total == 1:
            return True
        return False
