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

def first_rounds():
    global player_total, player_hand_count, hit_choice, win_condition, player_blackjack, player_bust, dealer_blackjack, tie_game
    win_condition = 0
    player_bust = 0
    player_blackjack = 0
    dealer_blackjack = 0
    tie_game = 0
    if player_hand_count == 1:
        player_hand_count = 2
        print('***********************************************************')
        print('')
        print(f' New Game: {player_name.title()}  VS Computer Dealer')
        print(" ")
        player_total = player_hand_1
        print('***********************************************************')
        print(' First Dealing')
        time.sleep(0.5)
        print(' Dealer is Dealing')
        time.sleep(0.5)
        print(' Please wait...')
        wait = ('*****')
        print(f' {wait[:1]}')
        time.sleep(0.5)
        print(f' {player_name.title()} has {player_hand_1} on hand')
        time.sleep(0.5)
        print(f' Dealer has {dealer_hand_1} on hand')
        print(' ')
        
    if player_hand_count == 2:
        player_total = player_hand_1 + player_hand_2
        print('***********************************************************')
        print(' Second Dealing')
        time.sleep(0.5)
        print(' Dealer is Dealing')
        time.sleep(0.5)
        print(' Please wait...')
        wait = ('****')
        print(f' {wait[:1]}')
        time.sleep(0.5)
        print(f' {wait[:2]}')
        time.sleep(0.5)
        print(f' {player_name.title()} has {player_hand_1} and {player_hand_2} on hand')
        time.sleep(0.5)
        print(f' Dealer has {dealer_hand_1} and XXX on hand')
        time.sleep(0.5)
        print('***********************************************************')
        print(f' Total {player_name.title()} card is {player_total}')
        print(f' Total Dealer card is {dealer_hand_1} + XXX ')
        print('***********************************************************')
    #Check if player bust
    player_bust_on_hit()
    #Check if player win BlackJack
    
    
def player_bust_on_hit():
    global player_total, player_hand_count, win_condition, player_bust
    if player_total > 21:
        win_condition = 0
        player_bust = 1
        print('========================================================')
    if player_total > 21 and player_hand_count == 2 :
        print(f' {player_name.title()} Bust. You have {player_hand_1} and {player_hand_2} on hand ')
    if player_total > 21 and player_hand_count == 3 :
        print(f' {player_name.title()} Bust. You have {player_hand_1}, {player_hand_2} and {player_hand_3} on hand ')
    if player_total > 21 and player_hand_count == 4 :
        print(f' {player_name.title()} Bust. You have {player_hand_1}, {player_hand_2}, {player_hand_3} and {player_hand_4} on hand ')
    if player_total > 21 and player_hand_count == 5 :
        print(f' {player_name.title()} Bust. You have {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4} and {player_hand_5} on hand ')
    if player_total > 21 and player_hand_count == 6 :
        print(f' {player_name.title()} Bust. You have {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4}, {player_hand_5} and {player_hand_6} on hand ')
    if player_total > 21:
        print(f' Total {player_name.title()} card is {player_total} ')
        print('========================================================')


def main():
    global player_name
    #Get player name
    get_player_name()
    #Bet placing
    #Player card random selection from deck
    player_hand_selection()
    #Dealer card random selection from deck
    dealer_hand_selection()
    #First two round play
    #Player choose to hit or stand
    #Giving results according to the win condition
    #Calculating bet win
    #Start again the game
main()   
      