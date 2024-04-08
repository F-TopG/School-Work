#Battleship 2

import random
import os

def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board():
    return [["O" for _ in range(10)] for _ in range(10)]

def place_ship(board, ship_length):
    direction = random.choice(["horizontal", "vertical"])
    x = random.randint(0, 9)
    y = random.randint(0, 9)

    while not is_valid_ship_placement(board, ship_length, x, y, direction):
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    if direction == "horizontal":
        for i in range(ship_length):
            board[y][x + i] = "S"
    else:
        for i in range(ship_length):
            board[y + i][x] = "S"

def is_valid_ship_placement(board, ship_length, x, y, direction):
    if direction == "horizontal":
        return x + ship_length <= 10 and all(board[y][x + i] == "O" for i in range(ship_length))
    else:
        return y + ship_length <= 10 and all(board[y + i][x] == "O" for i in range(ship_length))

def save_game_state(board, player1, player2):
    with open("game_state.txt", "w") as file:
        file.write(f"{player1}\n")
        file.write(f"{player2}\n")
        for row in board:
            file.write(" ".join(row) + "\n")

def load_game_state():
    if os.path.exists("game_state.txt"):
        with open("game_state.txt", "r") as file:
            player1 = file.readline().strip()
            player2 = file.readline().strip()
            board = [list(line.strip()) for line in file]
        return board, player1, player2
    else:
        return None, None, None

def take_shot(board, target_board, player):
    print(f"\n{player}'s Turn:")
    print_board(target_board)
    
    while True:
        try:
            x = int(input("Enter target X coordinate (0-9): "))
            y = int(input("Enter target Y coordinate (0-9): "))
            
            if 0 <= x < 10 and 0 <= y < 10:
                if target_board[y][x] == "O" or target_board[y][x] == "S":
                    return x, y
                else:
                    print("You've already targeted this position. Try again.")
            else:
                print("Invalid coordinates. Try again.")
        except ValueError:
            print("Invalid input. Enter integers for coordinates.")

def check_win(board):
    return all(all(cell != "S" for cell in row) for row in board)

def start_game():
    board, player1, player2 = load_game_state()

    if board is None:
        player1 = input("Enter name for Player 1: ")
        player2 = input("Enter name for Player 2: ")

        board = create_board()
        for _ in range(2):  # Place two ships for each player
            place_ship(board, 3)  # You can change the ship length as needed

    while True:
        print("\n=== Battleship Game ===")
        print(f"{player1}'s Board:")
        print_board(board)
        print("\n" + "=" * 20 + "\n")
        print(f"{player2}'s Board:")
        print_board(create_board())  # Opponent's board (no cheating!)
        print("\n" + "=" * 20)

        if check_win(board):
            print(f"\nCongratulations! {player2} wins!")
            break

        x, y = take_shot(board, create_board(), player1)
        if board[y][x] == "S":
            print("Hit!")
            board[y][x] = "X"
        else:
            print("Miss!")

        if check_win(board):
            print(f"\nCongratulations! {player1} wins!")
            break

        x, y = take_shot(board, create_board(), player2)
        if board[y][x] == "S":
            print("Hit!")
            board[y][x] = "X"
        else:
            print("Miss!")

start_game()