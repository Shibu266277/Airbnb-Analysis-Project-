# Airbnb Data Analysis Web App

![Airbnb Logo](https://static-00.iconduck.com/assets.00/airbnb-icon-512x512-d9grja5t.png)

This repository contains a Streamlit web app for exploratory data analysis of Airbnb listing data. The app provides interactive visualizations to gain insights into various aspects of Airbnb listings.

## Features

- **Exploratory Analysis**: View distributions, variations, and frequencies of different features in the Airbnb dataset.
- **Interactive Visualizations**: Select different analysis options from the sidebar to explore data interactively.
- **About Section**: Learn more about the app and its features.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/airbnb-data-analysis.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run AirbnbAnalysis.py
    ```

4. Access the app in your web browser at `http://localhost:8501`.

## Files

- `AirbnbAnalysis.py`: Python script containing the Streamlit web app code.
- `AirbnbDataset.csv`: Dataset used for analysis.
- `AirbnbDatasetFromMongodb.ipynb`: Jupyter Notebook containing code for extracting data from MongoDB.
- `Airbnb_Data_Analysis_Report.pdf`: Airbnb Data Analysis Report providing insights into the analysis findings.
- **PowerBI Folder**:
    - `Airbnb.pbix`: PowerBI file containing visualization.
    - `Airbnb_Analysis.png`: Included is an image showcasing the visualization within PowerBI for a quick overview of the insights.

## About

This Streamlit web app provides an exploratory analysis of Airbnb listing data. The analysis includes various visualizations to understand different aspects of the dataset.

The app allows users to select from the following analysis options:

- Distribution of Listings by Country
- Price Variation by Selected Feature
- Frequency of Selected Feature
- Sum of Price and Beds by Number of Bedrooms
- Average Price by Cancellation Policy
- Sum of Price and Beds by Property Type
- Sum of Price and Guests Included by Cancellation Policy
- Sum of Price and Average Review Scores Rating by Number of Bathrooms

Users can select an analysis option from the sidebar to view the corresponding visualization.
