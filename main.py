import streamlit as st
from utils.theming import init_theme, render_theme_toggle


init_theme(default="light")
st.logo("images/lung_cancer_logo_full.png", icon_image='images/lung_cancer_logo_icon.png', size='large')

pages = {
    "": [
        st.Page("components/home.py", title="Home", icon=":material/home:"),
        st.Page("components/info_page.py", title="Info about Lung Cancer", icon=":material/pulmonology:"),
        st.Page("components/form_prediction.py", title="Predict your Lung risk!", icon=":material/respiratory_rate:"),
        st.Page("components/about_us.py", title="About us", icon=":material/info:")
    ]
}
render_theme_toggle()
st.sidebar.text("Made by Umantsiv N., 2025")


pg = st.navigation(pages)
pg.run()
