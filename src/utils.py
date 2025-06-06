# utils.py
import pandas as pd

def load_colleagues(filename: str) -> list:
    """
    Reads the input from a CSV file name specified on the command line
    
    Parameters:
    - filename (str): Path to the CSV file containing the list of colleagues.
    
    Returns:
    - list: A list of colleague names.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        return []
