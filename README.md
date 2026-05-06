# Statcast Home Run Prediction Pipeline

## Overview
This project explores predicting whether a Major League Baseball player will hit a home run in a given game using Statcast data from Baseball Savant. The goal is to transform raw event-level baseball data into structured datasets and build a predictive model to estimate home run probability.

The project focuses on the full data workflow: ingestion, cleaning, feature engineering, and modeling.

---

## Problem Statement
Home runs are rare but high-impact events influenced by multiple factors such as hitter performance, pitcher tendencies, and ballpark conditions. The challenge is to integrate these diverse data sources and extract meaningful signals to predict home run likelihood at the player-game level.

---

## Data
The dataset is built from MLB Statcast data and includes:

- **Hitter features:** exit velocity, launch angle, rolling performance trends, home run rates  
- **Pitcher features:** pitch velocity, pitch mix, home run rates allowed, splits vs hitters  
- **Contextual features:** ballpark dimensions, environmental factors (when available)

Data source: Baseball Savant Statcast Search

---

## Pipeline

### 1. Data Ingestion
- Extracted raw Statcast data from Baseball Savant
- Combined multiple datasets across hitters, pitchers, and games

### 2. Data Cleaning & Processing
- Standardized inconsistent formats and missing values
- Filtered and aligned event-level data into structured tables

### 3. Feature Engineering
- Built rolling averages for hitter performance trends
- Engineered pitcher performance metrics (e.g., HR rates allowed)
- Incorporated contextual variables such as ballpark effects

### 4. Dataset Construction
- Aggregated event-level data into player-game level records
- Created a unified dataset for modeling

---

## Modeling
- Trained a classification model to predict home run probability
- Evaluated model performance using standard classification metrics
- Analyzed feature importance to understand key drivers of home runs

---

## Results
- Built a model capable of estimating home run likelihood for player-game matchups
- Identified key predictive features such as exit velocity trends and pitcher home run rates
- Demonstrated the importance of combining multiple data sources for predictive accuracy

---

## Key Takeaways
- Raw sports event data requires significant transformation before modeling
- Feature engineering has a greater impact on performance than model complexity
- Integrating multiple data sources is critical for capturing real-world behavior

---

## Tech Stack
- Python (Pandas, NumPy, Scikit-learn)
- Jupyter Notebook
- Statcast / Baseball Savant data

---

## Project Structure
- notebooks/ # Jupyter notebooks for analysis and modeling
- data/ # Raw and processed datasets (not included in repo)
- reports/ # Final report and presentation slides
- docs/ # Project proposal and documentation

---

## Notes
- Data files are excluded due to size constraints.
- This project is for educational and exploratory purposes.
