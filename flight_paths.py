import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import folium
from folium.features import CustomIcon
import random

PATH_TO_DATA = "./flight_paths_data.csv"


def flight_paths_mapbox():
    st.subheader("American Airlines Flight Paths")

    df = pd.read_csv(PATH_TO_DATA)
    # adding a column row_id at the beginning
    df.insert(loc=0, column="id", value=range(1, len(df) + 1))
    st.dataframe(df, hide_index=True)

    map = folium.Map(
        location=[35.0902, -105.7129], tiles="Cartodb dark_matter", zoom_start=4
    )

    # iterate over the rows of the dataframe
    for index, row in df.iterrows():
        start_coords = (row["start_lat"], row["start_lon"])
        end_coords = (row["end_lat"], row["end_lon"])

        # add a line to the map
        color = random_color()
        line = folium.PolyLine(
            locations=[start_coords, end_coords],
            color=color,
            popup=f"{row['id']}: {row['airport1']} to {row['airport2']}",
            weight=1,
            opacity=0.8,
            dash_array=5,
        )

        midpoint = [
            (start_coords[0] + end_coords[0]) / 2,
            (start_coords[1] + end_coords[1]) / 2,
        ]
        icon_url = (
            "https://cdn.iconscout.com/icon/free/png-512/free-plane-3802463-3168528.png"
        )
        icon = CustomIcon(icon_url, icon_size=(24, 24))
        folium.Marker(
            location=midpoint,
            icon=icon,
            popup=f"{row['id']}: {row['airport1']} to {row['airport2']}",
        ).add_to(map)

        map.add_child(line)

    # save map as html
    map.save("flight_paths.html")

    # read the html file
    HtmlFile = open("flight_paths.html", "r", encoding="utf-8")
    map = HtmlFile.read()

    components.html(map, height=500)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return "#{:02x}{:02x}{:02x}".format(r, g, b)
