#!/usr/bin/python
# -*- coding:utf-8 -*-
#TODO - create some locations manuallynto add in different
#fuctions - as subclasses of Location?

from random import randint, choice
from classes import *



def numPlayers():
    while True:
        try:
            noOfPlayers = int(raw_input('>'))
            print "Thanks"
            return noOfPlayers

        except:
            print "What??"


def textArea():
    pygame.init()
    width, height = 800, 50
    inputarea = pygame.display.set_mode((width, height))
    return inputarea

def setupItems():

    itemList = [] # create a blank list for the item ojects

    itemDefinitionDict=[ # create a list of dictionaries for each object to be created.
    { 'name':'Key',
        'value':50,
        'weight':100 },

    {'name':'Jewel',
        'value':90,
        'weight':100},

    {'name':'axe',
        'value':30,
        'weight':100},
    {'name':'phone',
        'value':50,
        'weight':100},

    {'name':'computer',
        'value':50,
        'weight':100}
    ]

     # the for loop below goes through the dictionary of items
    # and creates objects for each item in the dictionary

    for each in itemDefinitionDict:
        tempItem = Item(each['name'],each['value'],each['weight'])
        itemList.append(tempItem)

    return itemList




def setupLocations(items):
    # a list of dictionaries if attributes for the location
    locationdefinitionlist = [
    {'name':'lipon',
    'description':"Lipon is a rough border town, careful who you make friends with here.",
    'cords':(60,270)},

    {'name':'bridge',
    'description':"You are on the west side of the bridge over the mighty river Ukilee. In the \
    distance you can see the mighty misty mountains of Meridethium.",
    'cords':(307,227)},

    {'name':'Bilong farm',
    'description':"This is a rather run down farm with a lof of broken machineary and some loanley sheep.",
    'cords':(301,393)},

    {'name':'market',
    'description':'Here its always market day, people buy, people sell and all have a great time.',
    'cords':(426,519)},

    {'name':'cave',
    'description':'This is the dark smuglers cave. Well done for finding it. There is often treasure left here \
    by bandits',
    'cords':(112,495)},


     {'name':'Ukileemouth',
    'description':'This is bridge over the mouth of the River and the gateway to the tropical lands.',
    'cords':(481,491)}

    ]

# create the standard locations
    locationDict = {} # a dictionary of names and location objects associated.
    for each in locationdefinitionlist:
        tempLocation = Location(each['name'],each['description'],each['cords'])
        locationDict[each['name']] = tempLocation
        #print tempLocation.cords

# add 'sell' to the market options
    locationDict['market'].actionOptions.append("Sell")

# Create the ancient locations

    anchientLocationDefinitionlist = [
    {'name':'Desert',
    'description':"This is the Ancient Desert, may relics can be found here.",
    'cords':(500,500)},

    {'name':'Folobula Forest',
    'description':"This is the Ancinet Forest of Folobula with many special things.",
    'cords':(30,357)},

    ]
    for each in anchientLocationDefinitionlist:
        tempLocation = Ancient(each['name'],each['description'],each['cords'])
        locationDict[each['name']] = tempLocation

# allocate the destinations for each location

    liponDestinations = [locationDict['Bilong farm'],locationDict['bridge'],locationDict['Folobula Forest']]
    for dest in liponDestinations:
        locationDict['lipon'].destinations.append(dest)

    farmDestinations = [locationDict['lipon'],locationDict['market']]
    for dest in farmDestinations:
        locationDict['Bilong farm'].destinations.append(dest)

    bridgeDestinations = [locationDict['lipon']]
    for dest in bridgeDestinations:
        locationDict['bridge'].destinations.append(dest)

    marketDestinations = [locationDict['Bilong farm'], locationDict['Folobula Forest']]
    for dest in marketDestinations:
        locationDict['market'].destinations.append(dest)

    forestDestinations = [locationDict['market'],locationDict['Desert']]
    for dest in forestDestinations:
        locationDict['Folobula Forest'].destinations.append(dest)

     #randomly set bandits, create the temporaty blist and remove
     #the market before making the selection
    blist = []

    for name, loc in locationDict.items():
        blist.append(loc)
        #print loc.name
    for loc in blist:
        if loc.name == 'market':
            blist.remove(loc)

    banditLocation = choice(blist)
    banditLocation.banditHere = True
    #print "bandits are in %s " % banditLocation.name



    # Ramdonly allocate the items
    itemListIndex=0

    for item in items:
            x = choice(locationDict.keys())
            b = locationDict.get(x)  # retreives the value for a given key.
            b.items.append(item)

    return locationDict
