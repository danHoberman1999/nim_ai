from player import player
from nim_board import nimBoard
from nim_player import nimPlayer

'''
plays my game with an initial state.
'''
def play():
    board_state = [[1],[3],[5],[7]]
    current_move = None
    player_name = input("Enter player name: ")
    print("Starting Board: ")
    board = nimBoard()
    board.print_board(board_state)

    while not board.game_over(board_state):
        p1 = player(player_name, board_state)
        current_move = p1.player
        p1.player_move()
        board_state = p1.player_state()
        if board.game_over(board_state):
            break
        bot = nimPlayer(board_state)
        current_move = bot.name
        bot.nim_develop_state()
        bot.nim_dictionary()
        col, amount = bot.nim_algorithm()
        board_state = bot.dr_state(col,amount)
        if board.game_over(board_state):
            break

    print("The winner is " + current_move + "! What a great game!")


def main():
    play()

if __name__ == "__main__":
    main()  
        




    

