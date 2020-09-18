import random
import itertools

suits = ('H', 'C', 'D', 'S')
values= ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values_1 = ('2', '3', '4', '5', '6')

player_a_hand = []
player_b_hand = []
player_a_down = []
player_b_down = []
player_a_up = []
player_b_up = []

deck = list(itertools.product(values, suits))

def player_a_finish_up(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    player_a_hand = player_a_up
    player_a_up = []
    print('player a up code running'+str(player_a_hand))
    gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    print('player a finish')
    exit()

def player_b_finish_up(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    player_b_hand = player_b_up
    player_b_up = []
    print('player b up code running'+str(player_b_hand))
    gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    print('player b finish')
    exit()

def player_a_finish_down(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    for i in range(len(player_a_down)):
        print(str(i + 1))
    main_input = int(input("Player A Please select which card to place: "))
    if main_input in range(1, len(player_a_down) + 1):
        player_a_hand = [player_a_down[main_input - 1]]
        print('player_a_down_card:'+str(player_a_hand))
        player_a_down.remove(player_a_down[main_input - 1])

    turn = ['a']
    gameplay(pile, top_card, turn, burn_pile, player_a_hand, player_b_hand, available_cards, player_a_up,
                    player_b_up, player_a_down, player_b_down)


def player_b_finish_down(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    for i in range(len(player_b_down)):
        print(str(i + 1))
    main_input = int(input("Player B Please select which card to place: "))
    if main_input in range(1, len(player_b_down) + 1):
        player_b_hand = [player_b_down[main_input - 1]]
        print('player_b_down_card:'+str(player_b_hand))
        player_b_down.remove(player_b_down[main_input - 1])

    turn = ['b']
    gameplay(pile, top_card, turn, burn_pile, player_a_hand, player_b_hand, available_cards, player_a_up,
                    player_b_up, player_a_down, player_b_down)
def initial_hand():

    while len(player_a_hand) < 3:
        index = random.randint(0, len(deck) - 1)
        player_a_hand.append(deck[index])
        del deck[index]
        index = random.randint(0, len(deck) - 1)
        player_b_hand.append(deck[index])
        del deck[index]


def initial_down():

    while len(player_a_down) < 3:
        index = random.randint(0, len(deck) - 1)
        player_a_down.append(deck[index])
        del deck[index]
        index = random.randint(0, len(deck) - 1)
        player_b_down.append(deck[index])
        del deck[index]

def initial_up():

    while len(player_a_up) < 3:
        index = random.randint(0, len(deck) - 1)
        player_a_up.append(deck[index])
        del deck[index]
        index = random.randint(0, len(deck) - 1)
        player_b_up.append(deck[index])
        del deck[index]

def start(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn == ['a']:
        if player_a_hand == []:
            if player_a_up == []:
                player_a_finish_down(pile, top_card, turn, burn_pile, player_a_hand, player_b_hand, available_cards,
                                     player_a_up, player_b_up, player_a_down, player_b_down)
            else:
                player_a_finish_up(pile, top_card, turn, burn_pile, player_a_hand, player_b_hand, available_cards,
                                   player_a_up, player_b_up, player_a_down, player_b_down)

        available_cards = player_a_hand
        for i in range(len(player_a_hand)):
            print(str(i + 1) + ":", player_a_hand[i])
        main_input = int(input("Player A Please select the card you'd like to place: "))
        if main_input in range(1, len(player_a_hand)+1):
            print("valid selection")
            options = [i for i in available_cards if i[0] in (available_cards[main_input - 1])]
            print(options)
            if len(options) > 1:
                print("How many cards would you like to play?")
                for i in range(len(options)):
                    print(str(i + 1))
                main_input = int(input("Player A Please select how many cards you'd like to place: "))
                if main_input in range(1, len(available_cards) + 1):
                    print("valid selection:")
                    selection = random.sample(options, main_input)
                    print("the following cards will be played:" + str(selection))
                    res = [sub for sub in available_cards if sub not in selection]
                    top_card = selection[0]
                    pile = pile + selection
                    player_a_hand = res
            else:
                top_card = player_a_hand[main_input-1]
                pile.append(player_a_hand[main_input-1])
                player_a_hand.remove(player_a_hand[main_input-1])
            while len(player_a_hand) < 3:
                if len(deck) == 0:
                    break
                else:
                    index = random.randint(0, len(deck) - 1)
                    player_a_hand.append(deck[index])
                    del deck[index]

            turn = ['b']
            return gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        if player_b_hand == []:
            if player_b_up == []:
                player_b_finish_down(pile, top_card, turn, burn_pile, player_a_hand, player_b_hand, available_cards,
                                     player_a_up, player_b_up, player_a_down, player_b_down)
            else:
                player_b_finish_up(pile, top_card, turn, burn_pile, player_a_hand, player_b_hand, available_cards,
                                   player_a_up, player_b_up, player_a_down, player_b_down)
        available_cards = player_b_hand
        for i in range(len(player_b_hand)):
            print(str(i + 1) + ":", player_b_hand[i])
        main_input = int(input("Player B Please select the card you'd like to place: "))
        if main_input in range(1, len(player_b_hand) + 1):
            print("valid selection")
            options = [i for i in available_cards if i[0] in (available_cards[main_input - 1])]
            print(options)
            if len(options) > 1:
                print("How many cards would you like to play?")
                for i in range(len(options)):
                    print(str(i + 1))
                main_input = int(input("Player B Please select how many cards you'd like to place: "))
                if main_input in range(1, len(available_cards) + 1):
                    print("valid selection:")
                    selection = random.sample(options, main_input)
                    print("the following cards will be played:" + str(selection))
                    res = [sub for sub in available_cards if sub not in selection]
                    top_card = selection[0]
                    pile = pile + selection
                    player_b_hand = res
            else:
                top_card = player_b_hand[main_input - 1]
                pile.append(player_b_hand[main_input - 1])
                player_b_hand.remove(player_b_hand[main_input - 1])
            while len(player_b_hand) < 3:
                if len(deck) == 0:
                    break
                else:
                    index = random.randint(0, len(deck) - 1)
                    player_b_hand.append(deck[index])
                    del deck[index]

            turn = ['a']
            return gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

        else:
            start(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if len(player_a_hand) == 0:
        if len(player_a_up) == 0:
            if len(player_a_down) == 0:
                    print('Congrats player A you won')
                    exit()

    if len(player_b_hand) == 0:
        if len(player_b_up) == 0:
            if len(player_b_down) == 0:
                    print('Congrats player B you won')
                    exit()
            else:
                player_b_finish_down(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
        else:
            player_b_finish_up(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    if len(available_cards) == 0:
        print("sorry player: " + str(turn[0]) + " you cannot play and must pick up the pile" )
        player_b_hand = player_b_hand + pile
        top_card = []
        pile = []
        turn[0] = 'a'
        gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    else:
        print("You have the following cards available to play:")
        for i in range(len(available_cards)):
            print(str(i + 1) + ":", available_cards[i])
        main_input = int(input("Player B Please select the card you'd like to place: "))
        if main_input in range(1, len(available_cards) + 1):
            print("valid selection:" + str(available_cards[main_input - 1]))
            options = [i for i in available_cards if i[0] in (available_cards[main_input - 1])]
            print(options)
            if len(options) > 1:
                print("How many cards would you like to play?")
                for i in range(len(options)):
                    print(str(i + 1))
                main_input = int(input("Player B Please select how many cards you'd like to place: "))
                if main_input in range(1, len(available_cards) + 1):
                    print("valid selection:")
                    selection = random.sample(options, main_input)
                    print("the following cards will be played:" + str(selection))
                    res = [sub for sub in available_cards if sub not in selection]
                    top_card = selection[0]
                    pile = pile + selection
                    player_b_hand = res
            else:
                top_card = available_cards[main_input - 1]
                pile.append(available_cards[main_input - 1])
                player_b_hand.remove(available_cards[main_input - 1])
            while len(player_b_hand) < 3:
                if len(deck) == 0:
                    break
                else:
                    index = random.randint(0, len(deck) - 1)
                    player_b_hand.append(deck[index])
                    del deck[index]

            turn[0] = 'a'
            gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
        else:
            player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

def player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if len(player_b_hand) == 0:
        if len(player_b_up) == 0:
            if len(player_b_down) == 0:
                    print('Congrats player B you won')
                    exit()

    if len(player_a_hand) == 0:
        if len(player_a_up) == 0:
            if len(player_a_down) == 0:
                    print('Congrats player A you won')
                    exit()
            else:
                player_a_finish_down(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
        else:
            player_a_finish_up(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    if len(available_cards) == 0:
        print("sorry player: " + str(turn[0]) + " you cannot play and must pick up the pile")
        player_a_hand = player_a_hand + pile
        top_card = []
        pile = []
        turn[0] = 'b'
        gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    else:
        print("You have the following cards available to play:")
        for i in range(len(available_cards)):
            print(str(i + 1) + ":", available_cards[i])
        main_input = int(input("Player A Please select the card you'd like to place: "))
        if main_input in range(1, len(available_cards) + 1):
            print("valid selection:" + str(available_cards[main_input - 1]))
            options = [i for i in available_cards if i[0] in (available_cards[main_input - 1])]
            print(options)
            if len(options) > 1:
                print("How many cards would you like to play?")
                for i in range(len(options)):
                    print(str(i + 1))
                main_input = int(input("Player A Please select how many cards you'd like to place: "))
                if main_input in range(1, len(available_cards) + 1):
                    print("valid selection:")
                    selection = random.sample(options, main_input)
                    print("the following cards will be played:" + str(selection))
                    res = [sub for sub in available_cards if sub not in selection]
                    top_card = selection[0]
                    pile = pile + selection
                    player_a_hand = res
            else:
                top_card = available_cards[main_input - 1]
                pile.append(available_cards[main_input - 1])
                player_a_hand.remove(available_cards[main_input - 1])
            while len(player_a_hand) < 3:
                if len(deck) == 0:
                    break
                else:
                    index = random.randint(0, len(deck) - 1)
                    player_a_hand.append(deck[index])
                    del deck[index]

            turn[0] = 'b'
            gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
        else:
            player_a_gameplay()

def gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    print("the top card is:" + str(top_card))
    print("the pile consists of:" + str(pile))


    if len(pile) >= 4:
        if pile[-1][0] == pile[-2][0] == pile[-3][0] == pile[-4][0]:
            burn_pile = pile + burn_pile
            pile = []
            top_card = []
            print("The burn pile consists of:" + str(burn_pile))
            if turn[0] == 'b':
                turn[0] = 'a'
            else:
                turn[0] = 'b'


    if top_card == []:
        start(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('A'):
        Ace_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('K'):
        King_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('Q'):
        Queen_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('J'):
        Jack_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('10'):
        ten_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('9'):
        nine_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('8'):
        eight_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('7'):
        seven_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('6'):
        six_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('5'):
        five_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('4'):
        four_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    if top_card[0] == str('3'):
        three_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    else:
        two_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def Ace_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if i[0] in('A','2','3','10')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_a_hand if i[0] in ('A', '2', '3', '10')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def King_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if i[0] in('A','K','2','3','10')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_a_hand if i[0] in ('A','K', '2', '3', '10')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def Queen_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if i[0] in('A','K','Q', '2','3','10')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_a_hand if i[0] in ('A','K','Q', '2', '3', '10')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

def Jack_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if i[0] == 'J']
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_b_hand if i[0] == 'J']
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def ten_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    burn_pile = pile + burn_pile
    pile = []
    top_card = []
    print("The burn pile consists of:" + str(burn_pile))
    if turn[0] == 'b':
            turn[0] = 'a'
    else:
        turn[0] = 'b'

    gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

def nine_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if i[0] in('A','K','Q','J', '2','3','9', '10')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_a_hand if i[0] in ('A','K','Q','J', '2', '3', '9', '10')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def eight_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
            turn[0] = 'a'
    else:
        turn[0] = 'b'
    if turn[0] == 'b':

        available_cards = [i for i in player_b_hand if
                           i[0] in ('Q', 'K', 'A', '2', '3', '8', '9', '10', 'J')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:

        available_cards = [i for i in player_a_hand if
                           i[0] in ('Q', 'K', 'A', '2', '3', '8', '9', '10', 'J')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)



def seven_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
        turn[0] = 'a'
        options = ['Higher','Lower']
        for i in range(len(options)):
            print(str(i + 1) + ":", options[i])
        main_input = int(input("Player A Please select higher or lower: "))
        if main_input in range(1, len(options) + 1):
            print("valid selection:" + str(options[main_input - 1]))
        else:
            seven_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
        turn[0] = 'b'
        if main_input == 1:
            available_cards = [i for i in player_b_hand if
                               i[0] in ('7', '8', '9', '10', 'J', 'Q', 'K', 'A')]
            player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
        else:
            available_cards = [i for i in player_b_hand if
                               i[0] in ('2', '3', '4', '5', '6', '7')]
            player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
    else:
        turn[0] = 'b'
        options = ['Higher','Lower']
        for i in range(len(options)):
            print(str(i + 1) + ":", options[i])
        main_input = int(input("Player B Please select higher or lower: "))
        if main_input in range(1, len(options) + 1):
            print("valid selection:" + str(options[main_input - 1]))
        else:
            seven_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
        turn[0] = 'a'
        if main_input == 1:
            available_cards = [i for i in player_a_hand if
                               i[0] in ('7', '8', '9', '10', 'J', 'Q', 'K', 'A')]
            player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)
        else:
            available_cards = [i for i in player_a_hand if
                               i[0] in ('2', '3', '4', '5', '6', '7')]
            player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def six_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if i[0] in('A','K','Q','J', '2', '3', '6', '7', '8', '9', '10')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_a_hand if i[0] in ('A','K','Q','J', '2', '3', '6', '7', '8', '9', '10')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def five_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):

    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if i[0] in('A','K','Q', '2', '3', '5', '6', '7', '8', '9', '10')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_a_hand if i[0] in ('A','K','Q', '2', '3', '5', '6', '7', '8', '9', '10')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def four_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):
    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if i[0] in('A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_a_hand if i[0] in ('A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

def three_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):


    if len(pile) == 1:
        top_card = []
        gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    if len(pile) == 2:
        if pile[-2][0] == '3':
            top_card = []
        else:
            top_card = pile[-2]
        gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    if len(pile) == 3:
        if pile[-2][0] == '3':
            if pile[-3][0] == '3':
                top_card = []
            else:
                top_card = pile[-3]
        else:
            top_card = pile[-2]
        gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        if pile[-2][0] == '3':
            if pile[-3][0] == '3':
                if pile[-4][0] == '3':
                    top_card = pile[-5]
                else:
                    top_card = pile[-4]
            else:
                top_card = pile[-3]
        else:
            top_card = pile[-2]

        gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def two_rules(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down):
    if turn[0] == 'b':
        available_cards = [i for i in player_b_hand if
                           i[0] in ('Q', 'K', 'A', '2', '3','4', '5', '6', '7', '8', '9', '10', 'J')]
        player_b_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)

    else:
        available_cards = [i for i in player_a_hand if
                           i[0] in ('Q', 'K', 'A', '2', '3','4', '5', '6', '7', '8', '9', '10', 'J')]
        player_a_gameplay(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


def starting_code():
    turn = ['a']
    pile = []
    top_card = []
    burn_pile = []
    available_cards = []
    initial_hand()
    initial_down()
    initial_up()
    start(pile,top_card,turn,burn_pile,player_a_hand,player_b_hand,available_cards,player_a_up,player_b_up,player_a_down,player_b_down)


if __name__=="__main__":
    starting_code()





# code transition to up cards - unstarted forecast 3 hours
# code transition to down cards - unstarted forecast 3 hours
# ability to play multiple cards at once - unstarted forecast 3 hours
# ability to play with multiple players - unstarted forecast 5 hours
# Add GUI - unstarted forecast 20 hours



# 4 cards in a row to clear deck
# code in more players



