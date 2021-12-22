from helper import TelecomHelper
import pandas as pd
import numpy as np

class OverViewAnalysis:
    
    def __init__(self, df):
        
        self.df = df
    
    
    def read_head(self, top=5):
        return self.df.head(top)
    
    # returning the number of rows columns and column information
    def get_info(self):
        row_count, col_count = self.df.shape
    
        print(f"Number of rows: {row_count}")
        print(f"Number of columns: {col_count}")
        print("================================")

        return (row_count, col_count), self.df.info()
    
    # gets number of distnict values in a given coumn
    def get_count(self, column_name):
        return self.df[column_name].value_counts()
    
    # getting the null count for every column
    def get_null_count(self, column_name):
        print("Null values count")
        print(self.df.isnull().sum())
        return self.df.isnull().sum()
    
    # getting the percentage of missing values
    def get_percent_missing(self):
        Helper = TelecomHelper()
        
        percent_missing = Helper.percent_missing(self.df)
        
        null_percent_df = pd.DataFrame(columns = ['column', 'null_percent'])
        columns = self.df.columns.values.tolist()
        
        null_percent_df['column'] = columns
        null_percent_df['null_percent'] = null_percent_df['column'].map(lambda x: Helper.percent_missing_for_col(self.df, x))
        
        
        return null_percent_df.sort_values(by=['null_percent'], ascending = False), percent_missing
    
    
    # returning the top handseet
    def top_handset_type(self, top=5):
        
        return self.df['handset_type'].value_counts().head(top)
    
    # returning the top handset manufactruer
    def top_manufacturer(self, top=5):
        
        return self.df['handset_manufacturer'].value_counts().head(top)
    
    # top handset by manfuctruer
    def top_handset_by_manufacturer(self, manufacturer, top=5):
        
        return self.df.groupby('handset_manufacturer')['handset_type'].value_counts()[manufacturer].head(top)
 