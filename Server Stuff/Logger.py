from C:\Users\Cimara\Documents\GitHub\EECS393-RasPiHome\Client Stuff\myServer\piServer\models.py import User
from C:\Users\Cimara\Documents\GitHub\EECS393-RasPiHome\Client Stuff\myServer\piServer\models.py import Bulding
from C:\Users\Cimara\Documents\GitHub\EECS393-RasPiHome\Client Stuff\myServer\piServer\models.py import Outlet
from C:\Users\Cimara\Documents\GitHub\EECS393-RasPiHome\Client Stuff\myServer\piServer\models.py import Alarm
from django.db import models
from datetime import datetime
import sys

#to user the logger class effectively import imp
#and do the following line of code:
#   log =  imp.load_source('Logger', 'logger.py location')
#This should allow logger to be used easily. by making calls like:
#   log.log(0.0.0.0,bob,"I just turned something on.",0)
#in the code. These logging functions should not be seen by the user unless the Log.txt
#file is opened.

class logger(bID):
    #location will just be directly on the Pi when we can do that.
    location = "C:\Users\cimara\Desktop\test.txt,r+" #this is the location I currently am using
     def logAlarm(aID):
        a = Alarm.objects.filter(alarmID=aID)
        f = open(location, "a")
        timeStamp = datetime.datetime.now()
        f.write(timeStamp)
        f.write(a)
        f.close()
    def log(address,user,msg,flag):
        f = open(location, "a")
        if(flag == 0)
            f.write("info")
        if(flag == 1)
            f.write("error")
        if(flag == 2)
            f.write("warning")
        if(flag == 3)
            f.write("debug")
        f.write(address)
        f.write(user)
        f.write(msg)
        timeStamp = datetime.datetime.now()
        f.write(timeStamp)
        f.write("\n")
        f.close()
    def inputInvalid(msg):
        f = open (location, "a")
        f.write("The following input was invalid")
        f.write(msg)
        f.close()
    def killServer(address, user,msg,flag):
        self.log(address,user,"Server Died remotely",0)
        sys.exit("The Website Server was killed remotely")
        #change server status to Down or OFF
        #serverstatus flag in a file??? or the DB?
    
