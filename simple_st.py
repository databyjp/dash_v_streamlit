# ========== (c) JP Hwang 27/7/20  ==========
from shared_funcs import load_fig
fig = load_fig()

import streamlit as st

st.header("Houston Rockets Shot Chart - 2020 Season")
st.write("This chart shows the shot distribution of the NBA team Houston Rockets, based on particular areas of the court, and their expected points per shot (i.e. efficiency) from each area.")
st.write("Use the dropdown menu to change the color scale for the shot chart.")
choice = st.selectbox(
    "Choose a color scale",
    ("Blue-Yellow-Red", "Rose-Teal", "Orange-Purple")
)
lookup_dict = {"Blue-Yellow-Red":"RdYlBu_r", "Rose-Teal":"Tealrose_r", "Orange-Purple":"PuOr_r"}
fig = fig.update_traces(marker={"colorscale":lookup_dict[choice]})
st.write(fig)
