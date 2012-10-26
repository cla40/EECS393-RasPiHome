import handler.py
import sys
import logger.py

buildingID = sys.argv[1]
h = handler(buildingID)
yes = 1
while(yes == 1):
    h.checkAlarms()
    log.checkServerStatus()
