import sys
#import Logger.py
import os
import sqlite3
import imp
import handler
#h = handler()
#handler = imp.load_source('Handler','C:\Users\Cimara\Documents\GitHub\EECS393-RasPiHome\Client Stuff\handler.py')
yes = 1
while(yes == 1):
    handler.checkAlarms()
    #log.checkServerStatus()
