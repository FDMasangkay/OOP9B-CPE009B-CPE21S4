import random
from Archer import Archer
from Boss import Boss
from Novice import Novice
from Swordsman import Swordsman

from Magician import Magician


class Game:
    def __init__(self):
        self.single_player_wins = 0
        self.player_vs_player_wins = {"Player 1": 0, "Player 2": 0}
        self.roles = ["Swordsman", "Archer", "Magician"]

    def select_mode(self):
        mode = input("Select game mode (1 for Single Player, 2 for Player vs Player): ")
        if mode == "1":
            self.single_player_mode()
        elif mode == "2":
            self.player_vs_player_mode()
        else:
            print("Invalid mode. Please select a valid mode.")
            self.select_mode()

    def single_player_mode(self):
        player = Novice("Player")
        if self.single_player_wins >= 2:
            print("You have unlocked new roles!")
            role = input("Select a new role (Swordsman, Archer, Magician): ")
            if role == "Swordsman":
                player = Swordsman("Player")
            elif role == "Archer":
                player = Archer("Player")
            elif role == "Magician":
                player = Magician("Player")
            else:
                print("Invalid role. Defaulting to Novice.")
        opponent = Boss("Monster")
        self.play_match(player, opponent)
        self.select_mode()

    def player_vs_player_mode(self):
        player1 = self.select_role("Player 1")
        player2 = self.select_role("Player 2")
        self.play_match(player1, player2)
        self.select_mode()

    def select_role(self, player_name):
        print("Select a role for", player_name)
        for i, role in enumerate(self.roles):
            print(i+1, role)
        role_choice = input("Enter the number of your chosen role: ")
        if role_choice == "1":
            return Novice(player_name)
        elif role_choice == "2":
            return Swordsman(player_name)
        elif role_choice == "3":
            return Archer(player_name)
        elif role_choice == "4":
            return Magician(player_name)
        else:
            print("Invalid role. Defaulting to Novice.")
            return Novice(player_name)

    def play_match(self, player1, player2):
        players = [player1, player2]
        random.shuffle(players)
        while player1.getHp() > 0 and player2.getHp() > 0:
            for player in players:
                print("\n", player.getUsername(), "turn")
                action = input("Enter 'attack' to attack or 'heal' to heal: ")
                if action == "attack":
                    if player == player1:
                        player1.basickAttack(player2)
                    else:
                        player2.basickAttack(player1)
                elif action == "heal":
                    if player == player1:
                        player1.addHp(10)  # heal 10 HP
                    else:
                        player2.addHp(10)  # heal 10 HP
                print(player1.getUsername(), "HP:", player1.getHp())
                print(player2.getUsername(), "HP:", player2.getHp())
        if player1.getHp() <= 0:
            print(player2.getUsername(), "wins!")
            if player2.getUsername() == "Player":
                self.single_player_wins += 1
            else:
                self.player_vs_player_wins[player2.getUsername()] += 1
        else:
            print(player1.getUsername(), "wins!")
            if player1.getUsername() == "Player":
                self.single_player_wins += 1
            else:
                self.player_vs_player_wins[player1.getUsername()] += 1
    def start_game(self):
        print("Welcome to the game!")
        self.select_mode()

game = Game()
game.start_game()