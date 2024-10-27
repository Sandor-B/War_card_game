#Made by Sandor Balogh
#This game goes on indefinitely, just like in the "war" card game present on the website shown in class (https://cardgames.io/war/)

# Import necessary modules
import random
import time

# Define the ranks and suits
ranks_list = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits_list = ("hearts", "diamonds", "clubs", "spades")

#Create an unshuffled deck of cards
deck = [(rank, suit) for rank in ranks_list for suit in suits_list]

print("Creating deck...")
time.sleep(2)

#Create a shuffled deck
random.shuffle(deck)

print("Shuffling deck...")
time.sleep(2)

#Seperate shuffled cards into 2 hands
hand1 = deck[:26]
storage_hand1 = []

hand2 = deck[26:53]
storage_hand2 = []

print("Splitting deck...")
time.sleep(2)
print(f"You have {len(hand1)} cards and the computer has {len(hand2)} cards.")
time.sleep(2)

def card_comparison(p1_card, p2_card, ranks_list):
    """This is the logic that compares two cards to find the stronger card
            Return 1 if player 1's card is strong, 2 for player 2
	    if the cards are equal, return 0.
    """
    if ranks_list.index(p1_card[0]) > ranks_list.index(p2_card[0]):
        return 1
    elif ranks_list.index(p1_card[0]) == ranks_list.index(p2_card[0]):
        return 0
    else:
        return 2


def play_round(player1_hand, storage_hand1, player2_hand, storage_hand2, ranks_list, num_rounds, deck):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    war_cards_pile = []
    print("--------------------------------------------")
    print(f"Round number {num_rounds} started!")
    time.sleep(2)
    print(f"Computer plays {player2_hand[0]} and you play {player1_hand[0]}")
    time.sleep(3)
    round_result = card_comparison(player1_hand[0], player2_hand[0], ranks_list)
    if round_result == 1:
        storage_hand1.append(player2_hand.pop(0))
        storage_hand1.append(player1_hand.pop(0))
        print(f"You win! You gain the computer's card.")
        time.sleep(2)
    elif round_result == 2:
        storage_hand2.append(player1_hand.pop(0))
        storage_hand2.append(player2_hand.pop(0))
        print(f"You lose. The computer gains your card.")
        time.sleep(2)
    else:
        print(f"Both of you have equally strong cards! Beginning war scenario...")
        time.sleep(3)
        war(player1_hand, storage_hand1, player2_hand, storage_hand2, ranks_list, war_cards_pile, deck)

def war(player1_hand, storage_hand1, player2_hand, storage_hand2, ranks_list, temporary_cards_list, deck):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    if (len(player1_hand) < 4) or (len(player2_hand) < 4):
        if len(temporary_cards_list) != 0:
            for _ in range(len(temporary_cards_list)): deck.append(temporary_cards_list.pop(0))
        play_game(hand1, hand2, storage_hand1, storage_hand2, deck)
    
    for _ in range(3):
        temporary_cards_list.append(player1_hand.pop(0))
        temporary_cards_list.append(player2_hand.pop(0))
    print("--------------------------------------------")
    print(f"Both you and the computer place down 3 cards in a pile. The pile has {len(temporary_cards_list)} cards.")
    time.sleep(3)
    print(f"The computer now puts down a {player2_hand[0]} and you put down a {player1_hand[0]}.")
    time.sleep(3)
    war_result = card_comparison(player1_hand[0], player2_hand[0], ranks_list)
    
    if war_result == 1:
        storage_hand1.append(player2_hand.pop(0))
        storage_hand1.append(player1_hand.pop(0))
        for _ in range(len(temporary_cards_list)):
            storage_hand1.append(temporary_cards_list.pop(0))
        print(f"You win! You gain all the cards put in the pile and the computer's card.")
        time.sleep(2)
        
    elif war_result == 2:
        storage_hand2.append(player1_hand.pop(0))
        storage_hand2.append(player2_hand.pop(0))
        for _ in range(len(temporary_cards_list)):
            storage_hand2.append(temporary_cards_list.pop(0))
        print(f"You lose. The computer gains all the cards put in the pile and your card.")
        time.sleep(2)
    else:
        print("Both cards are equal. Restarting war scenario. Played cards are added to the pile.")
        time.sleep(3)
        temporary_cards_list.append(player1_hand.pop(0))
        temporary_cards_list.append(player2_hand.pop(0))
        war(player1_hand, storage_hand1, player2_hand, storage_hand2, ranks_list, temporary_cards_list, deck)

def play_game(hand1, hand2, storage_hand1, storage_hand2, deck):
    """Main function to run the game."""
    num_rounds = 0
    while (len(hand1) > 4) or (len(hand2) > 4):
        num_rounds += 1
        play_round(hand1, storage_hand1, hand2, storage_hand2, ranks_list, num_rounds, deck)
    print("Insufficient cards in one of the hands (insufficient as in not enough for a potential war scenario). Re-distributing all cards.")
    time.sleep(3)
    if len(storage_hand1) > len(storage_hand2):
        print("The winner of the game is player 1 (you), since they won more cards! Congratulations!")
        time.sleep(2)
    elif len(storage_hand1) < len(storage_hand2):
        print("The winner of the game is player 2 (computer), since they won more cards! Better luck next game!")
        time.sleep(2)
    else:
        print("It's a draw! Both players ended with the same amount of cards won during the game. Restarting...")
        time.sleep(3)
    for _ in range(len(storage_hand1)): deck.append(storage_hand1.pop(0))
    for _ in range(len(storage_hand2)): deck.append(storage_hand2.pop(0))
    random.shuffle(deck)
    hand1 = deck[:26]
    hand2 = deck[26:53]
    play_game(hand1, hand2, storage_hand1, storage_hand2, deck)
    
# Call the main function to start the game
play_game(hand1, hand2, storage_hand1, storage_hand2, deck)
