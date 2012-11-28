
from datetime import datetime
#import Logger
import sys
import imp
import sqlite3

class handler():
        import sqlite3

        createDB = sqlite3.connect("myDatabase")

        query = createDB.cursor()
        query.execute('SELECT SQLITE_VERSION() ')
        data = query.fetchone()
         
        bID = 1
	buildings = query.execute('SELECT * FROM piServer_building WHERE id = %s' % bID)
	for building in buildings:
                owner = building[1]
                print ("YO I AM PRINT THE OWNER I THINK %s" ,owner)
	user = query.execute('SELECT * FROM piServer_userprofile WHERE user = %s' % owner)
	def flipState(oID):
		outlet = query.execute('SELECT * FROM piServer_outlet WHERE id = %s' % oID)
		outletNewState = outlet[0].state
		query.execute('UPDATE piServer_outlet SET state = ? WHERE id = ?',(outletNewState,outlet[0].id))
                createDB.commit()
		#call hardware code to actually flip
		#if actual flip was successful
		print "YO STATE CHANGE"
		#log(user.lastAddress, user.username, "".join(["Outlet ", outlet.outletName, " was switched from ", "off" if outlet.state else "on", " to ", "on" if outlet.state else "off"]), 0)
		#else
		#log(user.lastAddress, user.username, "".join(["Outlet ", outlet.outletName, " was not switched due to a hardware error"]), 1)
	def checkAlarms():
                alarms = query.execute('SELECT * FROM piServer_alarm WHERE id = %s' % bID)
		for alarm in alarms:
                        startTime = alarm["startTime"]
			if startTime == None:
				checkTimer(alarm)
			else:
				checkAlarm(alarm)
	def checkTimer(timer):
		if datetime.datetime.now() >= timer.endTime:
			flipState(timer.outletID)
			#logTimer(timer.pk)
			#timer.delete()
	def checkAlarm(alarm):
		if datetime.datetime.now() >= alarm["endTime"]:
                        oID = alarm["outletID"]
			outlets = query.exectue('SELECT * FROM piServer_outlet WHERE id = ?',oID)
                        for outlet in outlets:
                                state = outlet["state"]
			if state is not alarm["desiredState"]:
				flipState(oID)
				#logAlarm(alarm.pk, true)
			else:
				#logAlarm(alarm.pk, false)
			#alarm.delete()
#	def killServer():
#               buildings = query.execute('SELECT * FROM piServer_building WHERE id = ?',bID)
#               for building in buildings:
#                       if building["onlineState"] is False:
                                #log(user.lastAddress, user.username, "The building associated with these alarms is no longer online... Shutting down", 0)
                                sys.exit("The building associated with these alarms is no longer online... Shutting down")
