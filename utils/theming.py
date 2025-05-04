import streamlit as st
import toml

def init_theme(default: str = "light"):
    if "theme" not in st.session_state:
        st.session_state.theme = default

def render_theme_toggle(key: str = "toggle_theme"):
    light_icon = ":material/light_mode:"
    dark_icon  = ":material/dark_mode:"
    icon = light_icon if st.session_state.theme == "light" else dark_icon

    if st.sidebar.button("", icon=icon, key=key, use_container_width=True):
        st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
        st.rerun()

