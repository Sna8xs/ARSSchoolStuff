# VertretungsplanApi
This is a Python library which is for getting the 'Vertretungsplan' from the ARS

This script uses the [requests](https://pypi.org/project/requests/) and [bs4](https://pypi.org/project/beautifulsoup4/) library, so these need to be installed


The ```plan.getToday``` and ```plan.getTomorrow``` functions return a list containing lists. 

Like this:
```data = [[day, date, hour, room, type, subject, teacher, ver teacher, task],[day, date, hour, ...]...]```

Simple example:
```python
import Vertretungsplan # imports library

link1 = "https://adolf-reichwein-schule.de/fileadmin/home/nichtImMenue/vertretungsplan/schueler/heute/subst_001.htm" # link for today
link2 = "https://adolf-reichwein-schule.de/fileadmin/home/nichtImMenue/vertretungsplan/schueler/morgen/subst_001.htm" # link for tomorrow

plan = Vertretungsplan.Plan(grade="E1C", urltoday=link1, urltomorrow=link2) # creates object

data_today = plan.getToday() # gets todays data
data_tomorrow = plan.getTomorrow() # gets tomorrows data

for i in data_today: # goes through first loop
    for j in i: #goes through second loop
        print(j.ljust(21), end="") # prints data without backslash
    print("") # makes backslash

print("-"*(21*9)) #prints a line

for i in data_tomorrow: # goes through first loop
    for j in i: #goes through second loop
        print(j.ljust(21), end="") # prints data without backslash
    print("") # makes backslash
```

There are still some changes to make and features to add. Work in progress ...
