import pandas as pd
from datetime import datetime

emergency_df=pd.DataFrame()
full_moon_df=pd.DataFrame()
mercury_df=pd.DataFrame()
new_moon_df=pd.DataFrame()


def load_data(file_paths, date_columns = None):
    """
    Loads and combines data from CSV files into a single pandas DataFrame.
    
    Parameters:
        file_paths (list): List of paths to CSV files to load
        
    Returns:
        pandas.DataFrame: Combined DataFrame containing all records from input files
        
    Raises:
        ValueError: If no files were successfully loaded
    """    
    # Initialize empty list to store DataFrames
    dfs = []
    
    for file in file_paths:
        try:
            df = pd.read_csv(file)
            print(f"Loading {file}")
            if date_columns:
                df[date_columns] = df[date_columns].apply(pd.to_datetime, format='mixed')
            dfs.append(df)
            print(f"Successfully loaded data for {file}")
        except Exception as e:
            print(f"Error loading data from {file}: {str(e)}")
    
    # Combine all DataFrames
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        print(f"\nSuccessfully combined {len(dfs)} files")
        print(f"Total records: {len(combined_df):,}")
        
        #combined_df.dropna(inplace=True)
        return combined_df
    else:
        raise ValueError("No data files were successfully loaded")
    
def load_all_data():
    global emergency_df, full_moon_df, mercury_df, new_moon_df
    emergency_df = load_emergency_data()
    full_moon_df = load_full_moon_data()
    mercury_df = load_mercury_data()
    new_moon_df = load_new_moon_data()
    
def get_emergency_data():
    global emergency_df
    if emergency_df.empty:
        emergency_df=load_emergency_data()
    return emergency_df

def get_mercury_data():
    global mercury_df
    if mercury_df.empty:
        mercury_df=load_mercury_data()
    return mercury_df

def get_full_moon_data():
    global full_moon_df
    if full_moon_df.empty:
        full_moon_df=load_full_moon_data()
    return full_moon_df

def get_new_moon_data():
    global new_moon_df
    if new_moon_df.empty:
        new_moon_df=load_new_moon_data()
    return new_moon_df

def load_emergency_data():
    """
    Loads and returns the emergency data.
    """
    files = ["./Resources/COS2019.csv", 
             "./Resources/COS2020.csv", 
             "./Resources/COS2021.csv", 
             "./Resources/COS2022.csv", 
             "./Resources/COS2023.csv"]
    df = load_data(files, ["REPORTED", "CLOSED"])

    # Drop the  columns
    df.drop(columns=["NATURE_CODE", "NATURE_TEXT", "INCIDENT_ADDRESS", "_id"], inplace=True)

    return df


def load_mercury_data():
    """
    Loads and returns the Mercury retrograde data.
    """
    files = ["./Resources/merc_retro.csv"]
    df = load_data(files, ["start_date", "end_date"])
    return df


def load_full_moon_data():
    """
    Loads and returns the full moon data.
    """
    files = ["./Resources/full_moons.csv"]
    df = load_data(files) 

    #Convert Data Types
    # Combine date and time columns into a single datetime column
    df["DateTime"] = pd.to_datetime(df["Date"] + " " + df["Time"], format="mixed")
    
    # Drop original separate columns
    df.drop(columns=["Date", "Time"], inplace=True)
    
    # Replace the flags with the correct names
    df['Flag'] = df["Flag"].fillna("Full")
    df['Flag'] = df["Flag"].str.replace("[+]", "Blue")
    df['Flag'] = df["Flag"].str.replace(r"[*]", "Partial Eclipse")
    df['Flag'] = df["Flag"].str.replace(r"[**]", "Total Eclipse")
    df['Flag'] = df["Flag"].str.replace("[/]", "Prenumbral Eclipse")

    # Columns to drop

    return df


def load_new_moon_data():
    """
    Loads and returns the new moon data.
    """
    files = ["./Resources/Newmoondata.csv"]
    df = load_data(files, ["DateTime"])
    
    # Drop any columns with 'Unnamed' in their name
    unnamed_cols = [col for col in df.columns if 'Unnamed' in col]
    
    df.drop(columns=unnamed_cols, inplace=True)
    return df

def main():
    """
    Loads all the data
    """
    load_all_data()

if __name__ == "__main__":
    main()
