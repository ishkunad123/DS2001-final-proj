#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alina Gonzalez & Ishani Kunadharaju
DS2001 Final Project 

Analysis of Crashes in Boston
"""
import matplotlib.pyplot as plt
import pandas as pd

VIS_ZERO_CRASH = "vis_zero_crash_rec.csv"

def read_data(file): 
    df = pd.read_csv(file)
    del df['x_cord']
    del df['y_cord']
    return df 
    
def sort_df(column, type_name, df):
    new_df = df[df[column] == type_name]
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
        
    plt.show()
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

    plt.savefig("year_graph.pdf", bbox_inches = "tight")
    


def most_dangerous_street(df):
    street_freqs = {}
    for index, row in df.iterrows(): 
        name = row["street"]
        if name != None: 
            if name not in street_freqs: 
                name_df = sort_df("street", name, df)
                street_freqs[name] = len(name_df)
    max_street = max(street_freqs, key=street_freqs.get)

    max_st_df = sort_df("street", max_street, df)
    ped = len(sort_df("mode_type", "ped", max_st_df))
    mv = len(sort_df("mode_type", "mv", max_st_df))
    bike = len(sort_df("mode_type", "bike", max_st_df))
    
    mode_names = ["Motor Vehicle", "Bike", "Pedestrian"]
    mode_counts = [mv, bike, ped]
    mode_colors = ["violet", "blue", "green"]
    
    plt.bar(mode_names, mode_counts, color = mode_colors, alpha = 0.6)
    plt.xticks(rotation = 30, horizontalalignment = "center")
    plt.title("Accidents by Mode type on " + max_street)
    plt.xlabel("Mode of Transportation")
    plt.ylabel("Accidents")
    plt.show()
    return max_street        

def main(): 
    vis_crash = read_data(VIS_ZERO_CRASH)

    transportation_graph(vis_crash)
    year_graph(vis_crash)
    plt.show()
    
    
    most_dangerous_street(vis_crash)
    get_csv_for_vis(vis_crash)
main()
