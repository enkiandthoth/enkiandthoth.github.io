#!/bin/bash 

echo Converting Car1

csv2geojson --lat lat --lon long /Users/enki/Desktop/shahud1.github.io/car1latest.csv > /Users/enki/Desktop/shahud1.github.io/car1latest.geojson


echo Converting Car2

csv2geojson --lat lat --lon long /Users/enki/Desktop/shahud1.github.io/car2latest.csv > /Users/enki/Desktop/shahud1.github.io/car2latest.geojson


echo GeoJson files created for Car1 and Car2 FINIISHED