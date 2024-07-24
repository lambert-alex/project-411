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
jupyter notebooks lts
panadas lts
geopandas lts
numpy lts
matplotlib lts
osmium lts
folium lts

Run in linux it is so much easier than screwing around with windows and osm files

First download the airbnb data you want from https://insideairbnb.com/get-the-data/ and place it in the same directory as process_data.py

Use https://geojson.io/ to create your geojson data for the area you downloaded from insideairbnb.com or format it yourself make sure the perimeter is closed! use the box tool if you are unsure on how to do this.

use https://www.geofabrik.de/ to get the closest osm.pbf file you can to your geographic area this will save time save this file as extracted.osm.pbf in the base project folder


This has only been tested with linux there are issues in windows
Ensure you have osmium installed
sudo apt-get install osmctools

Ensure you have ogr2ogr installed
sudo apt-get update
sudo apt-get install gdal-bin


add your geojson data as a file named area.geojson in the project folder
this will cut your map to your desired size if you are struggling with processing times
run python3 process_map.py


run extract_nodes_ways.sh it removes a bunch of stuff so its quicker
you can edit this file on line 19 if you want to compare against different features for example removing nwr/emergency!=* from line 19 will leave emergency
titled map plots your output
./extract_nodes_ways.sh

Download the boundaries of the area you would like to use
https://osm-boundaries.com/map

put them into a file called boundaries.geojson in the project file.

You will have to correct the names of boundaries against muni_df manually in cell 8 I recomend taking set(muni_df.names) ^ set(boundaries) to find the difference between the names I could automate corerection but I have no idea of the scope of open osm data naming conventions

You can now use FinalData.ipynb to create the map

The map data will be output to map.html for some reason when I try and write it in the map to a notebook the title and the barchart interfere with each other





