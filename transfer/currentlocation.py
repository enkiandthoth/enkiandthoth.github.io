import pandas as pd
import csv
import glob
from tqdm import tqdm
import datetime
import subprocess
import os


logfile = pd.read_csv('raw.csv')

car1 = logfile[logfile.vehicleid == 305]
car2 = logfile[logfile.vehicleid == 269]

car1.to_csv('car1.csv')
car2.to_csv('car2.csv')

car1 = pd.read_csv('car1.csv')
car2 = pd.read_csv('car2.csv')

car1last =pd.DataFrame(columns=['lat', 'long', 'enginestate','logtime',])
car2last =pd.DataFrame(columns=['lat', 'long', 'enginestate','logtime',])

car1last = car1last.append({'lat':car1.latitude[len(car1)-1],'long':car1.longitude[len(car1)-1],'logtime':car1.logtime[len(car1)-1],'enginestate':car1.enginestate[len(car1)-1]}, ignore_index=True)
car2last = car2last.append({'lat':car2.latitude[len(car2)-1],'long':car2.longitude[len(car2)-1],'logtime':car2.logtime[len(car2)-1],'enginestate':car2.enginestate[len(car2)-1]}, ignore_index=True)

print(car1last)
print(car2last)

car1last.to_csv('car1latest.csv')
car2last.to_csv('car2latest.csv')





