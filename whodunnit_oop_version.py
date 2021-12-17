import random


class Player():
    def __init__(self,name,status):
        self.name = name
        self.status = status

    def fake_kill(self):
        fake_victim = input("Enter the name of your fake or real victim:\r\n:> ")   

class Killer(Player):
    def real_kill(self):
        killer_victim = input("Enter the name of your fake or real victim:\r\n:> ")
        return killer_victim

class Game():
    def __init__(self,max_players):
        self.max_players = max_players
        self.player_list = []

    def add_player(self,player):
        if len(self.player_list) < self.max_players:
            self.player_list.append(player)
            return True
        else: 
            return False

    def remove_player(self,player):
        player.status = 'dead'        

    def register(self):
        name = input("What is your name")
        status = 'alive'
        player = Player(name,status)
        self.add_player(player)


def play_game():
        name_list = []
        max_players = int(input('What are the max players'))
        game = Game(max_players)  
        for i in range (max_players):
            game.register()
            name_list.append(game.player_list[i].name)
        print(name_list)
        killer = (random.choice(game.player_list))
        killer = Killer(killer.name,killer.status)
        for i in name_list:
            print(f'Give the laptop to {i}')
            with_laptop = input(f'Is the laptop with {i}?(y or n)\r\n> ')
            if with_laptop == 'y':
                if i != killer.name:
                    press_enter = input('You are not the killer. Press ok to continue')
                else:
                    press_enter = input('You are the killer. Press ok to continue')
                if press_enter == 'ok':
                    print("\033[A" + " "*20 + "\033[A")
        while True:
            for i in name_list:
                print(f'Give the laptop to {i}')
                with_laptop = input(f'Is the laptop with {i}?(y or n)\r\n> ')
                if with_laptop == 'y':
                    if i != killer.name: #checks if player is killer and if not grabs their object and fake kills
                        for j in game.player_list:
                            if j.name == i:
                                j.fake_kill()               
                    else:
                        kill_victim = killer.real_kill()
                    print("\033[A" + " "*200 + "\033[A")  
            if kill_victim in name_list:
                for j in game.player_list:
                    if j.name == kill_victim:
                        game.remove_player(j) 
                        name_list.remove(j.name)
                print (f'{kill_victim} has died')        
                if len(name_list) < 3:
                    print(f"The murderer {killer.name} has won")
                    break
                group_guess = input("The group should pick one person to eliminate\r\n:> ")
                if group_guess in name_list:
                    for j in game.player_list:
                        if j.name == group_guess:
                            game.remove_player(j)
                            name_list.remove(j.name)
                print(f'You have killed {group_guess}')
                if group_guess == killer.name:   
                    print(f'Congratulations you have eliminated the murder')
                    break
                elif group_guess != killer.name:
                    print(f'{group_guess} was innocent\r\nThe killer is still out there..')    
                    continue                   
play_game()
