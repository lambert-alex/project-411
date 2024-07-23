import subprocess
import osmium
import json

# Define the GeoJSON polygon for the area you want to extract
area_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-124.51320920228699, 48.48909340749657],
                        [-123.5666842133617, 48.26353181707546],
                        [-123.20387628408636, 48.41640427236018],
                        [-123.26834833718829, 48.69359374300129],
                        [-123.02578032671818, 48.76672982951058],
                        [-123.01836032831007, 48.831523305707975],
                        [-123.46449967442786, 49.0510597584493],
                        [-123.74522657408818, 48.88959966491461],
                        [-123.63533394961024, 48.57805485830272],
                        [-124.43411220955018, 48.627888848497264],
                        [-124.51272615235646, 48.487841855612885],
                        [-124.51320920228699, 48.48909340749657]  # Closing the polygon
                    ]
                ]
            }
        }
    ]
}

# Save the GeoJSON polygon to a file
with open('area.geojson', 'w') as f:
    json.dump(area_geojson, f)

# Define input and output file paths
input_pbf = 'british-columbia-latest.osm.pbf'
extracted_pbf = 'extracted.osm.pbf'
output_geojson = 'extracted.geojson'

print("Run osmium extract to get the desired area")
# Run osmium extract to get the desired area
subprocess.run(['osmium', 'extract', '--polygon', 'area.geojson', '-o', extracted_pbf, input_pbf], check=True)

print("Run ogr2ogr to convert the extracted data to GeoJSON")
# Run ogr2ogr to convert the extracted data to GeoJSON
subprocess.run(['ogr2ogr', '-f', 'GeoJSON', output_geojson, extracted_pbf], check=True)

print(f'Extracted data saved to {output_geojson}')
