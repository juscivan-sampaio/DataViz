import pandas as pd
import folium

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv'
dados_terremotos = pd.read_csv(url)

terremotos_significativos = dados_terremotos[dados_terremotos['mag'] >= 6.0]

mapa_terremotos = folium.Map(location=[0,0], zoom_start=2)

for index, terremoto in terremotos_significativos.iterrows():
    folium.Marker(
        location=[terremoto['latitude'], terremoto['longitude']],
        popup=f'Magnitude:{terremoto['mag']}, Profundidade: {terremoto['depth']}',
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(mapa_terremotos)

mapa_terremotos.save('data/mapa_terremotos.html')