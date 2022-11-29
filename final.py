#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:59:14 2022

@author: ishanikunadharaju
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

VIS_ZERO_CRASH = "vis_zero_crash_rec.csv"

def read_data(file): 
    df = pd.read_csv(file)
    del df['x_cord']
    del df['y_cord']
    return df 
    
def sort_df(column, type, df):
    new_df = df[df[column] == type]
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
    # test
def transportation_graph(df):
    types = extract_column("mode_type", df)
    
    mv_count = types.count("mv")
    bike_count = types.count("bike")
    ped_count = types.count("ped")
    
    transportation_methods = ["Motor Vehicle", "Bike", "Pedestrian"]
    counts = [mv_count, bike_count, ped_count]
    colors = ["purple", "pink", "violet"]
    plt.bar(transportation_methods, counts, color = colors, alpha = 0.8)
    
    plt.title("Frequency of Accidents for Transportation Methods")
    plt.xticks(rotation = 30, horizontalalignment = "center")
    plt.title("Frequency of Accidents for Transportation Methods")
    plt.xlabel("Transportation Method")
    plt.ylabel("Accidents")
        
    plt.show
    plt.savefig("transportation_graph.pdf", bbox_inches = "tight")

def year_graph(df):
    year = extract_column("dispatch_ts", df)
    
    fifteen = []
    sixteen = []
    seventeen = []
    eighteen = []
    nineteen = []
    twenty = []
    twenty_one = []
    twenty_two = []
    
    for value in year:
        if value[:4] == "2015":
            fifteen.append(value)
        elif value[:4] == "2016":
            sixteen.append(value)
        elif value[:4] == "2017":
            seventeen.append(value)
        elif value[:4] == "2018":
            eighteen.append(value)
        elif value[:4] == "2019":
            nineteen.append(value)
        elif value[:4] == "2020":
            twenty.append(value)
        elif value[:4] == "2021":
            twenty_one.append(value)
        elif value[:4] == "2022":
            twenty_two.append(value)
    

    years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
    counts = [len(fifteen), len(sixteen), len(seventeen), len(eighteen), len(nineteen), 
               len(twenty), len(twenty_one), len(twenty_two)]
    year_colors = ["purple", "pink", "violet", "green", "blue", "magenta", "olive", "indigo"]
    plt.bar(years, counts, color = year_colors, alpha = 0.6)
    
    plt.title("Frequency of Accidents Per Year")
    plt.xticks(rotation = 30, horizontalalignment = "center")
    plt.xlabel("Year")
    plt.ylabel("Accidents")

    plt.show
    plt.savefig("year_graph.pdf", bbox_inches = "tight")


def main(): 
    vis_crash = read_data(VIS_ZERO_CRASH)
    # example for sort_df()
    mv_df = sort_df("mode_type", "mv", vis_crash)
    extract_column("street", mv_df)
    transportation_graph(vis_crash)
    plt.show()
    year_graph(vis_crash)
    
    
    get_csv_for_vis(vis_crash)
main()
