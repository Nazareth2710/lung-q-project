import pickle
import streamlit as st

@st.cache_resource
def load_model(model_path="models/bnb_model.pkl"):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model
