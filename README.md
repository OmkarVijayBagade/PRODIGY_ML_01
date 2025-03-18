# House Price Prediction Web App

This is a Streamlit web application that predicts house prices based on square footage, number of bedrooms, and number of bathrooms.

## Features

* **Interactive Web Interface:** Users can input house features through a user-friendly Streamlit interface.
* **Linear Regression Model:** The app uses a pre-trained linear regression model to predict house prices.
* **Model Persistence:** The model is trained in a Jupyter Notebook and saved as `model.pkl` for efficient loading.
* **Background Image:** A house-related background image enhances the app's visual appeal.
* **Image display:** A house image is displayed within the app.

## Getting Started

### Prerequisites

* Python 3.6+
* pip

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/OmkarVijayBagade/PRODIGY_ML_01.git
    cd house-price-prediction
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2.  **Open the app in your browser:**

    * Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser.

3.  **Enter house features:**

    * Input the square footage, number of bedrooms, and number of bathrooms.

4.  **Predict the price:**

    * Click the "Predict Price" button to see the predicted house price.

### Files

* `app.py`: The Streamlit application code.
* `model.pkl`: The trained linear regression model.
* `house_prices.csv`: The dataset used to train the model.
* `house_image.jpg`: Image displayed in the app.
* `requirements.txt`: The list of Python dependencies.
* `README.md`: This file.
* `train_model.ipynb`: Jupyter notebook used to train the model.

### Training the Model

The `model.pkl` file is created using the `train_model.ipynb` Jupyter Notebook. To retrain the model or use a different dataset:

1.  Open `train_model.ipynb` in Jupyter Notebook.
2.  Modify the dataset or model parameters as needed.
3.  Run all cells to train and save the model.

### Deployment

This app can be deployed to Streamlit Community Cloud:

1.  Create a GitHub repository containing all project files.
2.  Create a Streamlit Community Cloud account.
3.  Deploy the app from your GitHub repository.

### Dataset

The `house_prices.csv` dataset is generated using a Python script. You can replace it with your own dataset.

### Image

The `house_image.jpg` image is used to enhance the visual appeal of the app. Replace it with your own image if desired.

### Author

* [Omkar Bagade/GitHub Username: OmkarVijayBagade]

