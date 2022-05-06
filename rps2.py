import random
moves = ['rock', 'paper', 'scissors']

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']

    def move(self):
        return self.moves[0]

    def __init__(self):
        # initialization of the list for the move function
        # in CyclePlayer class
        self.my_move = self.moves
        self.their_move = self.moves[0]
        # First is move always rock

    def learn(self, my_move, their_move):
        # tracks players move
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    # Random move for computer
    def move(self):
        index = random.randint(0, 2)
        return moves[index]


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return self.moves[0]  # First move is always rock
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'
# Remembers previous move from last round
# and cycles through the different moves


class HumanPlayer(Player):
    def move(self):
        # repeats input statement until an item
        # is chosen from the list or they quit
        while True:
            # Ask player to make a choice
            # Human_move is player move
            Human_move = input('rock, paper, scissors? >')
            if Human_move.lower() == 'quit':
                quit()
            elif Human_move in self.moves:
                return Human_move.lower()
            while Human_move not in self.moves:
                print('Please choose one of the options provided')
                break


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # initial score
        self.score_p1 = 0
        self.score_p2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        # move

        move1 = self.p1.move()
        move2 = self.p2.move()
        # Game outcome and tracking players scores
        if self.beats(move1, move2):
            self.score_p1 += 1
            Results = '**** WINNER! WINNER! CHICKEN DINNER! YOU WIN!!! ****'
        elif self.beats(move2, move1):
            self.score_p2 += 1
            Results = '**** SORRY, THE COMPUTER WINS!!! ****'
        else:
            move1 == move2
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            Results = '**** YOU GOT A TIE!!! ****'
        # match information
        print(
            f">>> YOU : {move1}"
            f"\n>>> COMPUTER: {move2}"
            f"\n{Results}"
            f"\nScore: Player one ( {self.score_p1} ),"
            f"Player two ( {self.score_p2} )"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(
            "** Game start! **"
            "\n*** WELCOME TO THE WONDERFUL WORLD OF ROCK,"
            " PAPER, AND SCISSORS!!! *** "
            "You can type [quit] "
            "at anytime")

        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.score_p1 < self.score_p2:
            print(
                f"\n >>> PLAYER TWO WINS! <<< "
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )"
            )
        elif self.score_p1 > self.score_p2:
            print(
                f"\n >>> PLAYER ONE WINS YAY! <<<"
                f"\nScore: Player one ( {self.score_p1} )*,"
                f"Player two ( {self.score_p2} )"
            )

        else:
            self.score_p1 == self.score_p2
            print(
                f"\n>>> THE GAME IS A TIE! <<< "
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )*"
            )

        while True:
            # Gives the player a chance to play the game again or not
            choice = input("Would you like to play again? (yes/no)").lower()
            if choice == "yes":
                print("\n\n\n... Excellent! Restarting the game ...\n\n\n")
                Game.play_game(self)
                break
            elif choice == "no":
                print("\n\n\nThanks for playing! See you next time!\n\n\n")
                break
            else:
                print("Please choose one of the options provided")
                break


if __name__ == '__main__':

    # Starts the game between a human player and
    # computer player. The computer choices are random
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), ReflectPlayer(), CyclePlayer()]))

    game.play_game()
