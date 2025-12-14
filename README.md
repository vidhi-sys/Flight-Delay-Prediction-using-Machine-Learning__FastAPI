# ✈️ Flight Delay Prediction

This project uses a machine learning model to **predict flight delays**, aiming to help airlines and passengers plan better.

Recently, as reported in [Times of India](https://timesofindia.indiatimes.com/city/patna/turmoil-at-city-airport-as-indigo-cancels-11-of-28-scheduled-flights/articleshow/125808652.cms), Indigo canceled 11 out of 28 scheduled flights at multiple airports. This highlights the real-world challenges that inspired this project.

## 📦 Dataset

The model is trained on historical flight data from the U.S. DOT dataset on Kaggle:

👉 [Flight Delays Dataset](https://www.kaggle.com/datasets/usdot/flight-delays)

## 🧠 Model Overview

We used a **Random Forest Classifier** to predict whether a flight will be delayed or on time.

The workflow includes:

* Preparing and cleaning the data
* Feature engineering
* Train–test split and evaluation
* Estimating delay probabilities
* Exporting the model for deployment

The model provides:

* **Binary prediction**: Delayed / On time
* **Probability score**: Likelihood of delay

Most flights have probabilities around **0.40–0.60**, showing moderate classifier confidence—helpful for operational decisions.

## 🚀 Deployment

The model is integrated with **FastAPI** for real-time predictions. You can try it out here:

👉 [Live App](https://flight-delay-prediction-tin5.onrender.com)

## 📁 Code

The model notebook and code are available here:

👉 [GitHub Notebook](https://github.com/vidhi-sys/Flight-Delay-Prediction-using-Machine-Learning__FastAPI/blob/main/fastapi_ml_model.ipynb)

## 🔧 Future Plans

* Enhance the FastAPI interface
* Integrate live flight and weather data
* Build a dashboard for real-time monitoring

## 🤝 Contributions

Suggestions, feedback, and collaboration are welcome!

---

Plan smarter. Fly safer.
