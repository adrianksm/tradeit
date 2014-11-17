#!/usr/bin/python
# -*- coding:utf-8 -*-
def getInt(min,max):
    while True:
        try:
            choice = int(raw_input('>'))
            #choice = int(inputbox.askInt(screen, ':'))
            if choice == 99:
                return choice
            if(choice>=min and choice<=max):

                return choice
        except:
            print "Sorry, that's not a valid choice"
            return