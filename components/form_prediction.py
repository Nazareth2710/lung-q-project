import streamlit as st
import pickle
import numpy as np
from utils.localization import get_localized_strings

t = get_localized_strings()["form_prediction"]

@st.cache_resource
def load_model():
    with open("models/bnb_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

st.image("images/lung-cancer-3.png")
st.title(t["title"])

yes_no = [t["yes"], t["no"]]

with st.form("prediction_form"):
    gender = st.selectbox(t["gender"], [t["male"], t["female"]])
    age = st.slider(t["age"], 1, 120, 18)

    col1, col2 = st.columns(2)

    with col1:
        smoking = st.radio(t["questions"]["smoking"], yes_no, index=None)
        anxiety = st.radio(t["questions"]["anxiety"], yes_no, index=None)
        chronic_disease = st.radio(t["questions"]["chronic_disease"], yes_no, index=None)
        allergy = st.radio(t["questions"]["allergy"], yes_no, index=None)
        alcohol_consuming = st.radio(t["questions"]["alcohol_consuming"], yes_no, index=None)
        shortness_of_breath = st.radio(t["questions"]["shortness_of_breath"], yes_no, index=None)
        chest_pain = st.radio(t["questions"]["chest_pain"], yes_no, index=None)

    with col2:
        yellow_fingers = st.radio(t["questions"]["yellow_fingers"], yes_no, index=None)
        peer_pressure = st.radio(t["questions"]["peer_pressure"], yes_no, index=None)
        fatigue = st.radio(t["questions"]["fatigue"], yes_no, index=None)
        wheezing = st.radio(t["questions"]["wheezing"], yes_no, index=None)
        coughing = st.radio(t["questions"]["coughing"], yes_no, index=None)
        swallowing_difficulty = st.radio(t["questions"]["swallowing_difficulty"], yes_no, index=None)

    submit = st.form_submit_button(t["submit"])

if submit:
    radio_answers = [
        smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease,
        fatigue, allergy, wheezing, alcohol_consuming, coughing,
        shortness_of_breath, swallowing_difficulty, chest_pain
    ]

    if any(ans is None for ans in radio_answers):
        st.warning(t["warning_unanswered"], icon=":material/warning:")
    else:
        def to_binary(val): return 1 if val == t["yes"] else 0

        gender_val = 1 if gender == t["male"] else 0

        input_data = np.array([[
            gender_val,
            age,
            to_binary(smoking),
            to_binary(yellow_fingers),
            to_binary(anxiety),
            to_binary(peer_pressure),
            to_binary(chronic_disease),
            to_binary(fatigue),
            to_binary(allergy),
            to_binary(wheezing),
            to_binary(alcohol_consuming),
            to_binary(coughing),
            to_binary(shortness_of_breath),
            to_binary(swallowing_difficulty),
            to_binary(chest_pain)
        ]])

        probabilities = model.predict_proba(input_data)[0]
        risk_percent = round(probabilities[1] * 100, 2)

        st.subheader(t["results"]["title"])
        if risk_percent >= 65:
            st.error(t["results"]["high"].format(risk=risk_percent), icon=":material/priority_high:")
        elif risk_percent >= 30:
            st.warning(t["results"]["medium"].format(risk=risk_percent), icon=":material/warning:")
        else:
            st.success(t["results"]["low"].format(risk=risk_percent), icon=":material/thumb_up:")
