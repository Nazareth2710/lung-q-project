import streamlit as st
import pickle
import numpy as np

st.title("Оцінка рзику рака легень")

# Загрузка модели
@st.cache_resource
def load_model():
    with open("models/xgb_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Форма ввода данных
with st.form("prediction_form"):
    gender = st.selectbox("Стать", ["Чоловічий", "Жіночий"])
    age = st.slider("Вік", 1, 120, 18)
    smoking = st.radio("Ви курете?", [0, 1])
    yellow_fingers = st.radio("Чи є у вас жовті пальці?", [0, 1])
    anxiety = st.radio("Чи відчуваєте ви час від часу тривогу?", [0, 1])
    peer_pressure = st.radio("Чи відчуваєте ви тиск зі сторони сім'ї, робочого колективу чи інших спільнот?", [0, 1])
    chronic_disease = st.radio("Чи маєте ви хронічні захворювання?", [0, 1])
    fatigue = st.radio("Ви відчуваєте сильну втому останнім часом?", [0, 1])
    allergy = st.radio("Чи маєте ви алергію?", [0, 1])
    wheezing = st.radio("Чи є під час глибокого дихання свистіння?", [0, 1])
    alcohol_consuming = st.radio("Чи вживаєте ви алкоголь?", [0, 1])
    coughing = st.radio("Ви маєте кашель?", [0, 1])
    shortness_of_breath = st.radio("Ви маєте задух?", [0, 1])
    swallowing_difficulty = st.radio("Чи є у вас утруднене ковтання?", [0, 1])
    chest_pain = st.radio("Чи відчуваєте останнім часом біль у грудях?", [0, 1])

    submit = st.form_submit_button("Оцінити ризик")

if submit:
    gender_val = 1 if gender == "Чоловічий" else 0
    input_data = np.array([[
        gender_val, age, smoking, yellow_fingers, anxiety, peer_pressure,
        chronic_disease, fatigue, allergy, wheezing, alcohol_consuming,
        coughing, shortness_of_breath, swallowing_difficulty, chest_pain
    ]])

    probabilities = model.predict_proba(input_data)[0]
    risk_percent = round(probabilities[1] * 100, 2)
    risk_percent = round(risk_percent, 2)

    st.subheader("Результат:")
    if risk_percent >= 65:
        st.error(f"Високий ризик: {risk_percent}% ймовірності захворювання на рак легень.")
    elif risk_percent >= 30:
        st.warning(f"Середній ризик: {risk_percent}% ймовірності захворювання на рак легень.")
    else:
        st.success(f"Низький ризик: {risk_percent}% ймовірності захворювання на рак легень.")