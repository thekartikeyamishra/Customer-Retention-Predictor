import tkinter as tk
from tkinter import filedialog, messagebox
from utils.prediction import load_model, predict_churn
from utils.data_processing import preprocess_data

class ChurnPredictorApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Customer Retention Predictor")

        tk.Label(self.root, text="Upload Customer Data", font=("Helvetica", 12)).pack(pady=5)
        self.upload_button = tk.Button(self.root, text="Browse", command=self.upload_file)
        self.upload_button.pack(pady=5)

        tk.Label(self.root, text="Churn Probability:", font=("Helvetica", 12)).pack(pady=5)
        self.result_text = tk.Label(self.root, text= " ", font= ("Helvetica", 12))
        self.result_text.pack(pady=5)

        self.model = load_model()
        self.scaler = None # Placeholder for scaler

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.process_data(file_path)

    def process_data(self, file_path):
        _, _, _, _, self.scaler = preprocess_data(file_path)
        messagebox.showinfo("Info", "Data processed successfully!")

    def predict(self, customer_data):
        probability = predict_churn(self.model, customer_data, self.scaler)
        self.result_text.config(text=f"{probability: .2f}")

    def run(self):
        self.root.mainloop()