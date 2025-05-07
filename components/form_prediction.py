import streamlit as st
import pickle
import numpy as np

st.title("Оцінка ризику раку легень")


@st.cache_resource
def load_model():
    with open("models/bnb_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

yes_no = ["Так", "Ні"]

with st.form("prediction_form"):
    gender = st.selectbox("Стать", ["Чоловічий", "Жіночий"])
    age = st.slider("Вік", 1, 120, 18)

    col1, col2 = st.columns(2)

    with col1:
        smoking = st.radio("Ви курите?", yes_no, index=None)
        anxiety = st.radio("Чи відчуваєте ви час від часу тривогу?", yes_no, index=None)
        chronic_disease = st.radio("Чи маєте ви хронічні захворювання?", yes_no, index=None)
        allergy = st.radio("Чи маєте ви алергію?", yes_no, index=None)
        alcohol_consuming = st.radio("Чи вживаєте ви алкоголь?", yes_no, index=None)
        shortness_of_breath = st.radio("Ви маєте задуху?", yes_no, index=None)
        chest_pain = st.radio("Чи відчуваєте останнім часом біль у грудях?", yes_no, index=None)

    with col2:
        yellow_fingers = st.radio("Чи є у вас жовті пальці?", yes_no, index=None)
        peer_pressure = st.radio("Чи відчуваєте ви тиск зі сторони сім'ї, робочого колективу чи інших спільнот?", yes_no, index=None)
        fatigue = st.radio("Ви відчуваєте сильну втому останнім часом?", yes_no, index=None)
        wheezing = st.radio("Чи є під час глибокого дихання свистіння?", yes_no, index=None)
        coughing = st.radio("Ви маєте кашель?", yes_no, index=None)
        swallowing_difficulty = st.radio("Чи є у вас утруднене ковтання?", yes_no, index=None)

    submit = st.form_submit_button("Оцінити ризик")


if submit:
    radio_answers = [
        smoking,
        yellow_fingers,
        anxiety,
        peer_pressure,
        chronic_disease,
        fatigue,
        allergy,
        wheezing,
        alcohol_consuming,
        coughing,
        shortness_of_breath,
        swallowing_difficulty,
        chest_pain
    ]

    if any(ans is None for ans in radio_answers):
        st.warning("Будь ласка, дайте відповідь на всі запитання, перш ніж продовжити.", icon=":material/warning:")
    else:
        def to_binary(val): return 1 if val == "Так" else 0

        gender_val = 1 if gender == "Чоловічий" else 0
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

        st.subheader("Результат:")
        if risk_percent >= 65:
            st.error(f"Високий ризик: {risk_percent}% ймовірності захворювання на рак легень.", icon=":material/priority_high:")
        elif risk_percent >= 30:
            st.warning(f"Середній ризик: {risk_percent}% ймовірності захворювання на рак легень.", icon=":material/warning:")
        else:
            st.success(f"Низький ризик: {risk_percent}% ймовірності захворювання на рак легень.", icon=":material/thumb_up:")
