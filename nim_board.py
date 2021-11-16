
# Defines the player making moves
class nimBoard():

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



    