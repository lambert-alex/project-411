#!/bin/bash

# Input OSM file
INPUT_FILE="extracted.osm.pbf"

# Holding files
TEMP_FILE_1="temp_1.osm"
TEMP_FILE_2="temp_2.osm"

OUTPUT_FILE="final.geojson"

# cut to user defined boundaries
python3 process_map.py

#convert
osmosis --read-pbf $INPUT_FILE --write-xml $TEMP_FILE_1

# Remove all buildings, highways, ameinties, shops, historic, and tourism markers
osmium tags-filter $TEMP_FILE_1 "nwr/emergency!=* nwr/public_transport!=* nwr/shop!=* and nwr/historic!=* and nwr/amenity!=* and nwr/tourism!=* and nwr/building!=* and nwr/highway!=*" -o $TEMP_FILE_2

osmium export $TEMP_FILE_2 -o $OUTPUT_FILE

rm $TEMP_FILE_1 $TEMP_FILE_2

echo "done"
