import plotly.express as px
import streamlit as st
import pandas as pd
import json

PATH_TO_DATA = "./state_city_data.json"
PATH_TO_GEOJSON = "./indian_map_coordinates.geojson"

def state_city_scatter_mapbox():
    st.subheader("States and capitals of India - Scatter Map")

    # Loading the data from JSON file
    state_city_date = pd.read_json(PATH_TO_DATA)
    # st.dataframe(state_city_date, hide_index=True)

    fig = px.scatter_mapbox(
        state_city_date,
        lat="lat",
        lon="long",
        hover_name="state",
        hover_data="capital",
        color="capital",
        # color_discrete_sequence=px.colors.qualitative.Plotly,
        # color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=3,
        height=600,
        center={"lat": 20.5937, "lon": 78.9629},
    )

    # to make the map visible
    # fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(mapbox_style="open-street-map")
    # fig.update_layout(margin={'r':100, 't':100, 'l':100, 'b':100})
    return st.plotly_chart(fig)

def state_city_choropleth_mapbox():
    st.subheader("States and capitals of India - Choropleth Map")

    # Loading the data from JSON file
    state_city_data = pd.read_json(PATH_TO_DATA)
    # st.dataframe(state_city_data, hide_index=True)

    fig = px.choropleth_mapbox(
        data_frame=state_city_data,
        geojson=json.load(open(PATH_TO_GEOJSON, "r")),
        featureidkey="properties.ST_NM",
        locations="state",
        hover_name="state",
        hover_data="capital",
        color="capital",
        zoom=3,
        height=600,
        center={"lat": 20.5937, "lon": 78.9629}
    )

    fig.update_layout(mapbox_style="carto-darkmatter")
    return st.plotly_chart(fig)