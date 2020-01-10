import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_alt(elevation):
    if elevation < 1500:
        return "darkpurple"
    elif 1501 <= elevation < 2500:
        return "darkred"
    else:
        return "blue"


html = """Volcano name:<br><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>Height: %s m"""

map = folium.Map(location=[45.33, -90.09], zoom_start=4, tiles="Stamen Toner")

fg = folium.FeatureGroup("My Map")

for lt,ln,el,name in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    map.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=folium.Popup(iframe),fill_color =color_alt(el),color="grey",fill_opacity =0.8))

map.add_child(fg)
map.save("Map_main.html")
