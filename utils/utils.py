import pandas as pd
from typing import List

def configfile(filepath): # Function to convert csv file into excel file
    df =pd.read_csv(filepath)
    df.to_excel("coleagues.xlsx", index=False, engine="openpyxl")

def load_collegues (filepath):

    df = pd.read_excel(filepath)
    return df["Name"].dropna().tolist()
