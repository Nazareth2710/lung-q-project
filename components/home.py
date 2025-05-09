import streamlit as st
from utils.localization import get_localized_strings

t = get_localized_strings()
st.image("images/lung-cancer-2.png")

st.title(t["home_page"]["title"])
st.write(t["home_page"]["description"])

