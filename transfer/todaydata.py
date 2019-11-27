# Filter the data from today 
# Draw the data using gradient linear 
# At the end of todays data put a pulsating point
# RED ----> Car is driving
# BLUE -----> Car is parked
# [OPTIONAL] when clicking the point it gives info about the car
# [OPTIONAL] Animate an icon along the path (plane riding along the path)
# [OPTIONAL] Make a back button to see previous days data
# FILTER OUT ONLY THE ENGINESTATE = ON
# For day filtering only mongoexport data from today. write a py script to pass datatime var to os command


# filter data from today
import datetime
import pandas as pd
from tqdm import tqdm
import os

d = datetime.datetime.today()
currentDay = d.day
currentMonth = d.month

# ###############################
# # TEMP TIME ( DELETE AFTER DEPLOYING)

# d = datetime.datetime.strptime('2019-10-25T16:41:24+0200', "%Y-%m-%dT%H:%M:%S%z")
# currentDay = d.day
# currentMonth = d.month


# ##############################


car1 = pd.read_csv('car1.csv')
car1df = pd.DataFrame(columns=['lat', 'long', 'enginestate','logtime',])
car2 = pd.read_csv('car2.csv')
car2df = pd.DataFrame(columns=['lat', 'long', 'enginestate','logtime',])




for i in tqdm(range(len(car1))):
    try:
        time = datetime.datetime.strptime(car1.logtime[i], "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        time = datetime.datetime.strptime(car1.logtime[i], "%Y-%m-%dT%H:%M:%S%z")
    car1day = time.day
    car1month = time.month
    if (currentDay == car1day and currentMonth == car1month):
        car1df = car1df.append({'lat':car1.latitude[i],'long':car1.longitude[i],'logtime':car1.logtime[i],'enginestate':car1.enginestate[i]}, ignore_index=True)


car1df.to_csv('car1today.csv', header=True)

for i in tqdm(range(len(car2))):
    try:
        time = datetime.datetime.strptime(car2.logtime[i], "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        time = datetime.datetime.strptime(car2.logtime[i], "%Y-%m-%dT%H:%M:%S%z")
    car2day = time.day
    car2month = time.month
    if (currentDay == car2day and currentMonth == car2month):
        car2df = car2df.append({'lat':car2.latitude[i],'long':car2.longitude[i],'logtime':car2.logtime[i],'enginestate':car2.enginestate[i]}, ignore_index=True)


car2df.to_csv('car2today.csv', header=True)



print("DONE! Converting to GeoJSON now...")




# RUNNING BASH COMMAND TOGENERATE GEOJSON

#convert1 = 'csv2geojson --lat lat --lon long --line true /Users/enki/Desktop/Finaldemo/car1today.csv > /Users/enki/Desktop/temp/car1today.geojson'
#convert2 = 'csv2geojson --lat lat --lon long --line true /Users/enki/Desktop/Finaldemo/car2today.csv > /Users/enki/Desktop/temp/car2today.geojson'

#os.system(convert1)
#os.system(convert2)