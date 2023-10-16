import random


board = [" " for _ in range(9)]


def print_board():
    print(" | ".join(board[:3]))
    print("-" * 9)
    print(" | ".join(board[3:6]))
    print("-" * 9)
    print(" | ".join(board[6:9]))


def is_board_full():
    return " " not in board


def check_win(player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False


def make_move(player, position):
    if board[position] == " ":
        board[position] = player
        return True
    return False


def ai_move():
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    make_move("O", best_move)


def minimax(board, depth, is_maximizing):
    if check_win("O"):
        return 1
    if check_win("X"):
        return -1
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        if not is_board_full():
            player_position = int(input("Enter your move (1-9): ")) - 1
            if player_position < 0 or player_position >= 9 or board[player_position] != " ":
                print("Invalid move. Try again.")
                continue
            make_move("X", player_position)
            print_board()

            if check_win("X"):
                print("You win!")
                break
            if is_board_full():
                print("It's a draw!")
                break

        ai_move()
        print_board()

        if check_win("O"):
            print("AI wins!")
            break
        if is_board_full():
            print("It's a draw!")
            break

    print("Game over!")

if __name__ == "__main__":
    main()
