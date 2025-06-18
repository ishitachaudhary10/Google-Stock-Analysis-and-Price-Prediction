# 📈 Google Stock Analysis & Price Prediction  

This project explores the historical stock performance of Google (GOOGL) through a combination of exploratory data analysis and machine learning. Using Python, the dataset is cleaned, visualized, and modeled to better understand price trends and even attempt to forecast future stock behavior using a regression-based approach.

---

## 🗂️ Dataset  

The data used in this project comes from Kaggle, specifically the "Google Stocks Historical Data" dataset. It contains daily stock market records for Google over several years, making it ideal for time series analysis and pattern discovery.  

The dataset is provided in CSV format and includes columns like `Date`, `Open`, `High`, `Low`, `Close`, and `Volume`. These fields are standard in financial datasets and provide enough granularity for performing both basic analysis and machine learning tasks.

---

## 🛠️ Technologies Used  

The project is built using Python 3, a popular and accessible language for data science. All scripts are designed to run efficiently in local Jupyter environments or cloud-based platforms like Kaggle Notebooks.  

Key Python libraries used include Pandas and NumPy for data manipulation, Matplotlib and Seaborn for visual analytics, and Scikit-learn for implementing machine learning models. The KaggleHub library is used to streamline dataset downloading directly within the script.

---

## 📌 Project Workflow  

### 1. Environment Setup  

The project begins by importing all necessary libraries for data handling, plotting, and modeling. It also configures the environment by suppressing warnings and setting up Matplotlib to work with non-GUI backends, ensuring compatibility with cloud platforms.

### 2. Data Loading  

The dataset is downloaded automatically using the KaggleHub library, eliminating the need for manual downloads. All available CSV files in the dataset directory are listed, and one is selected for analysis. The selected CSV is then read into a Pandas DataFrame.

### 3. Preprocessing  

The `Date` column is converted into proper datetime format to allow time-based grouping and sorting. Any rows with missing or malformed dates are removed, and the DataFrame index is reset. A data type check is also performed to confirm that all columns are in the correct format for analysis.

### 4. Exploratory Data Analysis (EDA)  

Various types of visualizations are used to explore the dataset. Histograms reveal the distribution of closing prices, while pair plots display relationships between key numerical features. Box plots are employed to detect outliers, and a correlation heatmap is used to understand inter-feature relationships. Additionally, a day-of-the-week plot provides insight into trading behavior over the week.

### 5. (Optional) Modeling  

While the primary focus is on EDA, the project also lays the foundation for machine learning by allowing the integration of models like Random Forest Regressor. This model can be trained to predict closing prices based on other available features such as `Open`, `High`, `Low`, and `Volume`.

---

## 📊 Visualizations  

### 📉 Histograms  

Histograms are used to show how frequently various closing price values occur. This helps identify common price ranges and any skew in the distribution.

### 🔗 Pair Plots  

Pair plots visually explore the relationships between numerical variables such as `Open`, `High`, `Low`, `Close`, and `Volume`, helping spot patterns and correlations at a glance.

### 📦 Box Plots  

Box plots help identify potential outliers and detect the spread and symmetry in each of the stock's price components. This is crucial for understanding volatility.

### 🔥 Correlation Heatmap  

The heatmap visually represents the correlation matrix of the dataset, showing how strongly each numerical feature is related to the others. This is especially useful for feature selection.

### 📅 Day-of-Week Frequency  

This plot shows how many stock data points are available for each day of the week. It helps confirm trading patterns and can be useful for detecting weekly cycles or anomalies.

---

## 🧠 Possible Extensions  

This project can be extended by incorporating more advanced time-series forecasting models such as ARIMA or LSTM for sequential prediction. Technical indicators like Moving Averages, RSI, and MACD can also be engineered to enhance model performance.  

You may further expand the project by integrating sentiment analysis from financial news or Reddit posts to see how external sentiment correlates with price changes. Finally, the entire pipeline could be turned into a deployable dashboard or web application for real-time stock prediction.

---

## ▶️ How to Run  

To run the project locally, ensure that you have Python 3.8 or higher installed. Use `pip` to install the necessary libraries including Pandas, Seaborn, Scikit-learn, and KaggleHub.  

Once dependencies are installed, you can run the notebook in Jupyter or directly within Kaggle Notebooks. The dataset will be downloaded automatically during execution, and all plots will be generated inline for interactive exploration.

---
