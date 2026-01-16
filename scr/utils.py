import os
import pandas as pd

def df_to_csv(df, file_name, folder_path):
    """
    Saves a DataFrame as CSV with a given name in a specific path.
    If the path does not exist, it will be created.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        file_name (str): Name of the CSV file.
        folder (str): Path where the CSV file will be saved.
    """
    try:
        os.makedirs(folder_path, exist_ok=True)
        
        complete_path = os.path.join(folder_path, file_name)

        df.to_csv(complete_path, index=False, encoding='utf-8')

        print(f"File correctly saved at: {complete_path}")

    except Exception as e:
        print(f"Error while saving file: {e}")