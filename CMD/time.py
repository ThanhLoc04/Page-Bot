import time;
import calendar

period=time.asctime(time.localtime(time.time()))

cal=calendar.month(2024,11)
localtime=time.localtime (time.time())

year,month,day,hour, minute=localtime[0:5]
print( """_____________________\n|\n|Today's Date is 🌍\n_____
""",'⏰ Time|'+ str(hour)+":"+str(minute),"\n","🗺️ Date|"+str(month)+":"+str(day), '\n|\n_____Calender📜_______\n|'+cal+'\n|_____________________\n|', period[0:11],'\n______________________')
