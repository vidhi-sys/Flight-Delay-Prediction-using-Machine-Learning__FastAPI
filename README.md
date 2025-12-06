
# ✈️ Flight Delay Prediction using Machine Learning


This project implements a machine learning model to **predict flight delays**, inspired by recent disruptions in domestic aviation and the growing need for operational decision support.  

For example, as reported in [Times of India](https://timesofindia.indiatimes.com/city/patna/turmoil-at-city-airport-as-indigo-cancels-11-of-28-scheduled-flights/articleshow/125808652.cms)
Indigo canceled 11 of 28 scheduled flights at multiple airport, highlighting the operational challenges that this project aims to address.

## 📦 Dataset

The model is trained on historical flight data from the U.S. DOT dataset on Kaggle:

👉 [https://www.kaggle.com/datasets/usdot/flight-delays](https://www.kaggle.com/datasets/usdot/flight-delays)

## 🧠 Model Overview

A **Random Forest Classifier** was used to classify delayed vs non-delayed flights.

The workflow includes:

* Feature engineering and preprocessing
* Train–test split and evaluation
* Delay probability estimation
* Model export for deployment

The model outputs:

* **Binary prediction**: Delayed / Not delayed
* **Probability score**: Likelihood of delay

Most flights fall in the **0.40–0.60 probability range**, indicating moderate classifier confidence and a well-spread distribution — useful for operational insights.

## 🚀 Deployment

The trained model has been serialized and the next step is **FastAPI integration** for real-time inference.
A lightweight web interface will be added for user interaction.

## 📁 Code

Model notebook and export:

👉 [https://github.com/vidhi-sys/Flight-Delay-Prediction-using-Machine-Learning__FastAPI/blob/main/fastapi_ml_model.ipynb](https://github.com/vidhi-sys/Flight-Delay-Prediction-using-Machine-Learning__FastAPI/blob/main/fastapi_ml_model.ipynb)

## 🔧 Future Enhancements

* FastAPI REST API interface
* Live flight and weather data integration
* Dashboard for real-time monitoring

## 🤝 Contributions

Feedback, suggestions, and collaboration are welcome!

---

✈️🛫 ➜ ➜ ➜ 🛬

Fly safe. Predict smarter.

