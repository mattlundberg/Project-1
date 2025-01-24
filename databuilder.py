import pandas as pd

def load_data(file_paths):
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
            dfs.append(df)
            print(f"Successfully loaded data for {file}")
        except Exception as e:
            print(f"Error loading data from {file}: {str(e)}")
    
    # Combine all DataFrames
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        print(f"\nSuccessfully combined {len(dfs)} files")
        print(f"Total records: {len(combined_df):,}")
        combined_df.dropna(inplace=True)
        return combined_df
    else:
        raise ValueError("No data files were successfully loaded")
    



def get_emergency_data():
    files = ["./Resources/COS2019.csv", 
             "./Resources/COS2020.csv", 
             "./Resources/COS2021.csv", 
             "./Resources/COS2022.csv", 
             "./Resources/COS2023.csv", 
             "./Resources/COS2024.csv"]
    return load_data(files)

def get_mercury_data():
    files = ["./Resources/merc_retro.csv"]
    return load_data(files)

def get_full_moon_data():
    files = ["./Resources/full_moons.csv"]
    return load_data(files) 

def main():
    """
    TODO.
    """

if __name__ == "__main__":
    main()
