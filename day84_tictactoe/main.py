possible_moves = {'a1':1, 'b1':2, 'c1':3, 'a2':4, 'b2':5, 'c2':6, 'a3':7, 'b3':8, 'c3':9}

def board(placeholder):
    print("   a  |  b  |  c  ")
    print("      |     |     ")
    print("1  " + placeholder[1] + "  |  " + placeholder[2] + "  |  " + placeholder[3] + "   ")
    print("      |     |     ")
    print(" -----|-----|-----")
    print("      |     |     ")
    print("2  " + placeholder[4] + "  |  " + placeholder[5] + "  |  " + placeholder[6] + "   ")
    print("      |     |     ")
    print(" -----|-----|-----")
    print("      |     |     ")
    print("3  " + placeholder[7] + "  |  " + placeholder[8] + "  |  " + placeholder[9] + "   ")
    print("      |     |     ")


def is_open(board_entries, move):
    #is the space empty
    return board_entries[possible_moves.get(move)] == '-'

def is_winner(board_entries, player):
    possible_wins = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
    player_pos = [i for i, x in enumerate(board_entries) if x == player]
    for win in possible_wins:
        if set(win).issubset(player_pos):
            return True

def board_full(board_entries):
    if "-" not in board_entries:
        return True


def main():
    game_over = False
    board_entries = ["", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    player = 'X'
    while not game_over:
        board(board_entries)
        # player makes a move
        move = input(f'Player {player}, enter your move (ex. b2): ')
        if move in possible_moves.keys() and is_open(board_entries, move):
            board_entries[possible_moves.get(move)] = player # puts player's mark on the board in desired location
        else:
            print("This move is not possible, either because you did not enter the location correctly or it is not open. Please try again.")

        if is_winner(board_entries,player):
            board(board_entries)
            print(f'Player {player} has won!')
            game_over = True
        elif board_full(board_entries):
            print("It's a draw.")
            game_over=True
            # switches the player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
  main()