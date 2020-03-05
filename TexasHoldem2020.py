import itertools
import pdb
import random
import os
clear = lambda: os.system('cls')
cls = lambda: print ("\n" * 100)

class deque_of_cards:
    list1=['♣','♦','♥','♠']
    list2=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deque = list(itertools.product(list1, list2)) 
        
    def __init__(self):
        print(num_of_cards)
        
    def print_cards(cards):
        for j in range(len(cards)):
            print(f'[{cards[j][0]}{cards[j][1]}] ', end = '')
        print('')
        
class player:
    num_of_players=0
    turn=0
    sblind=0
    bblind=0
    stake=0
    
    def __init__(self):
        self.name=input('Chose your name: ')
        while True:
            opt=input('How much cash do you have? ')
            if opt.isnumeric and opt.isalnum : break
            else : continue
        self.cash=int(opt)
        self.cards=[0,0]
        player.num_of_players += 1
        self.active=True
        self.raised=0
        self.checked_flag=0
        self.wait_flag=0
        
    def __del__(self):
        player.num_of_players -=1
        
    def raise_the_stake(self):
        while True:
            amount=input('Enter sum: ')
            if amount.isnumeric() and int(amount)+table.highest_raise<=self.cash:
                amount=int(amount)
                player.raise_the_stake2(self,amount)
                break
            else:
                continue
            
    def raise_the_stake2(self,amount):
        player.stake+=amount
        self.cash-=table.highest_raise+amount
        self.raised=table.highest_raise+amount
        table.highest_raise+=amount
        self.checked_flag=1
            
    def check(self):
        if  self.cash<=table.highest_raise-self.raised:
            player.stake+=self.cash
            self.cash=0
            print('ALL IN!')
            self.checked_flag=1
        else:
            player.stake+=table.highest_raise-self.raised
            self.cash-=table.highest_raise-self.raised
            self.checked_flag=1
                
    def pass_move(self):
        '''
        allows player to pass the move
        '''
    
    def quit(self):
        '''
        allows player to quit
        '''

class table:
    cards_on_table=[]
    highest_raise=0
    ready=True
    no_raise_flag=0
    
    def flop():
        print('FLOP')
        for i in range(3):
            table.cards_on_table.append(deque_of_cards.deque.pop(random.randint(0,len(deque_of_cards.deque)-1))) 
    def turn():
        print('TURN')
        table.cards_on_table.append(deque_of_cards.deque.pop(random.randint(0,len(deque_of_cards.deque)-1)))
    def river():
        print('RIVER')
        table.cards_on_table.append(deque_of_cards.deque.pop(random.randint(0,len(deque_of_cards.deque)-1)))
        
def game():
    print("Poker Texas Holdem")
    n_of=input("How many players?  ")
    n_of=int(n_of)
    players=[]
    for number in range(n_of):
        print(f'Player {number}, enter your data')
        players.append(player())
    start(players)
    cycle(players)
    table.turn()
    cycle(players)
    table.river()
    cycle(players)
    print("END")
    jury(players)
    importantDecisions()
    
def shuffle_give(players):
    random.shuffle(deque_of_cards.deque)
    for number1 in range(player.num_of_players):
        players[number1].cards[0]=deque_of_cards.deque.pop(random.randint(0,len(deque_of_cards.deque)-1))                                          
    for number2 in range(player.num_of_players):
        players[number2].cards[1]=deque_of_cards.deque.pop(random.randint(0,len(deque_of_cards.deque)-1))
    
def cycle(players):
    table.highest_raise=0
    player.stake=0
    table.no_raise_flag=0
    for j in range (player.num_of_players):
        players[j].raised=0
        players[j].wait_flag=0
        players[j].checked_flag=0
    i=0
    while i < player.num_of_players or table.ready==False:
        if players[i].active==True:
            #clear Screen
            #clear() for windows terminal
            cls() #bieda czyściciel (100 linijek \n)
            while True:
                if input(f'Are you ready {players[i].name}? Then press y: ') =='y':
                    break
                else:
                    continue
            print('Cards on the table: ',end='') 
            deque_of_cards.print_cards(table.cards_on_table)   
            print('Your cards: ',end='')
            deque_of_cards.print_cards(players[i].cards)
            print(f'Stake: {player.stake}')
            print(f'Your deposit: {players[i].cash}')
            i=options(players,i)
        i+=1
        if i==player.num_of_players:
            i=0
            table.no_raise_flag=1
        #pdb.set_trace()    
        if (set((map(lambda pl:pl.wait_flag,players))))=={1} or set((map(lambda pl:pl.checked_flag,players)))=={1}:
            break
        #pdb.set_trace()
def start(players):
    player.turn=random.randint(0,player.num_of_players-1)
    player.sblind=player.turn
    if(player.turn+1 == player.num_of_players):
        player.bblind = 0
    else:
        player.bblind = player.turn+1
    print(f'Player {players[player.sblind].name} small blind, player {players[player.bblind].name} big blind')
    shuffle_give(players)
    table.flop()
    
def options(players,i):
    tab=['1','2','3','4']
    if players[i].cash>table.highest_raise-players[i].raised and table.no_raise_flag==0 :
        print('1.Raise')
    else: tab.pop(0)
    if(players[i].raised==table.highest_raise):
        print('2.Wait')
    else:
        print('2.Check')
    print('3.Fold')
    print('4.Quit')
    
    while True:
        opt=input('Choose: ')
        if opt in tab : break
        else: continue
    if   opt=='1':
        for k in range(player.num_of_players):
            players[k].checked_flag=0
        players[i].raise_the_stake()    
    elif opt=='2':
        if players[i].raised==table.highest_raise:  #wait
            players[i].wait_flag=1
        else:   #check
            players[i].check()
    elif opt=='3':
        players[i].active=False
        players[i].checked_flag=1
        players[i].wait_flag=1
        
    elif opt=='4':
        players.pop(i)
        return i-1
    return i

def jury(players):
    print('Cards on the table: ',end='') 
    deque_of_cards.print_cards(table.cards_on_table)
    for i in range (player.num_of_players):
        if players[i].active==True :
            print(f"{players[i].name}'s cards: ",end='')
            deque_of_cards.print_cards(players[i].cards)
    table_score=ai_jury(table.cards_on_table)
    named_results=[]
    players_score=[]
    for i in range (player.num_of_players):
        if players[i].active==True :
            result=ai_jury(table.cards_on_table+players[i].cards)
            named_results.append(result[1])
            players_score.append(result[0])
        else:
            named_results.append(0)
            players_score.append(0)
    opt=players_score.index(max(players_score))

    #print('Who won?: ',end='')   
   # while True:
   #     opt=input('Choose: ')
   #     if opt in list(range(player.numb_of_players)): break
    #    else: continue

    if table_score[0]>=players_score[opt] :
       print(f'It is a match, sorry, you need to share. There was {table_score[1]} on the table')
    else:
        print(f'{players[opt].name} won {player.stake}$ with {named_results[opt]} \nCongratulations')
    players[opt].cash+=player.stake   
    #pdb.set_trace()

def importantDecisions():
    print('1.Want to play again?')
    print('2.Go back home to your wife')
    while True:
        opt=input('Choose: ')
        if opt in ['1','2'] : break
        else: continue
    if   opt=='1':
        deque_of_cards.deque = list(itertools.product(deque_of_cards.list1, deque_of_cards.list2))
        player.stake=0
        for i in range(player.num_of_players):
            players[i].active=True 
    elif opt=='2':
        import sys
        sys.exit()

def ai_jury(arg):
    flattened_cards_on_table_symbols=flatten_symbols(arg)
    flattened_cards_on_table_values=flatten_values(arg)

    tab = check_royal_flush(flattened_cards_on_table_symbols)
    if tab[0] : return tab[1],'ROYAL FLUSH!!!'
    tab = check_straight_flush(flattened_cards_on_table_values,flattened_cards_on_table_symbols) 
    if tab[0] : return tab[1],'Straight Flush!!!'
    tab=check_4(flattened_cards_on_table_values)
    if tab[0] : return tab[1],'Four of a kind!'
    tab=check_full(flattened_cards_on_table_values)
    if tab[0] : return tab[1],'Full'
    tab=check_color(flattened_cards_on_table_values)
    if tab[0] : return tab[1],'Flush'
    tab=check_straight(flattened_cards_on_table_values)
    if tab[0] : return tab[1],'Straight'
    tab=check_3(flattened_cards_on_table_values)
    if tab[0] : return tab[1],'Three of a kind'
    tab=check_2x2(flattened_cards_on_table_values)
    if tab[0] : return tab[1],'Two pairs'
    tab=check_2(flattened_cards_on_table_values)
    if tab[0] : return tab[1],'Pair'
    tab=check_high_card(flattened_cards_on_table_values)
    return tab,'High card'

def check_royal_flush(cards):
    if (set((map(lambda card:card in cards,['10','J','Q','K','A']))))=={True} and check_color(cards)[0]==True:
        return True,100000
    else:
        return False,0

def check_straight_flush(cards_values,cards_symbols):
    if check_straight(cards_values)[0]==True and check_color(cards_symbols)[0]==True:
        return True,1000
    else:
        return False,0    
    
def check_4(cards):
    for card in cards:
        if cards.count(card) == 4 :
            high=check_high_card(list(card))
            return True,high+600
    return False,0

def check_full(cards):
    value=check_2(cards)+check_3(cards)
    if value[0]==2  : 
        return True,value[1]+300
    else: 
        return False,0

def check_color(cards): #take flattened_cards_symbols
    for card in cards:
        if cards.count(card) == 5 :
            high=check_high_card(list(card))
            return True,100+high
    return False,0

def check_straight(cards) :
    if (set((map(lambda card:card in cards,['10','J','Q','K','A']))))=={True} : return True,80+14
    elif (set((map(lambda card:card in cards,['9','10','J','Q','K',]))))=={True}:return True,80+13
    elif (set((map(lambda card:card in cards,['8','9','10','J','Q']))))=={True}:return True,80+12
    elif (set((map(lambda card:card in cards,['7','8','9','10','J']))))=={True}:return True,80+11
    elif (set((map(lambda card:card in cards,['6','7','8','9','10']))))=={True}:return True,80+10
    elif (set((map(lambda card:card in cards,['5','6','7','8','9']))))=={True}:return True,80+9
    elif (set((map(lambda card:card in cards,['4','5','6','7','8']))))=={True}:return True,80+8
    elif (set((map(lambda card:card in cards,['3','4','5','6','7']))))=={True}:return True,80+7
    elif (set((map(lambda card:card in cards,['2','3','4','5','6']))))=={True}:return True,80+6
    elif (set((map(lambda card:card in cards,['A','2','3','4','5']))))=={True}:return True,80+5
    else:
        return False,0

def check_3(cards):
    for card in cards:
        if cards.count(card) == 3 :
            high=check_high_card(list(card))
            return True,60+high
    return False,0

def check_2x2(cards):
    counter=[]
    high=0
    for card in cards:
        if cards.count(card) == 2 :
            counter.append(1)
            if high<check_high_card(list(card)):
                high=check_high_card(list(card))
    if len(counter)==4:
        return True,high+40
    else : return False,0

def check_2(cards):
    for card in cards:
        if cards.count(card) == 2 :
            high=check_high_card(list(card))
            return True,high+20
    return False,0

def check_high_card(cards):

    if 'A' in cards : 
        high=14
    elif 'K' in cards : 
        high=13
    elif 'Q' in cards : 
        high=12
    elif 'J' in cards : 
        high=11
    elif '10' in cards : 
        high=10
    elif '9' in cards : 
        high=9
    elif '8' in cards : 
        high=8
    elif '7' in cards : 
        high=7
    elif '6' in cards : 
        high=6
    elif '5' in cards : 
        high=5
    elif '4' in cards : 
        high=4                   
    elif '3' in cards : 
        high=3
    else : 
        high=2
    return high




def flatten_symbols(cards):
    flattened_cards=[]
    for card in cards:
        flattened_cards.append(card[0])
    return flattened_cards

def flatten_values(cards):
    flattened_cards=[]
    for card in cards:
        flattened_cards.append(card[1])
    return flattened_cards

while True:
   game()
