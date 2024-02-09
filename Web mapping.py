import folium

map1 = folium.Map(location=[13.02, 80.22], zoom_start=15, tiles="CartoDB Positron",
                  attr='Map tiles by Carto, under CC BY 3.0. Data by OpenStreetMap, under ODbL.')
map1.save('Map.html')
