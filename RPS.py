import random
import time
# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Randomplayer(Player):
    def move(self):
        return random.choice(moves)


class Humanplayer(Player):
    def move(self):
        move = ''
        while move not in moves:
            move = input("Make your move: (rock,paper,scissors)>").lower()
        return move


class Reflectplayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        try:
            if self.their_move in moves:
                self.my_move = self.their_move
                return self.my_move
        except AttributeError:
            return random.choice(moves)


class Cycleplayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def __init__(self):
        self.my_move = ''
        self.my_list_of_moves = ['rock', 'paper', 'scissors']

    def move(self):
        self.my_move = random.choice(self.my_list_of_moves)
        self.my_list_of_moves.remove(self.my_move)
        return self.my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def print_pause(string):
    print(string)
    time.sleep(1)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.scorep1 = 0
        self.p2.scorep2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        if beats(move1, move2):
            self.p1.scorep1 += 1
            winner = "Player 1 wins!"
        elif beats(move2, move1):
            self.p2.scorep2 += 1
            winner = "Player 2 wins!"
        else:
            winner = "TIED"

        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        print_pause(winner)
        print_pause(f"\nScore---P1:{self.p1.scorep1} pts "
                    f"vs P2:{self.p2.scorep2} pts\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def Announce_the_winner(self):
        if self.p1.scorep1 > self.p2.scorep2:
            print_pause("PLAYER 1 WON THE GAME.")
        elif self.p2.scorep2 > self.p1.scorep1:
            print_pause("PLAYER 2 WON THE GAME.")
        else:
            print_pause("TIED GAME.")

    def play_game(self):
        print("\nGame start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        self.Announce_the_winner()
        play_again()


def play_again():
    answer = ''
    while answer not in ['y', 'n']:
        answer = input("Would you like to play again [y/n]").lower()
    if answer == 'y':
        game_start()
    else:
        print_pause("GAME OVER")
        print("THANKS FOR PLAYING")


def game_start():
    type_of_player = [Cycleplayer(), Reflectplayer(), Randomplayer(), Player()]
    Player2 = random.choice(type_of_player)
    Player1 = Humanplayer()
    game = Game(Player1, Player2)
    game.play_game()


if __name__ == '__main__':
    game_start()
