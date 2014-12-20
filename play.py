#!/usr/bin/python
# -*- coding:utf-8 -*-

# This is a simple turn based game, where players move around and trade itmes to
# make money. The winner is the first person to have £100 at the market.

# Players have locations, items and money
# items have value
# locations have names, items and travel options


from random import randint

import time
import pickle

#import inputbox
import sys
from classes import *
from setup2 import *
from others import *



def saveGame(playerList,itemList,locationList):
    gamestate = [playerList,itemList,locationList]

    with open('savefile.dat', 'wb') as file:
        pickle.dump(gamestate, file, protocol=2)

def loadGame():
    with open('savefile.dat', 'rb') as file:
        gamestate = []
        gamestate = pickle.load(file)
        playerList = gamestate[0]
        itemList = gamestate[1]
        locationList = gamestate[2]

    return (playerList, itemList, locationList)


def turn(activePlayer,playerList,itemList,locationList):


    if(activePlayer.money > 500):
        activePlayer.winner()

    if(activePlayer.location.banditHere == True):
        if(activePlayer.money > 0):
            if (activePlayer.robbed == False):
                activePlayer.location.bandits()
                activePlayer.robbed = True
            else:
                pass
        else:
          pass
    else:
        pass



    print "Do you want to: "

    print(", ".join(activePlayer.location.actionOptions)) + " " + "or Pass?"

    '''if(activePlayer.location.name == 'market'):
        if(len(activePlayer.items) > 0):
            activePlayer.riches()
            print "Do you want to look, move or sell an item?"

        else:
            print "Do you want to look or move?"

    else:
        print "Do you want to look or move?"'''

    action = raw_input('>')
    if "look" in action:
        activePlayer.location.look(activePlayer)
    elif "move" in action:
        activePlayer.move()
    elif "sell" in action:
        if not (activePlayer.location.name == 'market'):
            print "You are not at the market, you can't sell anything here."
            turn(activePlayer, playerList, screen, itemList, locationList)

        if(len(activePlayer.items) == 0):
            print "You haven't got anything to sell."
            turn(activePlayer, playerList, screen, itemList, locationList)
        else:
            activePlayer.sell()

    elif "inv" in action:
        activePlayer.printInv()
        turn(activePlayer,playerList,screen,itemList,locationList)
    elif "who" in action:
        activePlayer.location.steal(playerList,activePlayer)
        turn(activePlayer,playerList,screen,itemList,locationList)
    elif "save" in action:
        saveGame(playerList,itemList,locationList)
        print "Game Saved"
    elif "quit" in action:
        print "Goodbye"
        exit()
    elif "pass" in action:
        print "OK"
        turn(activePlayer,playerList,screen,itemList,locationList)
    else:
        print "Sorry that's not an option."
        turn(activePlayer,playerList,screen,itemList,locationList)

    print "End of your turn"
    print "---------------------------"
    time.sleep(3)
    return

def main ():



    print 'Welcome to Trade IT. Be the first person to make £500 to be the winner!'

    print 'Do you want to load a game? y/n'
    a = raw_input('>  ')
    if 'y' in a:
        try:
            playerList, itemList, locationList = loadGame()
            #print playerList[0].name
            play(playerList,itemList,locationList)
        except IOError:

            print "Error finding save game file, starting new game.\n"
    elif 'n' in a:
        print 'Ok, lets start a new game'

    else:
        print "I don't undertstand?"
        main()

    itemList = setupItems()

    print('--------------------')

    locationList = setupLocations(itemList)



    print 'How many players do we have today?'

    noOfPlayers = numPlayers()


    print 'Thank you, we have %s players in this game.' % noOfPlayers
    playerList = [] # create the player list
    gameplayers = 0
    while gameplayers < noOfPlayers:
        x = gameplayers+1 #using x to calcualte the human understandable player number which does not start at zero!
        print "Whats your name player %s?" % x
        name = raw_input('> ')
        newPlayer = Player(name) # create a new player object using the name input by the player
        newPlayer.location = locationList['lipon'] # start the player at the house
        playerList.append(newPlayer)
        gameplayers = gameplayers + 1


    print '------------------'

    print 'Today we have these players:'
    for player in playerList:
        print player

    play(playerList,itemList,locationList)

def play(playerList,itemList,locationList):

    activePlayerIndex = 0
    while True:
        print "It's your turn  "+playerList[activePlayerIndex].name+". You are at " + playerList[activePlayerIndex].location.name
        print playerList[activePlayerIndex].location.description

        turn(playerList[activePlayerIndex],playerList,itemList,locationList)

        activePlayerIndex = activePlayerIndex+1
        if(activePlayerIndex == len(playerList)):
            activePlayerIndex = 0



main() # start the game
