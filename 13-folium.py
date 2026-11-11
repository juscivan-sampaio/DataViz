import folium

mapa = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)

cafeteiras = [
    {'localizacao': [-23.5705, -46.6433], 'nome': 'Cafeterias A'},
    {'localizacao': [-23.5405, -46.6533], 'nome': 'Cafeterias B'},
    {'localizacao': [-23.5005, -46.6833], 'nome': 'Cafeterias C'},
    {'localizacao': [-23.5555, -46.6733], 'nome': 'Cafeterias D'}
]

for cafe in cafeteiras:
    folium.Marker(
        location=cafe['localizacao'],
        popup=cafe['nome'],
        icon=folium.Icon(color='blue', icon='coffee')
    ).add_to(mapa)

mapa.save('data/mapa.html')