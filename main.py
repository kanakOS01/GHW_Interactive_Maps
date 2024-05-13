import streamlit as st

from state_city_map import state_city_scatter_mapbox, state_city_choropleth_mapbox
from flight_paths import flight_paths_mapbox
from global_companies import global_companies_mapbox

PATH_TO_DATA = "./state_city_data.json"

st.set_page_config(layout="wide")
st.title("Interactive Maps")

SIDEBAR_DICT = {
    "STATE-CITY SCATTER MAP": state_city_scatter_mapbox,
    "STATE-CITY CHOROPLETH MAP": state_city_choropleth_mapbox,
    "FLIGHT PATHS": flight_paths_mapbox,
    "GLOBAL COMPANIES MAP": global_companies_mapbox,
}

def main():
    chart_type = st.sidebar.radio("Select Chart Type: ", SIDEBAR_DICT.keys())
    SIDEBAR_DICT[chart_type]()      # SIDEBAR_DICT[chart_type] gives the function name and () calls the function

if __name__ == "__main__":
    main()