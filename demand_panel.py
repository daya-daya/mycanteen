import os
import pandas as pd
import streamlit as st
from datetime import datetime

DEMAND_DIR = "Demand_stock"  # Specify your directory path


def save_demand_data(data):
    file_name = "Demand_data.xlsx"
    file_path = os.path.join(DEMAND_DIR, file_name)

    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")

    # Add submission date to the new data
    data['Date'] = date_str

    # Add the submission date to the new data
    data['Date'] = date_str

    if os.path.exists(file_path):
        # Read the existing data if the file exists
        existing_data = pd.read_excel(file_path, engine='openpyxl')
        # Concatenate the new data with the existing data
        updated_data = pd.concat([existing_data, data], ignore_index=True)
    else:
        # If the file doesn't exist, initialize with new data
        updated_data = data.copy()

    # Ensure S.No is generated properly
    updated_data['S.No'] = range(1, len(updated_data) + 1)

    # Reorder columns to place 'S.No' at the first position
    columns = ['S.No'] + [col for col in updated_data.columns if col != 'S.No']
    updated_data = updated_data[columns]

    # Save the updated data to Excel
    updated_data.to_excel(file_path, index=False, engine='openpyxl')

    st.success("Thank you for your demand; we will contact you soon.")