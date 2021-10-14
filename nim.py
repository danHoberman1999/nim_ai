"""
Daniel Hoberman

Description:
Plays a game of nim with Dr. Stewart (my AI). He will win every time.
"""


class Nim():
    def __init__(self):
        self.nim_sticks = [[1],[3],[5],[7]]
        self.player = None
        self.AI = "Dr. Stewart"
        self.current_move = None


    '''
    Gets player name as input to start game.
    '''
    def get_player(self):
        player_name = input("Enter player name: ")
        self.player = player_name
        print(self.player," vs. Dr. Stewart (AI) will begin now!!!!")


    '''
    Method used to print the nim board vertically.
    '''
    def print_board(self):
        for row, val in enumerate(self.nim_sticks):
            print(row +1, " ", end='')
            for num in range(val[0]):
                print("|", end=' ')
            print('\n')


    '''
    Method used to make player move and check if input is valid.
    '''
    def player_move(self):
        self.print_board()
        while True:
    
            try:
                num_sticks = int(input('{}, how many sticks to remove? '.format(self.player)))
                stick_pile = int(input('Pick a pile to remove from: '))
            except ValueError:
                print("Hmmm. You entered an invalid value. Try again, {}.".format(self.player))
                continue

            if (num_sticks and stick_pile > 0) and (stick_pile <= len(self.nim_sticks)):
                if (num_sticks <= self.nim_sticks[stick_pile -1][0]):
                    if (num_sticks and stick_pile != 0):
                        break
        
            # If not, display this statement
            print("Hmmm. You entered an invalid value. Try again, {}.".format(self.player))
        
        # Update state
        self.nim_sticks[int(stick_pile) - 1][0] -= int(num_sticks)
        self.current_move = self.player

        # Keep playing game
        self.print_board()

    '''
    Makes the AI generated move.
    '''
    def make_dr_move(self, col, amount):
        print("Dr. Stewart is making his move now")
        self.nim_sticks[int(col)][0] -= int(amount)
        self.print_board()
        print("The Dr took ", amount, "sticks from pile: ", col +1)
        self.current_move = self.AI



    '''
    Checks to see if the game has reached the end state.
    '''
    def game_over(self):
        total = 0
        for row in self.nim_sticks:
            total += row[0]
        
        if total == 1:
            return True
        return False

    


class Dr_Stewart():
    def __init__(self, nim):
        self.name = "Dr. Stewart"
        self.pile_states = None
        self.nim = nim
        self.even = []
        self.odd = []


    '''
    Keeps track of states off current nim board.
    '''
    def nim_develop_state(self):
        states = []
        first_pile = []
        second_pile = []
        third_pile = []
        fourth_pile = []
        
        first_pile_state = self.nim.nim_sticks[0][0]
        if first_pile_state == 1:
            first_pile.append(1)
        
        second_pile_state = self.nim.nim_sticks[1][0]
        if second_pile_state == 3:
            second_pile.append(1)
            second_pile.append(2)
        elif second_pile_state == 2:
            second_pile.append(2)
        elif second_pile_state == 1:
            second_pile.append(1)


        third_pile_state = self.nim.nim_sticks[2][0]
        if third_pile_state == 5:
            third_pile.append(1)
            third_pile.append(4)
        elif third_pile_state == 4:
            third_pile.append(4)
        elif third_pile_state == 3:
            third_pile.append(1)
            third_pile.append(2)
        elif third_pile_state == 2:
            third_pile.append(2)
        elif third_pile_state == 1:
            third_pile.append(1)


        fourth_pile_state = self.nim.nim_sticks[3][0]
        if fourth_pile_state == 7:
            fourth_pile.append(1)
            fourth_pile.append(2)
            fourth_pile.append(4)
        elif fourth_pile_state == 6:
            fourth_pile.append(2)
            fourth_pile.append(4)
        elif fourth_pile_state == 5:
            fourth_pile.append(1)
            fourth_pile.append(4)
        elif fourth_pile_state == 4:
            fourth_pile.append(4)
        elif fourth_pile_state == 3:
            fourth_pile.append(1)
            fourth_pile.append(2)
        elif fourth_pile_state == 2:
            fourth_pile.append(2)
        elif fourth_pile_state == 1:
            fourth_pile.append(1)

        states.append(first_pile)
        states.append(second_pile)
        states.append(third_pile)
        states.append(fourth_pile)
        self.pile_states = states



    

    '''
    Uses a dictionary to figure out if board has odd state values
    '''
    def nim_dictionary(self):
        even_values = []
        odd_values = []
        nim_dictionary = {}
        for cols in self.pile_states:
            for value in cols:
                if value in nim_dictionary:
                    nim_dictionary[value] += 1        
                elif value not in nim_dictionary:
                    nim_dictionary[value] = 1

        for value in nim_dictionary:
            if nim_dictionary[value] %2 == 0:
                even_values.append([value, nim_dictionary[value]])
            else:
                odd_values.append([value, nim_dictionary[value]])

        self.even = even_values
        self.odd = odd_values

    
    '''
    Depending on number of odd state values uses different algorithm to determine which column and amount to subtract from piles
    '''
    def nim_algorithm(self):
        smallest = 10
        largest = 0
        empty_pile_tracker = 0
        single_pile_tracker = 0
        large_pile_tracker = 0
        col_num = 0
        col_total = 0
        

        # This part still needs work
        for piles in self.nim.nim_sticks:
            if piles[0] > 1:
                large_pile_tracker +=1
            if piles[0] == 0:
                empty_pile_tracker += 1
            if piles[0] == 1:
                single_pile_tracker +=1


        if empty_pile_tracker ==2 and single_pile_tracker ==2:
            for col, piles in enumerate(self.nim.nim_sticks):
                if piles[0] == 1:
                    col_total = piles[0]
                    return col, col_total

        if single_pile_tracker ==3:
            for col, piles in enumerate(self.nim.nim_sticks):
                if piles[0] > 1:
                    col_total = piles[0]
                    return col, col_total


        if single_pile_tracker ==2 and large_pile_tracker ==1:
            for col, piles in enumerate(self.nim.nim_sticks):
                if piles[0] > 1:
                    col_total = piles[0]-1
                    return col, col_total
        
        if empty_pile_tracker == 3:
            for col, piles in enumerate(self.nim.nim_sticks):
                if piles[0] > 1:
                    col_total = piles[0] -1
                    return col, col_total

        if empty_pile_tracker == 2 and single_pile_tracker == 1:
            for col, piles in enumerate(self.nim.nim_sticks):
                if piles[0] >1:
                    col_num = col
                    col_total = piles[0]

            return col_num, col_total

        else:
            if len(self.odd) ==1:
                for col, val in enumerate(self.pile_states):
                    if self.odd[0][0] in val:
                        return col, self.odd[0][0]

            elif len(self.odd) ==2: # find largest item figure out how much to subtract to equal other number
                for val in self.odd:
                    if val[0] > largest:
                        largest = val[0]

                for val in self.odd:
                    if val[0] < smallest:
                        smallest = val[0]

                if largest == 2 and smallest == 1:
                    subtraction_amount = largest+smallest
                else:
                    subtraction_amount = largest-smallest

                for col, val in enumerate(self.pile_states):
                    if largest in val:
                        return col, subtraction_amount


            elif len(self.odd) ==3: # add smallest item with largest item, figure out how much to subtract to equal middle item
                col_tracker = [0,1,2]
                col_largest = None
                col_smallest = None
                for col, val in enumerate(self.odd):
                    if val[0] > largest:
                        largest = val[0]
                        col_largest = col

                for col,val in enumerate(self.odd):
                    if val[0] < smallest:
                        smallest = val[0]
                        col_smallest = col

                col_tracker.remove(col_largest)
                col_tracker.remove(col_smallest)
                middle_col_val = self.odd[col_tracker[0]][0]

                holding_number = smallest + largest

                subtraction_amount = holding_number - middle_col_val

                for col, val in enumerate(self.pile_states):
                    if largest in val and smallest in val and middle_col_val in val:
                        subtraction_amount = val[0] + val[1] + val[2]
                        return col, subtraction_amount
                    elif largest in val:
                        return col, subtraction_amount

            


            
def main():
    nim = Nim()
    nim.get_player()
    while not nim.game_over():
        nim.player_move()
        stew = Dr_Stewart(nim)
        stew.nim_develop_state()
        stew.nim_dictionary()
        col, amount = stew.nim_algorithm()
        nim.make_dr_move(col, amount)
    
    if nim.current_move == "Dr. Stewart":
        print("Dr Stewart has won like expected")
    else:
        print("well done, you are a genius: ", nim.player)

if __name__ == "__main__":
    main()

