  # not working battleships 5

board = []
for i in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for num in board_in:
    print board

print print_board(board)

# working
board = []
for i in range(5):
  board.append(["O"] * 5) # Add a O to the board five times

def print_board(board_in):
  for num in board_in:
    print num

print print_board(board)


# working battleships lesson 6
board = []
for i in range(5):
  board.append(["O"] * 5) # Add a O to the board five times

def print_board(board_in):
  for num in board_in:
    print " ".join(num)

print print_board(board)


# working battleships lesson 7
from random import randint 

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

# Add your code below!

def random_row(board_in):
  return randint(0, len(board_in) -1)

def random_col(board_in):
  return randint(0, len(board_in) -1)

# working battleships lesson 8
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))


# working battleships lesson 9

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Add your code below!

print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))


# working battleships lesson 10


from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if guess_col == ship_col and guess_row == ship_row:
  print "Congratulations! You sank my battleship!"


# working battleships lesson 11
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if guess_col == ship_col and guess_row == ship_row:
  print "Congratulations! You sank my battleship!"
else:
  print "You missed my battleship!"
  