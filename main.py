#Importing random and time modules
import random
import time

#Global Variables
global deck, player_hand_count, player_total, dealer_total
global player_hit, player_stand, player_quite, player_proceed, ask_help

#Global value
player_hit = 'h' #Player hit if choose this
player_stand = 's' #Player stand if choose this
player_proceed = 'n' #Player proceed to new game when run out of casha
player_quite = 'q' #Player quit the game and loop stop
ask_help = 'help' #Player get help on playing game
deck = [1, 2, 3, 4, 5 ,6, 7, 8, 8, 10, 11, 12, 13] #Deck for card selection. Ace is Always 1

#Function for asking player name. if none provided call them Strange Player.
# If provided with white space strip the whitespace
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

#Random selection of player card from the deck
def player_hand_selection():
    global player_hand_1, player_hand_2, player_hand_3, player_hand_4, player_hand_5, player_hand_6
    player_hand_1 = random.choice(deck)
    player_hand_2 = random.choice(deck)
    player_hand_3 = random.choice(deck)
    player_hand_4 = random.choice(deck)
    player_hand_5 = random.choice(deck)
    player_hand_6 = random.choice(deck)

#Random selection of dealer card from the deck   
def dealer_hand_selection():
    global dealer_hand_1, dealer_hand_2, dealer_hand_3, dealer_hand_4, dealer_hand_5, dealer_hand_6
    dealer_hand_1 = random.choice(deck)
    dealer_hand_2 = random.choice(deck)
    dealer_hand_3 = random.choice(deck)
    dealer_hand_4 = random.choice(deck)
    dealer_hand_5 = random.choice(deck)
    dealer_hand_6 = random.choice(deck)
    
#Bet placing
def bet_placing():
    global money, bet, balance, possible_win
    print('***********************************************************')
    while True:
        time.sleep(0.5)
        print(f" Your balance: Tsh {money}")
        time.sleep(0.5)
        bet=int(input(" Enter your bet: Tsh "))
        time.sleep(0.5)
        print('***********************************************************')
        time.sleep(0.5)
        if money < 500 and bet < 500:
            print(" You Dont have enough balance")
            time.sleep(0.5)
            print('***********************************************************')
            time.sleep(0.5)
            print(' STARTING NEW GAME')
            time.sleep(0.5)
            game_play()
        if bet > money:
            print(" You Dont have enough balance")
            continue
        if bet < 500 and money > 500:
            print(" You can place bet starting from Tsh 500 ")
            continue
        else:
            break
    balance=((int(money))-bet)
    possible_win = bet * 2
    print(f' {player_name.title()} placed bet: Tsh {bet}. Available balance: Tsh {balance}. Possible winning: Tsh {possible_win}')
    time.sleep(0.5)

#First two round play
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

#Player choose to hit or stand. If choose to hit will enter into play 2 - 6 loop
def player_hit_choice():
    global hit_choice, player_hand_count, player_hit, player_stand
    while True:
        hit_choice = str(input (" Press h/H to Hit. Press s/S to Stand: "))
        hit_choice = hit_choice.lower()
        if hit_choice in player_hit:
            player_hand_count += 1
            break
        if hit_choice in player_stand:
            dealer_hit()
            break
        if hit_choice in ask_help:
            help()
            continue
        else:
            print(' Please provide correct answer, For help enter help')
            continue

#This is important to controll Player Hand Selection
def player_hand_count():
    global player_hand_count, hit_choice
    if player_hand_count == 2:
        player_hand_count = 3
    if player_hand_count == 3:
        player_hand_count = 4
    if player_hand_count == 4:
        player_hand_count = 5
    if player_hand_count == 5:
        player_hand_count = 6
                
#Game play round 2 to 6. Only 6 Dealing is allowed
def player_hit_round():
    global hit_choice, player_hit, player_total, player_hand_count, player_name
    if hit_choice in player_hit and player_hand_count == 3:
        player_total = player_hand_1 + player_hand_2 + player_hand_3
        print(' ')
        print('***********************************************************')
        print(' Third Dealing')
        time.sleep(0.5)
        print(' Dealer is Dealing your card')
        time.sleep(0.5)
        print(' Please wait...')
        wait = ('*****')
        time.sleep(0.5)
        print(f' {wait[:1]}')
        time.sleep(0.5)
        print(f' {wait[:2]}')
        time.sleep(0.5)
        print(f' {wait[:3]}')
        time.sleep(0.5)
        print(f' {player_name.title()} has {player_hand_1}, {player_hand_2} and {player_hand_3} on hand')
        time.sleep(0.5)
        print(f' Dealer has {dealer_hand_1} and XXX on hand')
        time.sleep(0.5)
        print('***********************************************************')
        print(f' Total {player_name.title()} card is {player_total}')
        print(f' Total Dealer card is {dealer_hand_1} + XXX ')
        print('***********************************************************')

    if hit_choice in player_hit and player_hand_count == 4:
        player_total = player_hand_1 + player_hand_2 + player_hand_3 + player_hand_4
        print(' ')
        print('***********************************************************')
        print(' Fourth Dealing')
        time.sleep(0.5)
        print(' Dealer is Dealing your card')
        time.sleep(0.5)
        print(' Please wait...')
        wait = ('******')
        time.sleep(0.5)
        print(f' {wait[:1]}')
        time.sleep(0.5)
        print(f' {wait[:2]}')
        time.sleep(0.5)
        print(f' {wait[:3]}')
        time.sleep(0.5)
        print(f' {wait[:4]}')
        time.sleep(0.5)
        print(f' {player_name.title()} has {player_hand_1}, {player_hand_2}, {player_hand_3} and {player_hand_4} on hand')
        time.sleep(0.5)
        print(f' Dealer has {dealer_hand_1} and XXX on hand')
        time.sleep(0.5)
        print('***********************************************************')
        print(f' Total {player_name.title()} card is {player_total}')
        print(f' Total Dealer card is {dealer_hand_1} + XXX ')
        print('***********************************************************')

    if hit_choice in player_hit and player_hand_count == 5:
        player_total = player_hand_1 + player_hand_2 + player_hand_3 + player_hand_4 + player_hand_5
        print(' ')
        print('***********************************************************')
        print(' Fifth Dealing')
        time.sleep(0.5)
        print(' Dealer is Dealing your card')
        time.sleep(0.5)
        print(' Please wait...')
        wait = ('******')
        time.sleep(0.5)
        print(f' {wait[:1]}')
        time.sleep(0.5)
        print(f' {wait[:2]}')
        time.sleep(0.5)
        print(f' {wait[:3]}')
        time.sleep(0.5)
        print(f' {wait[:4]}')
        time.sleep(0.5)
        print(f' {wait[:5]}')
        time.sleep(0.5)
        print(f' {player_name.title()} has {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4} and {player_hand_5} on hand')
        time.sleep(0.5)
        print(f' Dealer has {dealer_hand_1} and XXX on hand')
        time.sleep(0.5)
        print('***********************************************************')
        print(f' Total {player_name.title()} card is {player_total}')
        print(f' Total Dealer card is {dealer_hand_1} + XXX ')
        print('***********************************************************')

    if hit_choice in player_hit and player_hand_count == 6:
        player_total = player_hand_1 + player_hand_2 + player_hand_3 + player_hand_4 + player_hand_5 + player_hand_6
        print(' ')
        print('***********************************************************')
        print(' Sixth Dealing')
        time.sleep(0.5)
        print(' Dealer is Dealing your card')
        time.sleep(0.5)
        print(' Please wait...')
        wait = ('******')
        time.sleep(0.5)
        print(f' {wait[:1]}')
        time.sleep(0.5)
        print(f' {wait[:2]}')
        time.sleep(0.5)
        print(f' {wait[:3]}')
        time.sleep(0.5)
        print(f' {wait[:4]}')
        time.sleep(0.5)
        print(f' {wait[:5]}')
        time.sleep(0.5)
        print(f' {wait[:6]}')
        time.sleep(0.5)
        print(f' {player_name.title()} has {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4}, {player_hand_5} and {player_hand_6} on hand')
        time.sleep(0.5)
        print(f' Dealer has {dealer_hand_1} and XXX on hand')
        time.sleep(0.5)
        print('***********************************************************')
        print(f' Total {player_name.title()} card is {player_total}')
        print(f' Total Dealer card is {dealer_hand_1} + XXX ')
        print('***********************************************************')
        
    if hit_choice in player_hit and player_hand_count == 7:
        print('***********************************************************')
        print(f' Sorry {player_name.title()} no more Hits')
        dealer_hit()
        
#Dealer hitting when Player choose to Stand
def dealer_hit():
    global dealer_total, dealer_card_counter, dealer_blackjack
    dealer_total = dealer_hand_1
    if dealer_total < 17:
        dealer_total = (dealer_total + dealer_hand_2)
        dealer_card_counter=2
        dealer_win_blackjack()
    if dealer_total < 17:
        dealer_total = (dealer_total + dealer_hand_3)
        dealer_card_counter=3
        dealer_win_blackjack()
    if dealer_total < 17:
        dealer_total = (dealer_total + dealer_hand_4)
        dealer_card_counter=4
        dealer_win_blackjack()
    if dealer_total < 17:
        dealer_total = (dealer_total + dealer_hand_5)
        dealer_card_counter=5
        dealer_win_blackjack()
    if dealer_total < 17:
        dealer_total = (dealer_total + dealer_hand_6)
        dealer_card_counter=6
        dealer_win_blackjack()
    wait = ("*******")
    if dealer_blackjack == 0:
        print('***********************************************************')
        print(f" Dealer is Hiting. Please {player_name.title()} Hold tight!....")
        print(" " + wait[:1])
        time.sleep(0.5)
        print(" " + wait[:2])
        time.sleep(0.5)
        print(" " + wait[:3])
        time.sleep(0.5)
        print(" " + wait[:4])
        time.sleep(0.5)
        print(" " + wait[:3])
        time.sleep(0.5)
        print(" " + wait[:2])
        time.sleep(0.5)
        print(" " + wait[:1])
        time.sleep(0.5)
        print('***********************************************************')
    tie_game_condition()
    
#Player Bust condition. if player bust have to loose all the bet  
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

#Player win condition and the Bet will Double
def player_win():
    global win_condition
    if 21 > player_total > dealer_total or dealer_total > 21 > player_total:
        win_condition = 1
        print_player_win()

#player win with black jack and the bet will be time 2.5        
def player_win_blackjack():
    global win_condition, dealer_total, player_total, player_blackjack
    if 21 == player_total:
        win_condition = 1
        player_blackjack = 1
        print(' BLACKJACK!')
        print_player_win_black_jack()

#Dealer win and the Player lost the bet        
def dealer_win():
    global win_condition
    if 21 > dealer_total > player_total or player_total > 21 > dealer_total:
        win_condition = 0
        print_dealer_win()

#Dealer win Black jack and the Player lost the bet
def dealer_win_blackjack():
    global win_condition, dealer_blackjack
    if 21 == dealer_total:
        win_condition = 0
        dealer_blackjack = 1
        print('***********************************************************')
        print(' BLACKJACK!')
        print_dealer_win()

#Tie game. The player Bet will be returned
def tie_game_condition():
    global win_condition, tie_game
    if player_total == dealer_total:
        win_condition = 0
        tie_game = 1
        print(' TIE GAME!')
        print_tie_game()


#Bet winning calculation
def bet_winning():
    global bet, bet_win, balance, money, player_hand_count
    player_hand_count = 1
    if win_condition == 1:
        bet_win = (bet * 2)
    if win_condition == 1 and player_blackjack = 1:
        bet_win = (bet * 2.5) 
    if win_condition == 0:
        bet_win = 0
    if tie_game == 1:
        bet_win = bet
    money = balance + bet_win

#Main game play
def main():
    global player_name
    #Get player name
    get_player_name()
    #Player card random selection from deck
    player_hand_selection()
    #Dealer card random selection from deck
    dealer_hand_selection()
    #Bet placing
    bet_placing()
    #First two round play
    first_rounds()
    #Player choose to hit or stand
    player_hit_choice()
    #Giving results according to the win condition
    
    #Calculating bet win
    #Start again the game
main()   
      