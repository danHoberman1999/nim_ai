
from Player import player
from Board import Board
from Bot import Bot

class NimPlayer():
    def __init__ (self):
        self.state = [[1],[3],[5],[7]]
        self.current_move = None
        self.p1_name = None

    def setGame(self):
        self.p1_name = input("Enter player 1 name: ")

    def playNormal(self):
        p1 = player(self.p1_name, self.state)
        board = Board()
        board.print_board(self.state)
        while not board.game_over(self.state):
            self.current_move = p1.player
            p1.player_move()
            self.state = p1.player_state()
            if board.game_over(self.state):
                break
            doctor = Bot(self.state)
            self.current_move = doctor.name
            doctor.nim_develop_state()
            doctor.nim_dictionary()
            col, amount = doctor.nim_algorithm()
            self.state = doctor.dr_state(col,amount)
            if board.game_over(self.state):
                break

        print("The winner is " + self.current_move + "! What a great game!")


        
    def play(self, state):
        self.state = state
        doctor = Bot(self.state)
        doctor.nim_develop_state()
        doctor.nim_dictionary()
        col, amount = doctor.nim_algorithm()
        board_state = doctor.dr_state(col,amount)
        return board_state

        
    

def main():
    player = NimPlayer()
    player.setGame()
    player.playNormal()

if __name__ == "__main__":
    main()  