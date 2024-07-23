import subprocess

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
