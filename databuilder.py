import pandas as pd
from datetime import datetime


class DataBuilder:
    def __init__(self):
        self.emergency_df = self.load_emergency_data()
        self.full_moon_df = self.load_full_moon_data()
        self.mercury_df = self.load_mercury_data()
        self.new_moon_df = self.load_new_moon_data()

    def load_data(self, file_paths, date_columns = None):
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
        
    def get_emergency_data(self):
        if self.emergency_df.empty:
            self.emergency_df = self.load_emergency_data()
        return self.emergency_df

    def get_mercury_data(self):
        if self.mercury_df.empty:
            self.mercury_df = self.load_mercury_data()
        return self.mercury_df

    def get_full_moon_data(self):
        if self.full_moon_df.empty:
            self.full_moon_df = self.load_full_moon_data()
        return self.full_moon_df

    def get_new_moon_data(self):
        if self.new_moon_df.empty:
            self.new_moon_df = self.load_new_moon_data()
        return self.new_moon_df

    def load_emergency_data(self):
        """
        Loads and returns the emergency data.
        """
        files = ["./Resources/COS2019.csv", 
                 "./Resources/COS2020.csv", 
                 "./Resources/COS2021.csv", 
                 "./Resources/COS2022.csv", 
                 "./Resources/COS2023.csv"]
        df = self.load_data(files, ["REPORTED", "CLOSED"])

        # Drop the  columns
        df.drop(columns=["NATURE_CODE", "NATURE_TEXT", "INCIDENT_ADDRESS", "_id"], inplace=True)

        return df

    def load_mercury_data(self):
        """
        Loads and returns the Mercury retrograde data.
        """
        files = ["./Resources/merc_retro.csv"]
        df = self.load_data(files, ["start_date", "end_date"])
        return df

    def load_full_moon_data(self):
        """
        Loads and returns the full moon data.
        """
        files = ["./Resources/full_moons.csv"]
        df = self.load_data(files) 

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

    def load_new_moon_data(self):
        """
        Loads and returns the new moon data.
        """
        files = ["./Resources/Newmoondata.csv"]
        df = self.load_data(files, ["DateTime"])
        
        # Drop any columns with 'Unnamed' in their name
        unnamed_cols = [col for col in df.columns if 'Unnamed' in col]
        
        df.drop(columns=unnamed_cols, inplace=True)
        return df

    def main(self):
        """
        Nothing to see here
        """