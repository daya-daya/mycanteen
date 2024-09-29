import os
import pandas as pd
from datetime import datetime


# Directory for storing search logs
LOG_DIR = "search_log"
os.makedirs(LOG_DIR, exist_ok=True)

SEARCH_LOG_FILE = os.path.join(LOG_DIR, "search_log.xlsx")

def log_search(search_term):
    """
    Logs the search term and timestamp, updating the existing entry or adding a new one.

    Parameters:
        search_term (str): The search term entered by the user.

    Returns:
        None
    """
    if not search_term.strip():  # Check if search term is empty
        print("No search term provided. No record added.")
        return

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a new entry
    new_entry = {"Search Term": search_term, "Timestamp": timestamp, "Search Count": 1}

    # Check if the search log file exists
    if os.path.exists(SEARCH_LOG_FILE):
        # Append the new entry to the existing file
        with pd.ExcelWriter(SEARCH_LOG_FILE, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            # Load existing log into a DataFrame
            search_log = pd.read_excel(SEARCH_LOG_FILE, engine='openpyxl')
            # Check if 'Search Term' column exists
            if "Search Term" in search_log.columns:
                # Check if the search term already exists in the log
                if search_term in search_log["Search Term"].values:
                    # Update the count and timestamp for the existing term
                    search_log.loc[search_log["Search Term"] == search_term, "Search Count"] += 1
                    search_log.loc[search_log["Search Term"] == search_term, "Timestamp"] = timestamp
                else:
                    # Add a new entry to the log
                    search_log = pd.concat([search_log, pd.DataFrame([new_entry])], ignore_index=True)
            else:
                print("Error: 'Search Term' column is missing in the log file.")
                return
            # Save the updated log back to the Excel file
            search_log.to_excel(writer, index=False, sheet_name='Sheet1')
    else:
        # Create a new DataFrame and save it to a new file
        search_log = pd.DataFrame([new_entry])
        with pd.ExcelWriter(SEARCH_LOG_FILE, engine='openpyxl') as writer:
            search_log.to_excel(writer, index=False, sheet_name='Sheet1')

# Example usage
#if __name__ == "__main__":
    # Fetch previous searches
   # previous_searches = get_previous_searches()

    # Get the search term from the user (replace this with your search input in the app)
   # search_term = input("Enter the item to search: ").strip()

    # Correct the search term based on previous searches
   # corrected_term = search_nlp_correction(search_term, previous_searches)

    # Log the search
    #log_search(corrected_term)

    # Print the corrected search term
    #print(f"Corrected Search Term: {corrected_term}")
