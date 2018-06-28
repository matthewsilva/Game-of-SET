# Name:        Matthew Silva
# Class:       CSC 110 - Fall 2017
# Assignment:  Programming Project Design
# Due Date:    November 18, 2017

# Program Title:  The Game of SET
  
# Project Description and Solution:
# --------------------
# This program will play the game of SET.  The game will present the player
# a board of 12 unique SET Cards and prompt them to create a SET of 3 cards.
# The SET's cards must either be all the same or all different for each attribute.
# The player is then prompted to decide whether they want to find more SETs
# with different cards than previous chosen, get dealt a new board of Cards,
# or quit the game.

# General Solution:
# -----------------
#  The implementation will entail several steps. First, the deck of set cards must be
#  generated. Python has the capability of creating new types of objects, so I have decided
#  that the deck will be an array of Card objects. Several nested for loops will likely
#  serve to generate Cards with every combination of attributes. Once the cards are
#  generated, a board of twelve Cards must be generated from the set of cards, taking care
#  not to put duplicate cards on the board. Then, the program must prompt the user to find
#  a SET of three cards, ensuring that their input was valid before collecting the next
#  Card of the proposed SET. The proposed SET is then examined to see if it meets the
#  requirements of a SET. After this, the user is prompted for a decision between finding
#  a new SET different from old SETs found, getting dealt a new board of cards,
#  or quitting the game.
#
#  NOTE: I have implemented the project as well and included it with this submission


# Pseudocode:
# -----------
# def main():
#   Display the intro text
#   Generate the full deck of 81 Cards
#   Generate a board of 12 unique Cards from the deck
#   Display the board
#   Allow the user to select 3 Cards from the board to propose a SET
#   If the SET was valid, record the 3 cards as being chosen
#   While the game hasn’t ended:
#       Get the user’s decision
#       If the user wants to chose another SET:
#           Allow the user to select 3 unchosen Cards from the board to propose a SET
#           If the SET was valid, record the 3 cards as being chosen
#       If the user wants to be dealt a new board:
#           Generate a new board of 12 unique Cards from the deck
#           Display the board
#           Allow the user to select 3 unchosen Cards from the board to propose a SET
#           If the SET was valid, record the 3 cards as being chosen
#       If the user wants to quit the game:
#           Print Game Over message
#           The game is now ended

# Function Design:
# ----------------

# import needed for choosing random cards of deck to generate board
import random

# Takes no parameters and returns nothing
def printIntro():
    #Print all the intro text for the game
    return


#An object that represents a Card in SET
class Card:
    
    def __init__(self, num, color, shading, shape):
        # Initializes the Card with a number, color, shading, and shape
        
    # Parameter is the Card the method is called on (i.e. someCard.getNum())
    # Return the Card's number
    def getNum(self):
        return self.number
    
    # Parameter is the Card the method is called on (i.e. someCard.getColor())
    # Return the Card's color
    def getColor(self):
        return self.color
    
    # Parameter is the Card the method is called on (i.e. someCard.getShading())
    # Return the Card's shading
    def getShading(self):
        return self.shading
    
    # Parameter is the Card the method is called on (i.e. someCard.getShape())
    # Return the Card's shape
    def getShape(self):
        return self.shape
    
    # Parameter is the Card the method is called on (i.e. str(someCard))
    # Returns the String representation of the card
    def __str__(self):
        return ("" + self.number + self.color + self.shading + self.shape)
    

# Takes no parameters and returns an array of 81 Cards
def generateDeck():
    # Generate a deck of every possible unique card of SET
    return deck

# Takes a deck of SET Cards and returns an array of 12 unique Cards
def generateBoard(deck):
    # Generate a board of 12 Card objects from the deck with
    # no duplicates
    return board

# Takes a board of SET Cards and returns nothing
def displayBoard(board):
    # Print each Card in the board, four in each row
    return

# Returns True if the Card of the given string representation
# is in the given array of SET Cards.
# Returns False otherwise.
def strInDeck(string, deck):
    # For every Card in the given deck, if the string representation
    # of a Card matches the string given, return True
            return True
    # If no matching Cards were found in the given deck, return False
    return False

# Returns True if the 3 objects in the given array of chosen objects
# all have the same output or all have different outputs when the
# given method is applied to them.
# Returns False otherwise.
def allDiffOrSame(chosen, method):
    # If the 3 objects in the array all have the same result when the given method
    # is applied, return True
        return True
    # Else if the 3 objects in the array all have different results when the given method
    # is applied, return True
        return True
    # Otherwise return False
        return False

# Returns True if the given array of Chosen Cards is a SET
# Returns False otherwise
def isSet(chosen):
    # If the chosen proposed SET of 3 cards are are appropriately all different or
    # all the same for each attribute, return True
        return True
    # Otherwise return False
        return False

# Takes an array of SET Cards representing the board and an
# array of SET Cards representing Cards already chosen
# Returns the new array of chosen cards (new cards would be
# added if the new SET proposed by the player was valid)
def promptForSet(board, chosen):
    # Prompt the user for 3 Cards from the board, repeating the
    # prompt if they enter invalid, repeated, or previously chosen
    # Cards.
    # Print whether the proposed 3 Card SET was really a SET
    # If so, add those 3 Cards to the chosen Cards
    return chosen

# Takes no parameters and returns the decision of the user
def getDecision():
    # Prints the possible decisions and takes the user's
    # decision as string input
    # Keeps taking input until it is a valid choice
    return decision


def main():
    # The main function implements the pseudocode by using the functions defined above.
