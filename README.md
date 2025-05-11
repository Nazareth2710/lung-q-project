[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)](https://keras.io/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

# Lung Q — Оцінка ризику раку легень

**Lung Q** — це веб-додаток на базі Streamlit, який дозволяє користувачам пройти коротке опитування та отримати попередню оцінку ризику розвитку раку легень. Проєкт розроблено у рамках практики для служби екстреної медичної допомоги Закарпатської області.

---

## 🔍 Основні можливості

- 🧠 Прогнозування з використанням кількох моделей (KNN, Naive Bayes, XGBoost, нейронна мережа).
- 🌐 Підтримка української та англійської мов.
- 🌓 Автоматична або ручна зміна теми (світла/темна).
- 🩺 Інформаційна сторінка про рак легень.
- 📱 Інтерфейс, адаптований для мобільних пристроїв.

---
## 🔧 Як запустити на локальному комп'ютері

> Потрібно мати встановлений **Python 3.12+** та **pip**

1. Клонуйте репозиторій:
```bash
git clone https://github.com/your-username/lung-q.git
cd lung-q
```

2. Встановіть залежності:
```bash
pip install -r requirements.txt
```

3. Запустіть додаток:
```bash
streamlit run main.py
```

4. Відкрийте у браузері:
```bash
http://localhost:8501
```

## 📦 Як запустити на сервері з Docker

1. Побудуйте Docker-образ:
```bash
docker build -t lung-q-app .
```

2. Запустіть контейнер:
```bash
docker run -p 8501:8501 lung-q-app
```

