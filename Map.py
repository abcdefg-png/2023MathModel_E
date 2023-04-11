import folium

# 创建一个基本地图
world_map = folium.Map(location=[30, 0], zoom_start=2)

# 标记美国纽约
ny_coords = [40.712776, -74.005974]
folium.Marker(ny_coords, popup='New York City',
              icon=folium.Icon(color='green')).add_to(world_map)

# 标记德国Cicero市
cicero_coords = [52.498312, 13.447984]
folium.Marker(cicero_coords, popup='Cicero, Germany',
              icon=folium.Icon(color='green')).add_to(world_map)

# 标记美国华盛顿州米尔顿镇
milton_coords = [46.8409, -122.2460]
folium.Marker(milton_coords, popup='Milton, Washington',
              icon=folium.Icon(color='green')).add_to(world_map)

# 标记台湾翡翠湾国家公园
feicuiwan_coords = [22.0824, 120.7364]
folium.Marker(feicuiwan_coords, popup='Feicuiwan National Park, Taiwan',
              icon=folium.Icon(color='green')).add_to(world_map)

# 展示地图
world_map.show_in_browser()
world_map.save("map.html")
