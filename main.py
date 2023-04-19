import random
import time

#Global Variables
global deck, player_hand_count, player_total, dealer_total
global player_hit, player_stand, player_quite, player_proceed, ask_help

#Global value
player_hit = 'h'
player_stand = 's'
player_proceed = 'n'
player_quite = 'q'
ask_help = 'help'
deck = [1, 2, 3, 4, 5 ,6, 7, 8, 8, 10, 11, 12, 13]

def get_player_name():
    global player_name, player_hand_count
    player_name = input(' Enter your name please:  ')
    player_name = player_name.strip()
    #what if Player dont provide a name. Call them Strange Player
    if player_name == '':
        player_name = 'Strange Player'
        print('***********************************************************')
        print(f' I will call you {player_name}')
    player_hand_count = 1
    time.sleep(0.5)

def player_hand_selection():
    global player_hand_1, player_hand_2, player_hand_3, player_hand_4, player_hand_5, player_hand_6
    player_hand_1 = random.choice(deck)
    player_hand_2 = random.choice(deck)
    player_hand_3 = random.choice(deck)
    player_hand_4 = random.choice(deck)
    player_hand_5 = random.choice(deck)
    player_hand_6 = random.choice(deck)
    
def dealer_hand_selection():
    global dealer_hand_1, dealer_hand_2, dealer_hand_3, dealer_hand_4, dealer_hand_5, dealer_hand_6
    dealer_hand_1 = random.choice(deck)
    dealer_hand_2 = random.choice(deck)
    dealer_hand_3 = random.choice(deck)
    dealer_hand_4 = random.choice(deck)
    dealer_hand_5 = random.choice(deck)
    dealer_hand_6 = random.choice(deck)




def main():
    global player_name
    #Get player name
    get_player_name()
    #Player card random selection from deck
    player_hand_selection()
    #Dealer card random selection from deck
    dealer_hand_selection()
main()   
      