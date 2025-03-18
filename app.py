import streamlit as st 
import joblib 
import numpy as np 
from PIL import Image

model = joblib.load('model.pkl')

def main():
    st.title("House Price Prediction")
    
    image = Image.open("house_image.jpg")
    resized_image = image.resize((600,250))

    st.image(resized_image, caption="A Pretty house",use_container_width=False)
    
    st.header("Make a Prediction")
    square_footage = st.number_input("Square Footage", min_value=100, value=1500)
    bedrooms = st.number_input("Bedrooms",min_value=1, value=2)
    bathrooms = st.number_input('Bathrooms',min_value=1, value=2)

    if st.button("Predict Price"):
        prediction = model.predict([[square_footage,bedrooms,bathrooms]])
        st.write(f"Predicted Price: {prediction[0]:.2f}")
    
    
    
if __name__ == "__main__":
    main()