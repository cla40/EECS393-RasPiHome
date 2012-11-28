import handler.py
import sys
#import Logger.py
import os
import sqlite3

buildingID = sys.argv[1]
h = handler(buildingID)
yes = 1
while(yes == 1):
    h.checkAlarms()
    log.checkServerStatus()
