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
        self.cash=int(input('How much cash do you have? '))
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
            print(f"Player ({i}) {players[i].name}'s cards: ",end='')
            deque_of_cards.print_cards(players[i].cards)
    print('Who won?: ',end='')   
    while True:
        opt=input('Choose: ')
        if opt in list(range(player.numb_of_players)): break
        else: continue
    print(f'{players[opt].name} won! Congratulations')                   
    players[opt].cash+=player.stake   

def importantDecisions():
    print('1.Want to play again?')
    print('2.Go back home to your wife')
    while True:
        opt=input('Choose: ')
        if opt in ['1','2'] : break
        else: continue
    if   opt=='1':
        deque_of_cards.deque = list(itertools.product(list1, list2))
        player.stake=0
        for i in range(player.num_of_players):
            players[i].active=True 
    elif opt=='2':
        import sys
        sys.exit()
        
while True:
   game() 

