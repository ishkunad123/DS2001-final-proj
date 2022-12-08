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
    """ 
    taktes data from csv stores it into df and cleans it. 
        file: name of csv file
    returns: df - dataframe of cleaned csv  
    """
    # reads data into pd.df
    df = pd.read_csv(file)
    # deletes unnecessary columns 
    del df['x_cord']
    del df['y_cord']
    return df 
    
def sort_df(column, type_name, df):
    """ 
    sorts specific rows into new df based on the column and type.
        column: column we want to sort by
        type_name: rows we sort by 
    returns: df - new sorted df 
    """
    new_df = df[df[column] == type_name]
    return new_df

def extract_column(column, df):
    """ 
     extracts column from df into a list
        column: column we're sorting
        df: dataframe we're extracting from
    returns: col_list - list of column
    """
    col_list = df[column].tolist()
    return col_list

def get_csv_for_vis(df): 
    """ 
     modifies df into new df and saves as csv for datawrapper purposes 
        df: dataframe we're modifying
    returns: nothing
    """
    df1 = df
    # deletes unnecessary columns 
    del df["dispatch_ts"]
    del df["location_type"]
    del df["xstreet1"]
    del df["xstreet2"]
    # saves df as a .csv file
    df1.to_csv("vis.csv", encoding = 'utf-8', index = False)
    # no return; saves the df1 to a csv file. 
    
def transportation_graph(df):
    '''
    creates a pie chart of the frequencies of motor vehicle, pedestrian, and bike accidents
        df: cleaned dataframe
    returns: pie chart of frequencies with values and percentages
    '''
    # calls extract_column function to extract mode column
    types = extract_column("mode_type", df)
    
    # finds the frequency of each type of accident from the column
    mv_count = types.count("mv")
    bike_count = types.count("bike")
    ped_count = types.count("ped")
    
    # creating labels, values, and color lists for the pie chart
    transportation_methods = ["Motor Vehicle", "Bike", "Pedestrian"]
    counts = [mv_count, bike_count, ped_count]
    colors = ["#78BDF3", "blue", "purple"]
    
    # plotting the pie chart
    plt.pie(counts, labels = list(zip(transportation_methods, counts)), colors = colors, autopct = '%.1f')
    fig = plt.figure(figsize =(10, 7))
    # saving figure
    plt.savefig("transportation_pie.pdf", bbox_inches = "tight")
    # showing pie chart
    plt.show()

def year_graph(df):
    '''
    creates bar chart of the frequencies of accidents per year from 2015-2022
        df: cleaned dataframe 
    returns: bar chart of frequencies of accidents per year
    '''
    # calls extract_column function to extract the year and time of the accident
    year = extract_column("dispatch_ts", df)
    
    # creates lists for all the years that an accident happened
    fifteen = []
    sixteen = []
    seventeen = []
    eighteen = []
    nineteen = []
    twenty = []
    twenty_one = []
    twenty_two = []
    
    # for loop to filter through time and year and add the values to appropriate lists we've created
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

    # creating titles and values for bar chart 
    years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
    counts = [len(fifteen), len(sixteen), len(seventeen), len(eighteen), len(nineteen), 
               len(twenty), len(twenty_one), len(twenty_two)]
    # color list
    year_colors = ["purple", "pink", "violet", "green", "blue", "magenta", "olive", "indigo"]
    # plotting bar chart
    plt.bar(years, counts, color = year_colors, alpha = 0.6)
    
    # chart, x-axis, and y-axis titles
    plt.title("Frequency of Accidents Per Year")
    plt.xticks(rotation = 30, horizontalalignment = "center")
    plt.xlabel("Year")
    plt.ylabel("Accidents")
    # saving figure
    plt.savefig("year_graph.pdf", bbox_inches = "tight")
    # showing bar chart 
    plt.show()

def year_breakdown(df):
    """ 
     plots the breakdowns of the year graph by ped, mv, and bike
        df: dataframe data is coming from 
    returns: nothing
    """
    years = []
    # loops through the rows in df 
    for index, row in df.iterrows(): 
        # checks the year of each row 
        year_row = row["dispatch_ts"]
        pieces = year_row.strip().split("-")
        year = pieces[0]
        # if the year is not in the years list, then we append that year to the
        # list
        if year != None: 
            if year not in years: 
                years.append(year)
    mv = []
    bike = []
    ped = []
    # loops through all the saved years in the years list. 
    for x in years:
        mv_count = 0
        bike_count = 0
        ped_count = 0
        # loops through the whole df 
        for index, row in df.iterrows(): 
            # compares the row to the year we're looping through in the list
            year_row = row["dispatch_ts"]
            pieces = year_row.strip().split("-")
            year = pieces[0]
            # if that year matches, then we can check to see what type of 
            # accident that row contains and adds a count depending on 
            # which type of accident it is. 
            if year == x: 
                type_row = row["mode_type"]
                if type_row == "mv": 
                    mv_count += 1
                elif type_row == "bike": 
                    bike_count += 1
                else: 
                    ped_count += 1
        # appends all the counts to each corresponding types
        mv.append(mv_count)
        bike.append(bike_count)
        ped.append(ped_count)
    
    # graphs stacked bar chart for each mode type
    fig, ax = plt.subplots()
    ax.bar(years, mv, color = "#78BDF3", label = "Motor Vehicle")
    ax.bar(years, bike, color = "blue", label = "Bike")
    ax.bar(years, ped, color = "purple", bottom = bike, label ="Pedestrian")
    # chart housecleaning
    ax.set_ylabel("Frequency of Accident")
    ax.legend()   
    plt.savefig("year_distr_graph.pdf", bbox_inches = "tight")
    plt.show()

def most_dangerous_street(df):
    """ 
     finds the most dangerous street and plots the counts for the 
     most dangerous street
        df: dataframe data is coming from 
    returns: nothing
    """
    street_freqs = {}
    for index, row in df.iterrows(): 
        # checks to see if the street name is not Null
        name = row["street"]
        if name != None: 
            # if the street name is not a key in the street_freqs dict
            if name not in street_freqs: 
                # create new df containing only rows w/ that street name
                name_df = sort_df("street", name, df)
                # store the len of that df as a value to its assigned key name
                street_freqs[name] = len(name_df)
    # find max in the dict. 
    max_street = max(street_freqs, key=street_freqs.get)
    # find individual counts of each mode type and store it into ints
    max_st_df = sort_df("street", max_street, df)
    ped = len(sort_df("mode_type", "ped", max_st_df))
    mv = len(sort_df("mode_type", "mv", max_st_df))
    bike = len(sort_df("mode_type", "bike", max_st_df))
    # lists for graphing
    mode_names = ["Motor Vehicle", "Bike", "Pedestrian"]
    mode_counts = [mv, bike, ped]
    mode_colors = ["#78BDF3", "blue", "purple"]
    # graph distribution 
    plt.bar(mode_names, mode_counts, color = mode_colors)
    plt.xticks(rotation = 30, horizontalalignment = "center")
    plt.title("Accidents by Mode type on " + max_street)
    plt.xlabel("Mode of Transportation")
    plt.ylabel("Accidents")
    plt.savefig("most_dangerous_graph.pdf", bbox_inches = "tight")
    plt.show()       

def main(): 
    '''
    the main function graphs four charts: three bar charts and one pie chart
    '''
    vis_crash = read_data(VIS_ZERO_CRASH)

    transportation_graph(vis_crash)
    year_graph(vis_crash)
    plt.show()
    
    year_breakdown(vis_crash)
    
    most_dangerous_street(vis_crash)
    get_csv_for_vis(vis_crash)
    
main()
