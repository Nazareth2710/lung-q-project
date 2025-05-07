import json
import streamlit as st
from pathlib import Path

LOCALES = ["uk", "en"]
DEFAULT_LOCALE = "uk"

def set_language():
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LOCALE

    if st.session_state.lang == "uk":
        if st.sidebar.button("![English](https://cdn-icons-png.flaticon.com/512/197/197374.png)", use_container_width=True):
            st.session_state.lang = "en"
            st.rerun()
    else:
        if st.sidebar.button("![Українська](https://cdn-icons-png.flaticon.com/512/197/197572.png)", use_container_width=True):
            st.session_state.lang = "uk"
            st.rerun()

def get_localized_strings():
    lang = st.session_state.get("lang", DEFAULT_LOCALE)
    path = Path("localization") / f"{lang}.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)