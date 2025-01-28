import pandas as pd
from datetime import datetime

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
            if date_columns:
                for column in date_columns:
                    df[column] = pd.to_datetime(df[column], format='mixed')
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
    



def get_emergency_data():
    files = ["./Resources/COS2019.csv", 
             "./Resources/COS2020.csv", 
             "./Resources/COS2021.csv", 
             "./Resources/COS2022.csv", 
             "./Resources/COS2023.csv"]
    df = load_data(files, ["REPORTED", "CLOSED"])

    # Drop the  columns
    df.drop(columns=["NATURE_CODE", "NATURE_TEXT"], inplace=True)

    return df

def get_mercury_data():
    files = ["./Resources/merc_retro.csv"]
    df = load_data(files, ["start_date", "end_date"])
    return df

def get_full_moon_data():
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

def main():
    """
    TODO.
    """

if __name__ == "__main__":
    main()
