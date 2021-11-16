
from Board import Board

class Bot(Board):
    def __init__(self, state):
        self.name = "Dr. Nimbot"
        self.pile_states = None
        self.state = state
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
        
        first_pile_state = self.state[0][0]
        if first_pile_state == 1:
            first_pile.append(1)
        
        second_pile_state = self.state[1][0]
        if second_pile_state == 3:
            second_pile.append(1)
            second_pile.append(2)
        elif second_pile_state == 2:
            second_pile.append(2)
        elif second_pile_state == 1:
            second_pile.append(1)


        third_pile_state = self.state[2][0]
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


        fourth_pile_state = self.state[3][0]
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
    Depending on number of odd state values uses different algorithm to determine which column and amount to subtract from piles.
    This algorithm changes as game goes on. Game changes states many times through out 1v1
    '''
    def nim_algorithm(self):
        smallest = 10
        largest = 0
        pile_largest = []
        largest_pile = 0
        largest_column = None
        smallest_pile = 10
        empty_pile_tracker = 0
        single_pile_tracker = 0
        large_pile_tracker = 0
        col_num = 0
        col_total = 0
        

        for piles in self.state:
            if piles[0] > 1:
                large_pile_tracker +=1
            if piles[0] == 0:
                empty_pile_tracker += 1
            if piles[0] == 1:
                single_pile_tracker +=1


        if empty_pile_tracker ==2 and large_pile_tracker ==2:
            for col, piles in enumerate(self.state):
                if piles[0] > 1:
                    pile_largest.append([piles[0],col])
            
            for val in pile_largest:
                if val[0] > largest_pile:
                    largest_pile = val[0]
                    largest_column = val[1]
                if val[0]< smallest_pile:
                    smallest_pile = val[0]

            subtraction_amount = largest_pile - smallest_pile

            return largest_column, subtraction_amount

                
        if empty_pile_tracker ==2 and single_pile_tracker ==2:
            for col, piles in enumerate(self.state):
                if piles[0] == 1:
                    col_total = piles[0]
                    return col, col_total

        if single_pile_tracker ==3:
            for col, piles in enumerate(self.state):
                if piles[0] > 1:
                    col_total = piles[0]
                    return col, col_total


        if single_pile_tracker ==2 and large_pile_tracker ==1:
            for col, piles in enumerate(self.state):
                if piles[0] > 1:
                    col_total = piles[0]-1
                    return col, col_total
        
        if empty_pile_tracker == 3:
            for col, piles in enumerate(self.state):
                if piles[0] > 1:
                    col_total = piles[0] -1
                    return col, col_total

        if empty_pile_tracker == 2 and single_pile_tracker == 1:
            for col, piles in enumerate(self.state):
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
                


                total = largest + smallest
                state_total = 0
                
                
                for val in self.pile_states:
                    if largest in val:
                        for num in val:
                            state_total += num


                if (total > state_total):
                    subtraction_amount = largest-smallest
                else:
                    subtraction_amount = largest+smallest

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
                    elif largest in val and middle_col_val in val:
                        subtraction_amount = largest + middle_col_val - smallest
                        return col, subtraction_amount
                    elif len(val) ==1 and largest in val:
                        subtraction_amount = largest-middle_col_val - smallest
                        return col, subtraction_amount
                    elif largest in val:
                        return col, subtraction_amount


    '''
    Keeps track of the state of the board after the Dr. makes his moves.
    '''
    def dr_state(self, col, amount):
        print("Dr. Nimbot is making his move now")
        print("AI turn : \n")
        self.state[int(col)][0] -= int(amount)
        print("The Dr took ", amount, "sticks from pile: ", col +1)
        self.print_board(self.state)
        return self.state