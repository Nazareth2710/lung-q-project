import streamlit as st
from utils.localization import get_localized_strings

t = get_localized_strings()
st.image("images/lung-cancer-4.png")

st.title(t["about_page"]["title"])
st.write(t["about_page"]["description"])