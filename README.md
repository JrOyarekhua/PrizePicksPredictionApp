# 🏀 PrizePicks Prediction App

**Predict NBA player performance to make smarter PrizePicks selections.**  
Combines data science, basketball analytics, and machine learning in a full-stack web app.

---

## 📌 Project Goal

The goal of this project is to build a machine learning-powered web application that helps users make more informed over/under picks on **PrizePicks**. The app predicts player performance based on opponent context and historical statistics, starting with points and expanding to other categories.

---

## 🚀 MVP Goals

The Minimum Viable Product (MVP) will include:

### ✅ Data & EDA
- Pull NBA data using `nba_api`
- Clean and structure player/team game data
- Perform EDA to validate basketball domain knowledge
- Identify key features influencing player performance

### ✅ Machine Learning
- Select 10–16 relevant features based on research + EDA
- Train baseline regression or classification model
- Evaluate prediction accuracy (e.g., RMSE, accuracy)
- Save and version models

### ✅ Backend
- Build a **FastAPI** or **Flask** backend with:
  - `/predict` endpoint to return predictions
  - Support for player + opponent inputs

### ✅ Frontend
- Build a **React/Next.js** interface:
  - Input: Choose a player and stat line
  - Output: Probability of hitting over/under
  - Optional: Show supporting stats and trends

---

## 🛠️ Tech Stack

| Layer     | Tool/Libs                      |
|-----------|-------------------------------|
| Data      | `nba_api`, `pandas`, `numpy`  |
| ML        | `scikit-learn`, `xgboost`     |
| Backend   | `FastAPI` / `Flask`           |
| Frontend  | `React.js` / `Next.js`        |
| DB (optional) | `SQLite` / `PostgreSQL`   |

---

## 📈 Progress Roadmap

- [x] Set up project and GitHub
- [ ] Complete EDA & feature selection
- [ ] Train and evaluate first ML model
- [ ] Build backend API
- [ ] Build frontend interface
- [ ] Deploy MVP

---

## 📚 References

- NBA analytics research papers
- PrizePicks user trends
- Sports data modeling studies

---

## 🤝


