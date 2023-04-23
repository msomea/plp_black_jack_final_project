#Importing random and time modules
import math #for converting bet
import random #for random selection of card from deck
import time #to give life to our game and make it interactive

#Global Variables
global deck, player_hand_count, player_total, dealer_total, alphabet, alph
global player_hit, player_stand, player_quite, player_proceed, ask_help

#Global value
player_hit = 'h' #Player hit if choose this
player_stand = 's' #Player stand if choose this
player_proceed = 'n' #Player proceed to new game when run out of casha
player_quite = 'q' #Player quit the game and loop stop
ask_help = 'help' #Player get help on playing game
deck = [1, 2, 3, 4, 5 ,6, 7, 8, 8, 10, 11, 12, 13] #Deck for card selection. Ace is Always 1
alphabet = ['a', 'b','c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x', 'y','z','!','@','$','%','^','&','*','(',')',',','/','[','\\']

    
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
    global money, bet, balance, possible_win, black_jack_win, elements, alphabet
    print('***********************************************************')
    while True:
        time.sleep(0.5)
        print(f" Your balance: Tsh {money}")
        time.sleep(0.5)
        bet = (input(" Enter your bet: Tsh ")) #get bet as string
        bet = bet.lower().replace(',', '').replace('K', '000').replace('k', '000') #convert bet to all small, remove , and replace k with 1000
        if bet == '': #if bet is empty return Tsh 0
            print('***********************************************************')
            print(' You can enter Integer only')
            print('***********************************************************')
            continue
        if bet == 'help':
            help()
            continue
        for elements in bet: #If bet is alphanumeric or contain special character
            elements = elements
        if elements in alphabet:
            print('***********************************************************')
            print(' You can enter Integer only')
            print('***********************************************************')
            continue
        bet = float(bet)
        bet = math.ceil(bet)
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
            time.sleep(0.5)
            print('***********************************************************')
            continue
        if bet < 500 and money > 500:
            print(" You can place bet starting from Tsh 500")
            time.sleep(0.5)
            print('***********************************************************')
            continue
        else:
            break
    balance=((int(money))-bet)
    possible_win = bet * 2
    black_jack_win = bet * 3
    print(f''' {player_name.title()} placed bet: Tsh {bet}. Available balance: Tsh {balance}.
 Winning will pays you 2 times of your bet amount. Possible winning: Tsh {possible_win}.
 Black Jack will pays you 3 times of your bet. Possible winning on Black Jack: Tsh {black_jack_win} ''')
    print('***********************************************************')
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
    player_win_blackjack()

#Player choose to hit or stand. If choose to hit will enter into play 2 - 6 loop
def player_hit_choice():
    global hit_choice, player_hand_count, player_hit, player_stand
    while True:
        hit_choice = str(input (" Press h/H to Hit, Press s/S to Stand and enter help for Help: "))
        hit_choice = hit_choice.lower().strip()
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
        print(f' {player_name.upper()} WON')
        print_player_win()

#player win with black jack and the bet will be 3 times      
def player_win_blackjack():
    global win_condition, dealer_total, player_total, player_blackjack
    if 21 == player_total:
        win_condition = 1
        player_blackjack = 1
        print(f' BLACKJACK! {player_name.upper()} WON')
        print_player_win_black_jack()

#Dealer win and the Player lost the bet        
def dealer_win():
    global win_condition
    if 21 > dealer_total > player_total or player_total > 21 > dealer_total:
        win_condition = 0
        print(' DEALER WON')
        print_dealer_win()

#Dealer win Black jack and the Player lost the bet
def dealer_win_blackjack():
    global win_condition, dealer_blackjack
    if 21 == dealer_total:
        win_condition = 0
        dealer_blackjack = 1
        print('***********************************************************')
        print(' BLACK JACK! DEALER WON')
        print_dealer_win()

#Tie game. The player Bet will be returned
def tie_game_condition():
    global win_condition, tie_game
    if player_total == dealer_total:
        win_condition = 0
        tie_game = 1
        print(' TIE GAME! NO WINNER')
        print_tie_game()
        
#Win Message
#When Player win with Blackjack
def print_player_win_black_jack():
    print('========================================================')
    if player_hand_count == 2 :
        print(f' {player_name.title()} have: {player_hand_1} and {player_hand_2} on hand ')
    if player_hand_count == 3 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2} and {player_hand_3} on hand ')
    if player_hand_count == 4 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3} and {player_hand_4} on hand ')
    if player_hand_count == 5 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4} and {player_hand_5} on hand ')
    if player_hand_count >= 6 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4}, {player_hand_5} and {player_hand_6} on hand ')
    print(f' {player_name.title()} won with total of {player_total} card')
    print('========================================================')

    print('========================================================')
#When Player win normal               
def print_player_win():
    print('========================================================')
    if player_hand_count == 2 :
        print(f' {player_name.title()} have: {player_hand_1} and {player_hand_2} on hand ')
    if player_hand_count == 3 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2} and {player_hand_3} on hand ')
    if player_hand_count == 4 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3} and {player_hand_4} on hand ')
    if player_hand_count == 5 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4} and {player_hand_5} on hand ')
    if player_hand_count >= 6 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4}, {player_hand_5} and {player_hand_6} on hand ')
    print(f' {player_name.title()} won with total of {player_total} card')
    if dealer_card_counter == 2:
        print (f" Dealer have: {dealer_hand_1} and {dealer_hand_2} on hand")
    if dealer_card_counter == 3:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2} and {dealer_hand_3} on hand")
    if dealer_card_counter == 4:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3} and {dealer_hand_4} on hand")    
    if dealer_card_counter == 5:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3}, {dealer_hand_4} and {dealer_hand_5} on hand")
    if dealer_card_counter == 6:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3}, {dealer_hand_4}, {dealer_hand_5} {dealer_hand_6} on hand")
    print (f" Dealer has total of {dealer_total} card")
    print('========================================================')
    
#when  dealer win normal   
def print_dealer_win():
    print('========================================================')
    if player_hand_count == 2 :
        print(f' {player_name.title()} have: {player_hand_1} and {player_hand_2} on hand ')
    if player_hand_count == 3 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2} and {player_hand_3} on hand ')
    if player_hand_count == 4 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3} and {player_hand_4} on hand ')
    if player_hand_count == 5 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4} and {player_hand_5} on hand ')
    if player_hand_count >= 6 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4}, {player_hand_5} and {player_hand_6} on hand ')
    print(f' {player_name.title()} have total of {player_total} card')
    if dealer_card_counter == 2:
        print (f" Dealer have: {dealer_hand_1} and {dealer_hand_2} on hand")
    if dealer_card_counter == 3:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2} and {dealer_hand_3} on hand")
    if dealer_card_counter == 4:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3} and {dealer_hand_4} on hand")    
    if dealer_card_counter == 5:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3}, {dealer_hand_4} and {dealer_hand_5} on hand")
    if dealer_card_counter == 6:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3}, {dealer_hand_4}, {dealer_hand_5} {dealer_hand_6} on hand")
    print (f" Dealer won with total of {dealer_total} card")
    print('========================================================')

#When it is Tie Game ie Draw    
def print_tie_game():
    print('========================================================')
    if player_hand_count == 2 :
        print(f' {player_name.title()} have: {player_hand_1} and {player_hand_2} on hand ')
    if player_hand_count == 3 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2} and {player_hand_3} on hand ')
    if player_hand_count == 4 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3} and {player_hand_4} on hand ')
    if player_hand_count == 5 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4} and {player_hand_5} on hand ')
    if player_hand_count >= 6 :
        print(f' {player_name.title()} have: {player_hand_1}, {player_hand_2}, {player_hand_3}, {player_hand_4}, {player_hand_5} and {player_hand_6} on hand ')
    print(f' {player_name.title()} have total of {player_total} card')
    if dealer_card_counter == 2:
        print (f" Dealer have: {dealer_hand_1} and {dealer_hand_2} on hand")
    if dealer_card_counter == 3:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2} and {dealer_hand_3} on hand")
    if dealer_card_counter == 4:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3} and {dealer_hand_4} on hand")    
    if dealer_card_counter == 5:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3}, {dealer_hand_4} and {dealer_hand_5} on hand")
    if dealer_card_counter == 6:
        print (f" Dealer have: {dealer_hand_1}, {dealer_hand_2}, {dealer_hand_3}, {dealer_hand_4}, {dealer_hand_5} {dealer_hand_6} on hand")
    print (f" Dealer have total of {dealer_total} card")
    print('========================================================')

#Our help to use on how to play   
def help():
    print('========================================================')
    print('     BLACK JACK HELP CENTER')
    print('========================================================')
    print('''
    Welcome to Black Jack game.
    This game was designed by Raphael Msomea
    You are starting the game with Tsh 10000 to place bet and multiply it by winning game
    You can place Bet starting from Tsh 500 up to the Maximum amount you have in your balance
    Watch out not to get below Tsh 500 or to Tsh 0
    You can choose to HIT by pressing 'h' and STAND by pressing 's'
    To start new game when run out of cash press 'n' 
    To Quite the game when promped press 'q'
    To access help center enter 'help'
''')
    print('========================================================')
    
#Bet winning calculation
def bet_winning():
    global bet, bet_win, balance, money, player_hand_count
    player_hand_count = 1
    if win_condition == 1:
        bet_win = (bet * 2)
    if win_condition == 1 and player_blackjack == 1:
        bet_win = (bet * 3) 
    if win_condition == 0:
        bet_win = 0
    if tie_game == 1:
        bet_win = bet
    money = balance + bet_win

#Better game play with Loops
def game_play():
    global hit_choice, player_hit, player_bust, player_blackjack, player_choice
    global player_hand_count, player_total, dealer_total, money, win_condition, balance, bet, bet_win
    while True:
        money = 10000
        while money > 0:
            #Random select player Card
            player_hand_selection()
            #Random select dealer card
            dealer_hand_selection()
            #Bet placing
            bet_placing()
            #Dealer Play Round One and Two
            while True:
                player_choice = input(' To start dealing press enter. To enter Help center enter help: ')
                player_choice = player_choice.lower().strip()
                if player_choice == '':
                    first_rounds()
                    break
                if player_choice in ask_help:
                    help()
                    continue
                else:
                    first_rounds()
                    break
            #Player choose to Hit or Stand if not Bust
            if player_bust != 1 and player_blackjack != 1: 
                player_hit_choice()
                while hit_choice in player_hit:
                    #Player choose to Hit
                    player_hit_round()
                    #Check for player Burst
                    player_bust_on_hit()
                    #Check for blackjack
                    player_win_blackjack()
                    #Player choose to Hit or Stand when still on game
                    if player_bust == 0 and player_blackjack == 0: 
                        player_hit_choice()
                    #Play stop when player Bust or win by BlackJack
                    if player_bust == 1 or player_blackjack == 1:
                        break
                    if player_hand_count == 7:
                        print('***********************************************************')
                        print(f' Sorry {player_name.title()} no more dealing')
                        dealer_hit()
                        break
            #Check for player or dealer win or Tie game
            if player_bust == 0 and player_blackjack == 0:
                player_win()
            if dealer_blackjack == 0 and player_bust == 0 and player_blackjack == 0:
                dealer_win()
            if dealer_blackjack == 1:
                dealer_win_blackjack() 
            #Bet ammount calculation
            bet_winning()
        #Ending game
        print(f" You are out of Cash! {player_name.title()} ")
        time.sleep(0.5)
        choice = str(input(" To quite press q/Q. To start new game press n/N: "))
        choice = choice.lower()
        if choice in player_quite:
            break
        if choice in player_proceed:
            continue
#Main game play   
def main():
    global player_name
    #Get player name
    get_player_name()
    #Game play
    game_play()
main()   

      