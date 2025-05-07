import json
import streamlit as st
from pathlib import Path

LOCALES = ["uk", "en"]
DEFAULT_LOCALE = "uk"

def set_language():
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LOCALE

    label = "English 🇬🇧" if st.session_state.lang == "uk" else "Українська 🇺🇦"
    if st.sidebar.button(label, use_container_width=True):
        st.session_state.lang = "en" if st.session_state.lang == "uk" else "uk"
        st.rerun()

def get_localized_strings():
    lang = st.session_state.get("lang", DEFAULT_LOCALE)
    path = Path("localization") / f"{lang}.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)
