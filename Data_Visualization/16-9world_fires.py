import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'Data_Visualization\world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)



    lats, lons, brights = [], [], []
    for row in reader:
        #lats.append(row[1])
        #lons.append(row[2])
        #bright.append(row[3])
        lat = float(row[1])
        lon = float(row[2])
        bright = float(row[3])
        lats.append(lat)
        lons.append(lon)
        brights.append(bright) 

data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	#'bright': bright,
	#'marker': {
	#	'size': [5],
	#	'color': bright,
	#	'colorscale': 'Viridis',
	#	'reversescale': True,
	#	'colorbar': {'title': 'Brightness'},
	#},
}]

my_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='World_fires.html')