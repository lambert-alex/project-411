import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

startDt = pd.read_csv(".\May2023.csv")
endDt = pd.read_csv(".\May2024.csv")
startDt.head(1)

# get the center of all unique munis
result = {}

def get_center_loc(group):
    # assuming the earth is perfectly round
    rads_lat = np.radians(group.latitude)
    rads_lng = np.radians(group.longitude)
    
    # Convert lat/lon (radians) to Cartesian coordinates for each location.
    X = np.cos(rads_lat) * np.cos(rads_lat)
    Y = np.cos(rads_lng) * np.sin(rads_lng)
    Z = np.sin(rads_lat)

    #find average x, y, z coords
    x = X.mean()
    y = Y.mean()
    z = Z.mean()

    # Convert average x, y, z coordinate to latitude and longitude.
    lng = math.atan2(y, x)
    hyp = math.sqrt(x*x + y*y)
    lat = math.atan2(z, hyp)
    result[group['neighbourhood_group'].unique()[0]] = (np.degrees(lat), np.degrees(lng))

startDt.groupby(['neighbourhood_group']).apply(get_center_loc)



# break up all the startDt data into single owners and multi owners
start_count = startDt.host_id.value_counts()
multi_start = startDt[startDt.host_id.isin(start_count.index[start_count.gt(1)])]
single_start = startDt[startDt.host_id.isin(start_count.index[start_count.lt(2)])]

# break up all endDt data into multi owners and single owners
end_count = endDt.host_id.value_counts()
multi_end = endDt[endDt.host_id.isin(end_count.index[end_count.gt(1)])]
single_end = endDt[endDt.host_id.isin(end_count.index[end_count.lt(2)])]

# get mean price grouped by host_id
# values tracking multi_start, multi_end, single_start, single_end, singleDt, endDt
multi_start['mean_price'] = multi_start.groupby(['host_id']).price.transform('mean')
multi_end['mean_price'] = multi_end.groupby(['host_id']).price.transform('mean')