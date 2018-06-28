#!/usr/bin/env python3

# Name:        Matthew Silva
# Class:       CSC 110 - Fall 2017
# Assignment:  Programming Project Design
# Due Date:    November 18, 2017

# Program Title:  The Game of SET
  
# Project Description and Solution:
# --------------------
# This program will play the game of SET.  The game will present the players
# a board of 12 unique SET Cards and prompt them to create a SET of 3 cards.
# The SET's cards must either be all the same or all different for each attribute.
# The players are then prompted to decide whether they want to find more SETs
# with different cards than previous chosen, get dealt a new board of Cards,
# or quit the game. They will pick cards until the game determines that all
# SETs have been chosen, at which point it will show who won and generate a new board.
#
# NOTE: I tried my best to implement all of the extra credit this assignment
# except for a player losing a turn when they choose an invalid set
#

# General Solution:
# -----------------
#  The implementation will entail several steps. First, the deck of set cards must be
#  generated. Python has the capability of creating new types of objects, so I have decided
#  that the deck will be an array of Card objects. Several nested for loops will likely
#  serve to generate Cards with every combination of attributes. Once the cards are
#  generated, a board of twelve Cards must be generated from the set of cards, taking care
#  not to put duplicate cards on the board. Then, the program must prompt the users to find
#  two SETs of three cards, ensuring that their input was valid before collecting the next
#  Card of the proposed SET. The proposed SET is then examined to see if it meets the
#  requirements of a SET. After this, the user is prompted for a decision between finding
#  a new SET different from old SETs found, getting dealt a new board of cards,
#  or quitting the game. The game will check after each round to see if any possible SETs
#  that have not been chosen remain. If not, the game will generate a new board and
#  explain who has found the most sets (won the game).

# Program:
# --------

# import needed for choosing random cards of deck to generate board
import random

# Takes no parameters and returns nothing
def printIntro():
    print("Choose a SET from the following cards.")
    print("A SET consists of three cards where each feature is EITHER the same on each card, or different on each card.")
    return


#An object that represents a Card in SET
class Card:
    """ Card class represents a card in Set"""
    
    # Parameter is the Card the method is called on (i.e. someCard.getNum())
    # Return the Card's number
    def __init__(self, num, color, shading, shape):
        self.number = num
        self.color = color
        self.shading = shading
        self.shape = shape
        
    # Parameter is the Card the method is called on (i.e. someCard.getColor())
    # Return the Card's color
    def getNum(self):
        return self.number
    
    # Parameter is the Card the method is called on (i.e. someCard.getShading())
    # Return the Card's shading
    def getColor(self):
        return self.color

    # Parameter is the Card the method is called on (i.e. someCard.getShape())
    # Return the Card's shape
    def getShading(self):
        return self.shading

    # Parameter is the Card the method is called on (i.e. str(someCard))
    # Returns the String representation of the card
    def getShape(self):
        return self.shape

    # Parameter is the Card the method is called on (i.e. str(someCard))
    # Returns the String representation of the card
    def __str__(self):
        return ("" + self.number + self.color + self.shading + self.shape)


# Takes no parameters and returns an array of 81 Cards
def generateDeck():
    deck = []
    numbers = ["1","2","3"] # These arrays are all the possible attributes of SET Cards
    colors = ["R","G","P"]
    shadings = ["S","O","P"]
    shapes = ["O","S","D"]
    for h in range(3): # These nested for loops traverse every possible Card attribute combination
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    newCard = Card(numbers[h],colors[i],shadings[j],shapes[k]) # Instantiate new Card
                    deck.append(newCard)
    return deck

# Takes a deck of SET Cards and returns an array of 12 unique Cards
def generateBoard(deck):
    board = []
    boardSize = 12
    currentCard = deck[random.randint(0,(len(deck) - 1))]
    board.append(currentCard)
    for i in range(boardSize - 1):
        while (currentCard in board):
            currentCard = deck[random.randint(0,(len(deck) - 1))]
        board.append(currentCard)
    return board
    
# Takes a board of SET Cards and returns nothing
# Prints that board in lines of 4
def displayBoard(board):
    i = 0
    while i < len(board):
        print("", board[i], board[i+1], board[i+2], board[i+3])
        i += 4
    return

# Returns True if the Card of the given string representation
# is in the given array of SET Cards.
# Returns False otherwise.
def strInDeck(string, deck):
    for card in deck:
        if string == str(card):
            return True
    return False

# Returns True if the 3 objects in the given array of chosen objects
# all have the same output or all have different outputs when the
# given method is applied to them.
# Returns False otherwise.
def allDiffOrSame(chosen, method):
    if (method(chosen[0]) == method(chosen[1]) == method(chosen[2])):
        return True
    elif (method(chosen[0]) != method(chosen[1])
          and method(chosen[1]) != method(chosen[2])
          and method(chosen[2]) != method(chosen[0])):
        return True
    else:
        return False

# Returns True if the given array of Chosen Cards is a SET
# Returns False otherwise
def isSet(chosen):
    if (allDiffOrSame(chosen, Card.getNum) == True
        and allDiffOrSame(chosen, Card.getColor) == True
        and allDiffOrSame(chosen, Card.getShading) == True
        and allDiffOrSame(chosen, Card.getShape) == True):
        return True
    else:
        return False

# Takes an array of SET Cards representing the board and an
# array of SET Cards representing Cards already chosen
# Also takes the list of scores and the current player's number (1 or 2)
# Returns the new array of chosen cards (new cards would be
# added if the new SET proposed by the player was valid)
# Also returns the new list of scores, which is modified if a player scored
def promptForSet(board, chosen, scores, playerNum):
    print("Player " + str(playerNum) +": Choose three cards that make a SET")
    validChoice = False
    newChosen = []
    i = 1
    while (i < 4):
        validChoice = False
        while (validChoice == False):
            choice = input("" + str(i) + ": ")
            if (strInDeck(choice, chosen) or  strInDeck(choice,newChosen)):
                print("You already chose that card, please try again")
            elif (strInDeck(choice, board) == False):
                print("Not a valid choice, please choose again")
            else:
                newChosen.append(Card(choice[0],choice[1],choice[2],choice[3]))
                validChoice = True
        i += 1
    if (isSet(newChosen)):
        print("Yes that is a SET")
        chosen.extend(newChosen)
        scores[playerNum - 1] += 1
        print("Player " + str(playerNum) + "'s score is now " + str(scores[playerNum - 1]))
        return chosen, scores
    else:
        print("Sorry, that is not a SET")
        return chosen, scores
    
# Takes the current board, the scores, and the deck.
# Returns True if an unchosen SET exists in the board
# Returns Falseif no unchosen SET exists in the board
def checkBoard(board, chosen):
    # Uses 3 nested while loops to try every combination of 3 Cards on the board
    i = 0
    while (i < len(board)):
        j = 0
        while (j < len(board)):
            if (j == i):
                j += 1
            k = 0
            while (k < len(board)):
                while (k == i or k == j):
                    k += 1
                if ( j < len(board) and k < len(board)):
                     next3 = [board[i], board[j], board[k]]
                     if (isSet(next3) and # If the current 3 Cards are a SET and they haven't been chosen, return True
                         not strInDeck(str(next3[0]), chosen) and
                         not strInDeck(str(next3[1]), chosen) and
                         not strInDeck(str(next3[2]), chosen)):
                       return True
                k += 1
            j += 1
        i += 1
    return False

# Takes no parameters and returns the decision of the user
def getDecision():
    print("What would you like to do next?")
    print("F - Find another SET")
    print("D - Deal another set of cards")
    print("Q - Quit")
    decision = input("==>")
    possibleDecisions = ["F","D","Q"]
    while (decision not in possibleDecisions):
        print("Not a vaild option, please enter again")
        decision = input("==>")
    return decision

# Takes the list of scores and prints the victor of the round
def printWinner(scores):
    if scores[0] > scores[1]:
        print("Player 1 won that round with " + str(scores[0]) + " point(s)!")
    elif scores[0] == scores[1]:
        print("It was a tie!")
        print("The score that round was " + str(scores[0]) + " to " + str(scores[0]) + "!")
    else:
        print("Player 2 won that round with " + str(scores[1]) + " point(s)!")

# Main Method
def main():
    printIntro()
    deck = generateDeck()
    board = generateBoard(deck)
    displayBoard(board)
    gameEnded = False
    chosen = []
    scores = [0,0]
    while (checkBoard(board, chosen) == False): # Check to make sure the board can be played
        print("The board did not have any SETs... Generating a new one...")
        board = generateBoard(deck)
        displayBoard(board)
    chosen, scores = promptForSet(board, chosen, scores, 1) # Get first actions from player 1 and 2
    chosen, scores = promptForSet(board, chosen, scores, 2)
    while (gameEnded != True):
        while (checkBoard(board, chosen) == False): # First check board for a SET
            print("No SETs are left!")              # and make end the current round if so
            printWinner(scores)
            scores = [0,0]
            print("Generating a new board...")
            board = generateBoard(deck)
            displayBoard(board)
        decision = getDecision()
        if (decision == "F"): # Prompts players for more choices
            chosen, scores = promptForSet(board, chosen, scores, 1)
            chosen, scores = promptForSet(board, chosen, scores, 2)
        elif (decision == "D"): # Prints the winner, creates a new board, and prompts for a SET
            printWinner(scores)
            board = generateBoard(deck)
            displayBoard(board)
            chosen = promptForSet(board, chosen, scores, 1)
            chosen = promptForSet(board, chosen, scores, 2)
        elif (decision == "Q"): # Ends the game
            printWinner(scores)
            print("Game Over - Thanks for Playing")
            gameEnded = True


if __name__ == "__main__":
    main()