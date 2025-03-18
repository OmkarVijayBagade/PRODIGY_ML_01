import pandas as pd
import numpy as np

def generate_house_data(num_samples=1000):
    """Generates a synthetic house price dataset."""

    np.random.seed(42)  # For reproducibility

    square_footage = np.random.randint(800, 3500, num_samples)
    bedrooms = np.random.randint(1, 5, num_samples)
    bathrooms = np.random.randint(1, 4, num_samples)

    # Generate base prices with some noise
    base_prices = 100 * square_footage + 50000 * bedrooms + 30000 * bathrooms
    noise = np.random.normal(0, 50000, num_samples)  # Add noise for realism
    prices = base_prices + noise

    # Ensure prices are non-negative
    prices = np.maximum(prices, 50000)

    data = {
        'square_footage': square_footage,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'price': prices,
    }

    df = pd.DataFrame(data)
    return df

# Generate and save the dataset
house_df = generate_house_data()
house_df.to_csv('house_prices.csv', index=False)

print("Dataset 'house_prices.csv' generated successfully.")

# Example of how to use the generated dataset in your app.py
# (replace your_data.csv with house_prices.csv)

#In app.py change the line:
# df = pd.read_csv('your_data.csv')
# to
# df = pd.read_csv('house_prices.csv')