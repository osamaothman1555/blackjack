# -*- coding: utf-8 -*-

"""
Game rules:

- Player given two cards and computer given two cards, one revealed later
- Player starts, player sees cards value and asked if he wants to hit or stay
- Player acts and is given a card that is added to his set
- Player cards tested if over 21
- If player receives an ace then he gets to choose value of card
- Move on to computer, computer gets one cards in effect as he reveals
- Computer based on value if not above 17 decides to hit and receives a card
- If not above 17 dealer hits again and again until dealer total is above 17
- Class used to store the possible deck of cards and distribute
- Class used to store the hand of the player and take a card from the deck class
- Class to process all computation with a function for the player and the
  computer
- This is excluding the while loop in main where the user input is prompted
"""

# start of BlackJack 

import random

# Global variable
game_over = 0
continue_var = 0
break_var = 0


class Hand:
    def __init__(self):
        self.deck = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            11: 'King',
            12: 'Queen',
            13: 'Jack',
            14: 'Ace'
        }
        self.hand = 0

    def add_card(self):
        """
        Choose a random card and add it to the deck
        """
        rand_num = random.randint(1, 14)
        card = self.deck[rand_num]

        if card == 'King' or card == 'Jack' or card == 'Queen':
            self.hand += 10
        elif card == 'Ace':
            _input = input("Please Enter ace value "
                           "(can only be 1 or 11): ")
            while not _input.isdigit() \
                    or (1 != int(_input) or 11 != int(_input)):
                _input = input("Please enter an integer that's either 1 or 11: ")

        else:
            self.hand += card

        print('{}'.format(self.hand))

    def reset_hand(self):
        self.hand = 0


class Game:
    def __init__(self):
        self.my_player = Hand()
        self.my_computer = Hand()

    def add_card(self, player):
        """
        Add a card to the hand of the player/computer

        :param player: the current player
        """
        if player == 'player':
            print('player\'s hand is: ')
            self.my_player.add_card()
        elif player == 'computer':
            print('computer\'s hand is:')
            self.my_computer.add_card()

    def reset_hands(self):
        """
        Reset the hand of the player and computer
        """
        self.my_player.reset_hand()
        self.my_computer.reset_hand()

    def check_player_status(self):
        """
        Check if the player win or bust during game

        :return: String of "Bust" | "Win", or None otherwise
        """
        if self.my_player.hand > 21:
            print("player loses... (player action)")
            return 'Bust'
        elif self.my_player.hand == 21:
            print("player wins! (player action")
            return 'Win'

    def check_computer_status(self):
        """
        Check if the computer win or bust during game

        :return: String "Bust" | "Win" | "check for win" | "hit again"
        """
        if self.my_computer.hand > 21:
            print("player wins! (computer action)")
            return 'Win'
        elif self.my_computer.hand == 21 and self.my_player.hand == 21:
            print("tie, player loses... (computer action)")
            return 'Bust'

        elif self.my_computer.hand >= 17:
            return 'check for win'
        else:
            return 'hit again'

    def check_for_win(self):
        """
        Checks if player or computer wins at the end of game
        """
        if self.my_player.hand > self.my_computer.hand:
            print("player wins against cpu (check for win)")
            print()
        else:
            print("player loses against cpu (check for win)")
            print()

    def player_action(self, action):
        """
        Change the player's hand based on input

        :param action: string "hit me" | "stay"
        """
        if action == 'hit me':
            self.my_player.add_card()
        elif action == 'stay':
            pass


def main():
    game = Game()
    # loop variables
    global continue_var, break_var, game_over

    def check_for_hand_win():
        # made global because i want both to be able to access
        # tried to make variable only in main_Black)jack but i need this
        # function to edit them
        global continue_var, break_var, game_over
        restart_game_check = game.check_player_status()

        if restart_game_check is not None:
            player_answer = input("Do you want to play again? Enter Y or N: ")
            if player_answer.upper() == 'Y':
                game_over = 0
                continue_var = 1
                break_var = 0
            elif player_answer.upper() == 'N':
                game_over = 1
                break_var = 1
                continue_var = 0

    while game_over == 0:
        # start initializing
        continue_var = 0
        break_var = 0
        game_over = 0
        game.reset_hands()

        # start game
        game.add_card('player')
        game.add_card('player')
        game.add_card('computer')

        # check if the player won the game and change break and con based on
        # input
        check_for_hand_win()

        if break_var == 1:
            break

        elif continue_var == 1:
            continue
        # player plays and we check if he wins
        player_action = input('Enter your move, either hit me or stay: ')
        game.player_action(player_action)
        check_for_hand_win()

        if break_var == 1:
            break

        elif continue_var == 1:
            continue
        # almost at end of game
        # computer flips second card and we see if he gets greater than 17
        game.add_card('computer')

        # here if statement because continue would always get stuck here.
        # dunno why
        if continue_var == 0:
            while game.my_computer.hand < 17:
                verdict = game.check_computer_status()
                if verdict == 'hit again':
                    game.add_card('computer')
            # here we check if computer is equal or over 21 and if won or lost 
            # we dont check who has the greater value
            cpu_win_or_lose = game.check_computer_status()
            if cpu_win_or_lose != 'Win' and cpu_win_or_lose != 'Bust':
                game.check_for_win()

        # this time we ask if you want to play again outside check_for_hand_win 
        player_answer = input(
            "Do you want to play again (last one)? Enter Y or N: "
        )

        if player_answer.upper() == 'Y':
            game_over = 0
        elif player_answer.upper() == 'N':
            game_over = 1
            break


print('Welcome to the Black jack game!')
print('You will be playing against the computer')
print('The total number of player\' and CPU\'s deck '
      'will be displayed in each turn')
print('Thank you and have fun!')
input("Please press Enter to begin...")
main()
