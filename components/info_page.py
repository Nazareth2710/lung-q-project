import streamlit as st
from utils.localization import get_localized_strings

t = get_localized_strings()

st.image("images/lung-cancer.png")

st.title(t["info_page"]["title"])


st.markdown(t["info_page"]["intro"])

st.header(t["info_page"]["what_is_lung_cancer"]["header"])
st.markdown(t["info_page"]["what_is_lung_cancer"]["content"])

st.header(t["info_page"]["statistics"]["header"])
st.markdown(t["info_page"]["statistics"]["content"])

st.header(t["info_page"]["symptoms"]["header"])
st.markdown(t["info_page"]["symptoms"]["content"])

st.header(t["info_page"]["causes_risk_factors"]["header"])
st.markdown(t["info_page"]["causes_risk_factors"]["content"])

st.header(t["info_page"]["diagnosis"]["header"])
st.markdown(t["info_page"]["diagnosis"]["content"])

st.header(t["info_page"]["treatment"]["header"])
st.markdown(t["info_page"]["treatment"]["content"])

st.header(t["info_page"]["prevention"]["header"])
st.markdown(t["info_page"]["prevention"]["content"])

st.markdown(t["info_page"]["conclusion"])

st.markdown(f"### {t['info_page']['source_title']}")
for source in t["info_page"]["sources"]:
    st.markdown(f"- [{source['title']}]({source['url']})")
