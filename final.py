import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

VIS_ZERO_CRASH = "vis_zero_crash_rec.csv"

def read_data(file): 
    df = pd.read_csv(file)
    del df['x_cord']
    del df['y_cord']
    return df
    
def sort_df(column, type_data, df):
    new_df = df[df[column] == type_data]
    # new_df.index.tolist()
    return new_df

def extract_column(column, df):
    col_list = df[column].tolist()
    return col_list

def get_csv_for_vis(df): 
    df1 = df
    del df["dispatch_ts"]
    del df["location_type"]
    del df["xstreet1"]
    del df["xstreet2"]
    df1.to_csv("vis.csv", encoding = 'utf-8', index = False)
    # no return; saves the df1 to a csv file. 
    
def main(): 
    vis_crash = read_data(VIS_ZERO_CRASH)
    # example for sort_df()
    mv_df = sort_df("mode_type", "mv", vis_crash)
    streets = extract_column("street", mv_df)
    get_csv_for_vis(vis_crash)
main()

