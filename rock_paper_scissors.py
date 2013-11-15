import random


def generate_move():
    rand_num = random.randint(0, 2)
    possible_moves = ["rock", "paper", "scissors"]
    return possible_moves[rand_num]


def compare_moves(move1, move2):
    """
    Returns:
      1 if move1 wins,
      2 if move2 wins
      0 if it is a tie
      -1 if it is an illegal move
    """
    if move1 == "rock":
        if move2 == "paper":
            return 2
        elif move2 == "scissors":
            return 1
        else:
            return 0
    elif move1 == "paper":
        if move2 == "rock":
            return 1
        elif move2 == "scissors":
            return 2
        else:
            return 0
    elif move1 == "scissors":
        if move2 == "rock":
            return 2
        elif move2 == "paper":
            return 1
        else:
            return 0
    else:
        return -1


def rock_paper_scissors():
    print "Hello to Rock, Paper, Scissors"
    user_score = 0
    computer_score = 0
    num_ties = 0
    while True:
        user_move = raw_input("Enter your move: ")
        if user_move == "quit":
            return
        computer_move = generate_move()
        print "The computer moved: " + computer_move
        result = compare_moves(user_move, computer_move)
        if result == 0:
            num_ties += 1
            print "=> Tie!"
        elif result == 1:
            user_score += 1
            print "You won!"
        elif result == 2:
            computer_score += 1
            print "Sorry, the computer won"
        elif result == -1:
            print "Please enter 'rock', 'paper', 'scissors', or 'quit'"
        if result >= 0:
            print "The score so far is:"
            print "  Your score: " + str(user_score)
            print "  Computer's score: " + str(computer_score)
            print "  # ties: " + str(num_ties)


rock_paper_scissors()