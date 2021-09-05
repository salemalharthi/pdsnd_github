import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = [ "january", "february", "march", "april", "may", "june", "all" ]
days   = [ "monday", "tuesday", "wednesday", "thursday",
                        "friday", "saturday", "sunday", "all" ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('\nkindly enter the name of city\n').lower()
        city==CITY_DATA
        if city not in CITY_DATA:
            print('kindly choose between Chicago, new york city , or Washington\n')
        else:
             print('\nYou chose {}! We\'re going to explore its data\n'.format(city))
             break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('kindly enter the month from (all,january,february...,june) :  ').lower()
        month==months 
        if month not in months:
            print('kindly choose month either January, February, March, April, May,June or all .Please reneter\n')
        else:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('kindly enter the day  as(all,monday,tuesday,....,sunday): ').lower()
        day==days 
        if day not in days:
            print('kindly entered the day name as eihter all,monday,tuesday,wednesday,Thursday,friday, saturday or sunday.Please renter\n')
        else:
            break


    print('-'*40)
    return city, month, day 
   

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    df = pd.read_csv(CITY_DATA[city], index_col = 0)

    df['Start Time'] = pd.to_datetime(df['Start Time'])     
    df["month"] = df['Start Time'].dt.month                 
    df["week_day"] = df['Start Time'].dt.weekday_name      
    df["start_hour"] = df['Start Time'].dt.hour              
    df["start_end"] = df['Start Station'].astype(str) + ' to ' + df['End Station']

    if month != 'all':
        month_index = months.index(month) + 1              
        df = df[df["month"] == month_index ]                

    if day != 'all':
        df = df[df["week_day"] == day.title() ]             

    return df
   


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
  
    print('\nPopular times of travel ... \n')
    start_time = time.time()

    # display the most common month
    month_index = df["month"].mode()[0] - 1
    most_common_month = months[month_index].title()

    print("Most common month: ", most_common_month)

    # display the most common day of week
    most_common_day = df["week_day"].mode()[0]
    print("most common day of week: ", most_common_day)

    # display the most common start hour
    most_common_hour = df["start_hour"].mode()[0]
    print("most common hour of day: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
   
    print('\nPopular stations and trip ...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start = df['Start Station'].mode()[0]
    print("most common start station: ", most_used_start)

    # display most commonly used end station
    most_used_end = df['End Station'].mode()[0]
    print("most common end station: ", most_used_end)

    # display most frequent combination of start station and end station trip
    most_common_combination = df["start_end"].mode()[0]
    print("most common trip from start to end: ", 
            most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print("\nTrip Duration ...\n")
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("total travel time: ", total_travel_time)

    # display mean travel time
    average_time = df["Trip Duration"].mean()
    print("average travel time: ", average_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  


def user_stats(df):
    """Displays statistics on bikeshare users."""
   
    print('\nUser info ...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of user types: ", 
            df["User Type"].value_counts())

    # Display counts of gender
    if "Gender" in df:
        print("\nCounts of client`s gender")
        print("Male: ", df.query("Gender == 'Male'").Gender.count())
        print("Female: ", df.query("Gender == 'Female'").Gender.count())

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("\nEarliest year of birth: ", df["Birth Year"].min())
        print("Most recent year of birth: ", df["Birth Year"].max())
        print("Most common year of birth: ", df["Birth Year"].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()