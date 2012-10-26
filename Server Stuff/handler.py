from C:\Users\Anthony\Documents\GitHub\EECS393-RasPiHome\Client Stuff\myServer\piServer\models.py import User
from C:\Users\Anthony\Documents\GitHub\EECS393-RasPiHome\Client Stuff\myServer\piServer\models.py import Building
from C:\Users\Anthony\Documents\GitHub\EECS393-RasPiHome\Client Stuff\myServer\piServer\models.py import Outlet
from C:\Users\Anthony\Documents\GitHub\EECS393-RasPiHome\Client Stuff\myServer\piServer\models.py import Alarm
from django.db import models
from datetime import datetime
from logger.py import log, logAlarm, logTimer, checkServerStatus
import sys

class handler(bID):
	building = Building.objects.get(pk=bID)
	user = building.userID
	def flipState(oID):
		outlet = Outlet.objects.get(pk=oID)
		outlet.state = not outlet.state
		outlet.save()
		#call hardware code to actually flip
		#if actual flip was successful
		log(user.lastAddress, user.username, "".join(["Outlet ", outlet.outletName, " was switched from ", "off" if outlet.state else "on", " to ", "on" if outlet.state else "off"]), 0)
		#else
		#log(user.lastAddress, user.username, "".join(["Outlet ", outlet.outletName, " was not switched due to a hardware error"]), 1)
	def checkAlarms():
		alarms = Alarm.objects.filter(buildingID=bID)
		for alarm in alarms:
			if alarm.startTime is None
				checkTimer(alarm)
			else
				checkAlarm(alarm)
	def checkTimer(timer):
		if datetime.datetime.now() >= timer.endTime
			flipState(timer.outletID)
			logTimer(timer.pk)
			#timer.delete()
	def checkAlarm(alarm):
		if datetime.datetime.now() >= alarm.endTime
			outlet = Outlet.objects.get(pk=alarm.outletID)
			if outlet.state is not desiredState
				flipState(alarm.outletID)
				logAlarm(alarm.pk, true)
			else
				logAlarm(alarm.pk, false)
			#alarm.delete()
	def killServer():
		if building.onlineState is False
			log(user.lastAddress, user.username, "The building associated with these alarms is no longer online... Shutting down", 0)
			sys.exit("The building associated with these alarms is no longer online... Shutting down")