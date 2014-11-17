#!/usr/bin/python
# -*- coding:utf-8 -*-
from others import *
import random
import time

class Player(object):
    """sets up players"""
    def __init__(self,name):
        self.name = name
        self.money = 0
        self.location = '' # location object
        self.items = []
        self.robbed = False

    def __str__(self):
        return self.name

    def printInv(self):
        if len(self.items)==0:
            print "You have no items"

        if len(self.items)>0:
            print "You are holding:" + "\n"
            for item in self.items:
                print item.name + " and it's value is %s "  % item.value
                print "And you have %s gold coins" % self.money
        return

    def riches(self):
        total = 0
        for item in self.items:
            total = total + item.value
        print "You items are worth %s gold pieces." % total
        #print '\n'
        print "You are carrying %s gold pieces." % self.money

    def sell(self):
        pass


    def winner(self):
        print "Congratulations %s, you are the WINNER!" % self.name
        print '\n'
        print " ***  GAME OVER!  ***"
        exit()

    def move(self):
        print "Where do you want to go?"
        for index,dest in enumerate(self.location.destinations):
            print `index` + ': '+ dest.name
        choice = getInt(0,len(self.location.destinations)-1)


        nextLocation = self.location.destinations[choice]
        print 'Off you go to %s ' % nextLocation.name
        print '--------------'
        self.location = nextLocation
        return

    def sell(self):

        self.printInv()
        print "What do you want to sell to the market dealer?"
        for index,item in enumerate(self.items):
            print `index` + ': ' + item.name

        sellChoice = getInt(0,len(self.items)-1)

        soldItem = self.items[sellChoice]
        print "You chose to sell the %s  " % soldItem.name

        self.money = self.money + soldItem.value
        self.items.remove(soldItem)
        return False

class Item(object):
    """Sets up Items"""
    def __init__(self,name,value,weight):
        self.name = name
        self.value = value
        self.weight = weight
        self.capacity = 0

class Relic(Item):
    def __init__(self,name):
        self.name = name
        self.value = random.choice([50,50,50,50,100,100,250,500])
    def __str__(self):
        return self.name

class Location(object):
    """Lots of Location objects, all with names and destination, descrpitions, items and potentially bandts"""
    def __init__(self, name, description,cords):
        self.name = name
        self.destinations = []
        self.description = description
        self.items = []
        self.banditHere = 0
        self.cords = cords
        self.old = False
        self.actionOptions =["Look","Move"]

    def bandits(self):
        print "There are bandits here!"
        print "They have stolen half your gold."
        self.money = self.money / 2
        print "You now have %s gold" % self.money
        return()


    def steal(self,playerList,activePlayer):
        players_here = []
        for player in playerList:
            if player.location.name == self.name:
                players_here.append(player)


        for x in players_here:
            if x == activePlayer:
                players_here.remove(x)
        if len(players_here) == 0:
            print 'nobody here'
        return()

        for x in players_here:
            print "You are here with %s " % player.name


        print "You can attempt to rob a player, but it's risky."
        print "Do you want to rob:"
        for index,player in enumerate(players_here):
            print `index` + ': ' + player.name
        choice = int(raw_input("> "))
        chosenPlayer = players_here[choice]
        print "You chose to rob %s " % chosenPlayer.name
        chosenPlayer.money = chosenPlayer.money / 2
        activePlayer.money = activePlayer.money + chosenPlayer.money
        print "You have %s gold coins " % activePlayer.money

        return()

    def look(self,activePlayer):
        print "%s, you are at the %s " % (activePlayer.name, self.name)
        print '\n'
        print self.description
        print '\n'
        print "You look around and see:"
        if len(self.items)<1:
            print "There is nothing here"
            pass
        else:
            for item in self.items:
                print item.name
            print 'Do you want to take anything?'
            for index,item in enumerate(self.items):
                print `index` + ': '+ item.name
            print '99' + ': Choose nothing'
            choice = getInt(0,len(self.items)-1)
            if choice == 99:
                print "ok doing nothing"
                return

            chosenItem = self.items[choice]
            print "You chose to take the %s " % chosenItem.name
            activePlayer.items.append(chosenItem)
            self.items.remove(chosenItem)
            activePlayer.printInv()
            activePlayer.riches()


        return

class Ancient(Location):
    """Create the and Ancient site"""
    def __init__(self, name, description,cords):
        #super(Location, self).__init__()
        self.name = name
        self.description = description
        self.cords = cords
        self.relics = 5
        self.destinations = []
        self.items = []
        self.banditHere = False
        self.old = True
        self.actionOptions =["Look","Move"]

    def look(self,activePlayer):
        if self.relics == 0:
            print "No more treasures to be found"
            return

        print "%s, you are at a special site with Ancient Relics " % activePlayer.name
        print '\n'
        print self.description
        print "There are %s relics remaining to find here" % self.relics
        print "Do you want to search for a relic? Y/N"
        action = raw_input("> ")
        if 'y' in action:
            a = random.randint(1,10)
            if a<5:
                print 'You search and search and find.....'
                time.sleep(3)
                self.relics -=1
                a = Relic("An Ancient Relic")
                print a
                activePlayer.items.append(a)
            else:
                print "You search around and find....."
                time.sleep(3)
                print 'Nothing! Better luck next tiem'
        elif 'n' in action:
            pass
        else:
            print 'Sorry, I do not understand that.'
            look (self,activePlayer)
