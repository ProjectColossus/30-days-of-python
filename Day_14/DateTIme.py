## Python got datetime Module to handle date and time

import datetime
print(dir(datetime)) ## with this command it lets u known what are some of the built in commands


#1 Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
x = datetime.now()
print(x)
day = x.day
year = x.year
month = x.month
hour = x.hour
Second = x.second
minute = x.minute
timestamp = x.timestamp()
print("Timestamp", timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}:{Second}")


#2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# in this We will BE using the Strftime Method which is used to format date objects into readable strings
## ("%m/%d/%Y, %H:%M:%S") -- mm/dd/yy H:M:S format 

from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")
print("Time:", time)
date_and_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time: ",date_and_time)


#3 Today is 5 December, 2019. Change this time string to time
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string) 

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     

#4 Calculate the time difference between now and new year.

from datetime import datetime, date

year_now = date(month=8,year=2026,day=20)
new_year = date(month=1,year=2027,day=1)
time_left_for_newyear = new_year - year_now
print("Time Left For New Year:",time_left_for_newyear)

#5  Calculate the time difference between 1 January 1970 and now.

from datetime import date, datetime
date_given = date(1970,1,1) ## Year, month ,day
today = date.today()
difference = today - date_given
print(f"Days Since 1 jan 1970: {difference}")   

## datetime Module is USed in 
# Time Series Analysis == Store and compare dates/times of data points
#Activity timestamps == Record exactly when a user logged in, uploaded a file, etc.
#Blog posts ==	Store when a post was published



#Calender Module
import calendar

month,day , year = map(int,input().split())
days = calendar.weekday(year,month,day)

week = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
#since the output is given in index so initiated a list 

print(week[days]) #prints the weekday when the output is given from days