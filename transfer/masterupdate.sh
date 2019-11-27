#!/bin/bash 

echo Updating right now...

cd /var/www/html/evcarscripts


mongoexport --uri="mongodb://tusmartcity:tu2018@log.haupcar.com/tusmartcity" --collection=interval --query '{"logtime":{"$gte": "2019-11-08T00:00:00+07:00"}}' --type=csv --out=/var/www/html/evcarscripts/raw.csv --fields _id,vehicleid,reservationno,logtime,latitude,longitude,speed,heading,hdop,fuel,charge,km,doorlockstate,enginestate


python3 /var/www/html/evcarscripts/currentlocation.py

echo Converting Car1

csv2geojson --lat lat --lon long /var/www/html/evcarscripts/car1latest.csv > /var/www/html/evcarscripts/car1latest.geojson

echo Converting Car2

csv2geojson --lat lat --lon long /var/www/html/evcarscripts/car2latest.csv > /var/www/html/evcarscripts/car2latest.geojson

python3 /var/www/html/evcarscripts/todaydata.py

csv2geojson --lat lat --lon long --line true /var/www/html/evcarscripts/car1today.csv > /var/www/html/evcarscripts/car1today.geojson

csv2geojson --lat lat --lon long --line true /var/www/html/evcarscripts/car2today.csv > /var/www/html/evcarscripts/car2today.geojson


echo Finished update

read -p "Press enter to continue"


