# project-411

Grading guidelines

3 minute video hard max.

Suggested times:

    [~10s] Project Name, student names and the main idea for your project in one sentence (a tag line) [do not spend too much time here because this was already in your interim presentation].

    [~15s] Describe what the project is about, the motivation(s) for the project.

    [~20s] Describe the data you used and your most important data questions (1 to 3 data questions).

    [~20s] Describe very briefly what is known already about this topic (e.g., related visualization projects, websites, articles).

    [~30s] Briefly introduce your visualization and how to read it, i.e. which visual marks and visual variables you are using to encode which dimensions of the data.

    [~90s] Data insights: focusing on your 1 to 3 most important data questions, show us how your visualization helps answer these questions. Talk us through a narrative an your process for figuring out answers (even partial) to these questions, demonstrating that these answers rely on the human being in the loop. This part is the core part of the presentation and you should maximize the use of images and videos (video-captures of your system is a great way of showing animations and interactions for example).


# to run 

requirments for this project

python 3.7
panadas
geopandas
numpy
matplotlib
osmium
json

Run in linux it is so much easier than screwing around with windows and osm files

First download the airbnb data you want from https://insideairbnb.com/get-the-data/ and place it in the same directory as process_data.py

Use https://geojson.io/ to create your geojson data for the area you downloaded from insideairbnb.com or format it yourself make sure the perimeter is closed! use the box tool if you are unsure.

use https://www.geofabrik.de/ to get the closest osm.pbf file you can to your geographic area this will save time


This has only been tested with linux...
Ensure you have osmium installed
sudo apt-get install osmctools

Ensure you have ogr2ogr installed
sudo apt-get update
sudo apt-get install gdal-bin


Place file in in the same location as process_map.py and add the geoJSON data to the area_geojson var on line 6 of process_map.py

Run process_map.py

Run to convert to osm file
osmosis --read-pbf extracted.osm.pbf --write-xml extracted.osm

Finally convert the data on https://mygeodata.cloud/converter/osm-to-geojson

todo nima automate this into a single executeable tool.


Run the process_data.py

See the glory!!




