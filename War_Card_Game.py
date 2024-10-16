 # Import necessary modules
import random

# Define the ranks and suits
ranks_list = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
suits_list = ("hearts", "diamonds", "clubs", "spades")

#Create an unshuffled deck of cards
deck = []
for suits in range(0, len(suits_list)):
    for ranks in range(0, len(ranks_list)):
        deck.append((suits_list[suits], ranks_list[ranks]))

#Create a shuffled deck
shuffled_deck = []
for cards in range(0, len(deck)):
    card_selected = random.choice(deck)
    shuffled_deck.append(card_selected)
    deck.pop(deck.index(card_selected))

#Seperate shuffled cards into 2 hands
hand1 = []
for cards in range(0, int(len(shuffled_deck)/2)):
    hand1.append(shuffled_deck[cards])

hand2 = []
for cards in range(0, int(len(shuffled_deck)/2)):
    hand2.append(shuffled_deck[cards + 26])

def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
            Return 1 if player 1's card is strong, 2 for player 2
	    if the cards are equal, return 0.
    """
    if ranks_list.index(p1_card[1]) > ranks_list(p2_card[1]):
        return 1
    elif ranks_list.index(p1_card[1]) == ranks_list(p2_card[1]):
        return 0
    else:
        return 2


def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    round_result = card_comparison(player1_hand[0], player2_hand[0])
    if round_result == 1:
        player1_hand.append(player2_hand[0])
        player2_hand.pop(0)
    elif round_result == 2:
        player2_hand.append(player1_hand[0])
        player1_hand.pop(0)
    else:
        war(player1_hand, player2_hand)

def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    temporary_cards_list = []
    for cards in range(0, 3):
        temporary_cards_list.append(player1_hand[0])
        player1_hand.pop(0)
        temporary_cards_list.append(player2_hand[0])
        player2_hand.pop(0)
    war_result = card_comparison(player1_hand[0], player2_hand[0])
    if round_result == 1:
        player1_hand.append(player2_hand[0])
        for cards in range(0, len(temporary_cards_list)):
            player1_hand.append(temporary_cards_list[0])
            temporary_cards_list.pop(0)
        player2_hand.pop(0)
    elif round_result == 2:
        player2_hand.append(player1_hand[0])
        for cards in range(0, len(temporary_cards_list)):
            player2_hand.append(temporary_cards_list[0])
            temporary_cards_list.pop(0)
        player1_hand.pop(0)

def play_game():
    """Main function to run the game."""
    while (len(hand1) != 0) or (len(hand2) != 0):
        play_round(hand1, hand2)

# Call the main function to start the game
play_game()
    
    
    
    
        

