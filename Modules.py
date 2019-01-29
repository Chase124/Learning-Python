
import sys
import time

print ("The Python version in this computer is" + sys.version)
print (str(time.time()) + " seconds has passed from the epoch of 1 january 1970 at 12:00am.")



def get_minutes():
    print ("The approximate number of min is " + str(time.time() / 60))

def  get_hours():
    print ("The approximate number of hours is " + str(time.time() / 60 / 60))

def get_days():
    print ("The approximate number of days is " + str(time.time() / 60 / 60 / 24))

def get_weeks():
    print ("The approximate number of weeks is " + str(time.time() / 60 / 60 / 24 / 7))

def get_years():
    print ("The approximate number of years is " + str(time.time() / 60 / 60 / 24 / 7 / 52))

def quit_message():
    print ('Bye Bye')

dict_switch = {'quit': quit_message, 'm': get_minutes,'minutes': get_minutes, 'h': get_hours, 'hours': get_hours, 'd': get_days, 'days': get_days, 'w': get_weeks, 'weeks': get_weeks, 'y': get_years, 'years': get_years}
# comment big blocks is '''   commented      '''
#1 - add the single char option to all the if statements
'''
if choiceOfTime == 'minutes' or choiceOfTime == 'm':
    print ("The approximate number of minutes is " + str(minutes))

elif choiceOfTime == 'hours':
    print ("The approximate number of hours is " + str(hours))

elif choiceOfTime == 'days':
    print ("The approximate number of days is " + str(days))

elif choiceOfTime == 'weeks':
    print ("The approximate number of weeks is " + str(weeks))

elif choiceOfTime == 'years':
    print ("The approximate number of years is " + str(years))
'''
#2 - Try to use switch case instead of the series of if elif statements

choiceOfTime = ''
while choiceOfTime != 'quit':

    print ("Would you like the epoch time in (m)inutes, (h)ours, (d)ays, (w)eeks or (y)ears?")

    choiceOfTime = raw_input()

    dict_switch[choiceOfTime]()