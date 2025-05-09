import streamlit as st
from utils.localization import get_localized_strings

def run():
    st.image("images/lung-cancer-2.png")
    t = get_localized_strings()

    st.title(t["home_page"]["title"])
    st.write(t["home_page"]["description"])

run()

