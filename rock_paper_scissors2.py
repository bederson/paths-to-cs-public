import random

# 'winner_order' is an array that specifies which moves beats which
# where each item beats the one just after it. Some items are repeated
# so that every item type can be compared to the items following it.
WINNER_ORDER = ["rock", "scissors", "paper", "rock", "scissors"]


def generate_move():
    rand_num = random.randint(0, 2)
    possible_moves = ["rock", "paper", "scissors"]
    return possible_moves[rand_num]


def valid_move(move):
    return move in WINNER_ORDER


def compare_moves(move1, move2):
    """
    Returns:
      0 if it is a tie
      1 if move1 wins,
      2 if move2 wins
    """
    if move1 == move2:
        return 0
    index1 = WINNER_ORDER.index(move1)
    index2 = WINNER_ORDER.index(move2, index1)
    if index2 - index1 == 1:
        return 1
    else:
        return 2


def print_welcome():
    print "Welcome to Rock, Paper, Scissors."
    print "Your available moves are: rock, paper, scissors. Or type 'quit' to quit."
    print ""


def print_scores(user_score, computer_score, num_ties):
    print "The score so far is:"
    print "  Your score: " + str(user_score)
    print "  Computer's score: " + str(computer_score)
    print "  # ties: " + str(num_ties)


def rock_paper_scissors():
    print_welcome()
    user_score = 0
    computer_score = 0
    num_ties = 0
    while True:
        user_move = raw_input("Enter your move: ").lower()
        if user_move == "quit":
            return
        if valid_move(user_move):
            computer_move = generate_move()
            print "The computer moved: " + computer_move
            result = compare_moves(user_move, computer_move)
            if result == 0:
                num_ties += 1
                print "=> Tie!"
            elif result == 1:
                user_score += 1
                print "=> You won!"
            elif result == 2:
                computer_score += 1
                print "=> Sorry, the computer won"
            print_scores(user_score, computer_score, num_ties)
        else:
            print "Please enter 'rock', 'paper', 'scissors', or 'quit'"


rock_paper_scissors()