import time
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from geopy.geocoders import Nominatim, Photon
import folium
from folium.plugins import MarkerCluster

PATH_TO_DATA = "./global_companies_data.csv"

def global_companies_mapbox():
    st.subheader("Global Companies")

    df = pd.read_csv(PATH_TO_DATA, index_col="Ranking")
    
    # slice dataframe for easier testing
    df = df[100:150]

    # geolocator to get location from country name
    geolocator = Nominatim(user_agent="my_user_kanak")

    # folium map
    map = folium.Map(location=[0, 0], zoom_start=2, tiles="Stadia.AlidadeSmoothDark")

    # adding marker cluster to handle multiple markers
    marker_cluster = MarkerCluster().add_to(map)

    for index, row in df.iterrows():
        country = row["Country"]

        try:
            # st.write(f"COUNTRY: {country}")
            location = geolocator.geocode(country, language='en', timeout=10)
            # st.write(f"COUNTRY: {country} {{LATITUDE: {location.latitude}, LONGITUDE: {location.longitude}}}")
            if location:
                msg = st.empty()
                msg.text(f"Geoencoding {row['Company']} in {country}")
                time.sleep(0.3)
                msg.empty()

                popup_message = f"{index}: {row["Company"]}, {row["Country"]}"
                folium.Marker(location=[location.latitude, location.longitude], popup=popup_message).add_to(marker_cluster)
            else:
                st.error(f"Geocity not found for {row["Company"]}")
            
        except Exception as e:
            st.error(f"Error: {e}")
   
    map.save("global_companies.html")
    HtmlFile = open("global_companies.html", "r", encoding="utf-8")
    map = HtmlFile.read()

    components.html(map, height=700, width=1000)
