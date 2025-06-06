import streamlit as st
from utils.theming import render_theme_toggle
from utils.localization import set_language, get_localized_strings

st.logo("images/lung_cancer_logo_full.png", icon_image='images/lung_cancer_logo_icon.png', size='large')
t = get_localized_strings()

pages = {
    "": [
        st.Page("components/home.py", title=t["pages"]["home"], icon=":material/home:"),
        st.Page("components/info_page.py", title=t["pages"]["info"], icon=":material/pulmonology:"),
        st.Page("components/form_prediction.py", title=t["pages"]["prediction"], icon=":material/respiratory_rate:"),
        st.Page("components/about_us.py", title=t["pages"]["about"], icon=":material/info:")
    ]
}
render_theme_toggle()
set_language()
st.sidebar.caption("Made by Umantsiv N., 2025")

pg = st.navigation(pages)
pg.run()
