🏀 PrizePicks NBA Player Stat Prediction App
📌 Project Overview
The goal of this project is to build a machine learning-powered web application that predicts how many points an NBA player will score in a given matchup. The app combines basketball domain knowledge, exploratory data analysis (EDA), and machine learning to create a predictive tool for use cases like PrizePicks.

This project showcases:

End-to-end machine learning deployment

Real-time data ingestion and updates from the nba_api

Informed feature selection using research and statistical analysis

Backend API for ML inference

Frontend interface for user interaction

🎯 Minimum Viable Product (MVP) Goals
Data Pipeline

Ingest player and team stats from the nba_api

Clean, organize, and store data in a database (or cache locally for testing)

Include scripts to initialize and update the dataset

Exploratory Data Analysis (EDA)

Perform visual and statistical analysis to identify key features

Cross-reference insights with basketball domain knowledge and 2–3 research papers

Use techniques like χ² tests, correlation heatmaps, and seasonal trends

Feature Selection

Determine a minimal, high-impact set of features that affect scoring

Justify feature choices using both data and research

Machine Learning Model

Build a simple baseline model (e.g., Linear Regression or Tree-based)

Evaluate and document performance (RMSE, MAE, etc.)

Save model for deployment

Backend API

Build a Python/Flask or FastAPI backend

Expose ML model via an API endpoint (/predict) that accepts player/matchup data

Handle input validation and serve predictions in JSON format

Frontend Interface

Create a lightweight React or Next.js frontend

Allow users to select a player and see predicted points for upcoming games

Display basic stats and charts to explain the prediction