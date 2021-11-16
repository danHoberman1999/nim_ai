
from nim_board import nimBoard


# Defines the player making moves
class player(nimBoard):
    def __init__(self, name, state):
        self.player = name
        self.state = state

    '''
    Method used to make player move and check if input is valid.
    '''
    def player_move(self):
        print("Player turn : \n")
        while True:
    
            try:
                num_sticks = int(input('{}, how many sticks to remove? '.format(self.player)))
                stick_pile = int(input('Pick a pile to remove from: '))
            except ValueError:
                print("Hmmm. You entered an invalid value. Try again, {}.".format(self.player))
                continue

            if (num_sticks and stick_pile > 0) and (stick_pile <= len(self.state)):
                if (num_sticks <= self.state[stick_pile -1][0]):
                    if (num_sticks and stick_pile != 0):
                        break
        
            # If not, display this statement
            print("Hmmm. You entered an invalid value. Try again, {}.".format(self.player))
        
        # Update state
        self.state[int(stick_pile) - 1][0] -= int(num_sticks)


    '''
    Method used to keep track of player state.
    '''
    def player_state(self):
        self.print_board(self.state)
        return self.state


    