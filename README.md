# Customer Retention Predictor

For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

The **Customer Retention Predictor** is a Python-based tool designed to help businesses predict customer churn using historical data. This project is particularly beneficial for small businesses and MSMEs in India, allowing them to identify customers at risk of leaving and take proactive measures to retain them.

---

## Features

### Basic Version
- **Load and Preprocess Customer Data**: Supports CSV file input with data cleaning and preparation.
- **Machine Learning Model**: Implements Logistic Regression for predicting customer churn.
- **Simple GUI**: Built with Tkinter for easy interaction and displaying individual churn probabilities.

### Advanced Version (Coming Soon!)
- **Advanced ML Models**: Integration of XGBoost or Random Forest for higher accuracy.
- **Feature Importance Analysis**: Understand the factors influencing customer churn.
- **Interactive Dashboard**: Visual insights, export options, and more.

---

## File and Folder Structure

### Basic Version
```bash
CustomerRetentionPredictor/
├── data/
│   ├── customer_data.csv          # Sample customer data
├── models/
│   ├── churn_model.pkl            # Trained machine learning model
├── utils/
│   ├── __init__.py                # Initializes the utils module
│   ├── data_preprocessing.py      # Handles data cleaning and preparation
│   ├── model_training.py          # Builds and trains the ML model
│   ├── prediction.py              # Logic for making predictions
├── gui/
│   ├── __init__.py                # Initializes the GUI module
│   ├── predictor_gui.py           # GUI implementation using Tkinter
├── main.py                        # Entry point for the application
├── requirements.txt               # Dependencies required for the project
├── README.md                      # Documentation for the project
```

---

## Installation and Setup

Follow these steps to set up and run the project:

### Prerequisites
Ensure you have Python 3.8+ and `pip` installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/thekartikeyamishra/Customer-Retention-Predictor.git
cd CustomerRetentionPredictor
```

### Step 2: Set Up a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python main.py
```

---

## How It Works

1. **Load Customer Data**: Upload a CSV file containing customer information.
2. **Preprocess Data**: The tool cleans the data and prepares it for analysis.
3. **Train the Model**: The Logistic Regression model is trained on historical data to predict churn.
4. **Make Predictions**: Input individual customer data to predict churn probability.
5. **Visualize Results**: Use the GUI to view predictions in real-time.

---

## Code Details

### Data Preprocessing
- Cleans and scales the data.
- Splits the dataset into training and testing sets.

### Model Training
- Builds a Logistic Regression model.
- Saves the trained model for future use.

### Prediction
- Loads the trained model.
- Predicts churn probability for individual customers.

### GUI
- User-friendly interface using Tkinter for data input and predictions.

---

## Future Enhancements
- Support for additional programming languages (e.g., Java, C++).
- Auto-fix suggestions for common issues in customer data.
- Advanced AI models for deeper insights and better accuracy.

---

## Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request for any enhancements or bug fixes.

---

## Support and Feedback

If you encounter any issues or have suggestions, feel free to open an issue on GitHub or contact me directly.

---

## Call to Action

⭐ **Star the Repository**: [Customer Retention Predictor](https://github.com/thekartikeyamishra/Customer-Retention-Predictor)

Together, let's build smarter tools to help businesses grow!
```
