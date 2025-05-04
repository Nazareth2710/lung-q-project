from typing import NamedTuple
import streamlit as st

class ThemeColor(NamedTuple):
    primaryColor: str
    backgroundColor: str
    secondaryBackgroundColor: str
    textColor: str

@st.cache_resource
def get_original_theme() -> ThemeColor:
    return ThemeColor(
        primaryColor=st._config.get_option("theme.primaryColor"),
        backgroundColor=st._config.get_option("theme.backgroundColor"),
        secondaryBackgroundColor=st._config.get_option("theme.secondaryBackgroundColor"),
        textColor=st._config.get_option("theme.textColor"),
    )

_DARK_THEME = ThemeColor(
    primaryColor="#e6faf9",
    backgroundColor = "#051918",
    secondaryBackgroundColor = "#3c384d",
    textColor = "#e7faed"
)

def init_theme_hack(default: str = "light"):
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = default
    if "orig_theme" not in st.session_state:
        st.session_state.orig_theme = get_original_theme()

def reconcile_theme_config():
    target: ThemeColor = _DARK_THEME if st.session_state.theme_mode == "dark" else st.session_state.orig_theme

    changed = False
    for field in ThemeColor._fields:
        opt_name = f"theme.{field}"
        curr = st._config.get_option(opt_name)
        want = getattr(target, field)
        if curr != want:
            st._config.set_option(opt_name, want)
            changed = True

    if changed:
        st.rerun()

def render_theme_toggle(key: str = "toggle_theme"):
    init_theme_hack()

    icon = (
        ":material/light_mode:"
        if st.session_state.theme_mode == "dark"
        else ":material/dark_mode:"
    )

    if st.sidebar.button("", icon=icon, key=key, use_container_width=True):
        st.session_state.theme_mode = (
            "light" if st.session_state.theme_mode == "dark" else "dark"
        )
        reconcile_theme_config()

    reconcile_theme_config()
