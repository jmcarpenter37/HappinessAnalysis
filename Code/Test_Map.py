import folium
import pandas as pd
import numpy as np
import altair.vega.v2 as alt
import json
import requests
# open json
#with open(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\Code\data.json") as f:
#    df = json.load(f)
data = pd.DataFrame({'a': list('CCCDDDEEE'),
                     'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})
chart = alt.Chart(data).mark_bar().encode(
    x='a',
    y='average(b)',
)
print(chart.to_json())
df = chart.to_json()

# get a map
my_map = folium.Map(location=[46.3014, -123.7390], zoom_start=7, tiles='Stamen Terrain' )
# add data to the map
folium.Marker(location=[47.3489, -124.708], popup=folium.Popup(max_width=450).add_child(folium.Vega(df, width=450, height=250)) ).add_to(my_map)

#
my_map.save("map_test.html")

