import time
import pandas as pd
import numpy as np
import sys
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - number of the month to filter by, or "all" to apply no month filter
        (str) day - number of the day (starting monday = 0) of week to filter by, or "all" to apply no day filter
    """
    print("_"*70)
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    #Bike grafic from internet: http://www.asciikunst.com/-Fahrrad-.html
    print ('''
                                          $"   *.
              $$$$$$$$$"                  $    J
                  ^$.                     4r  "
                  d"b                    .db
                 P   $                  e" $
        ..ec.. ."     *.              zP   $.zec..
    .^        3*b.     *.           .P" .@"4F      "4
  ."         d"  ^b.    *c        .$"  d"   $         %
 /          P      $.    "c      d"   @     3r         3
4        .eE........$r===e$$$$eeP    J       *..        b
$       $$$$$       $   4$$$$$$$     F       d$$$.      4
$       $$$$$       $   4$$$$$$$     L       *$$$"      4
4         "      ""3P ===$$$$$$"     3                  P
 *                 $       """        b                J
  ".             .P                    %.             @
    %.         z*"                      ^%.        .r"
       "*==*""                             ^"*==*""
    ''')
    print("\n")
    print("_"*70)

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("\nChoose a city!")
    print("_"*35, "\n")

    while True:
        # Input
        city = input("There is data available for Chicago, New York City and Washington.\nFor which city you like to expore Data?\nIf you want to exit the programm, please type 'exit'.\nCity: ")
        
        # Check if the input matches the given parameters
        city = city.lower().replace(" ","")
        if city == "chicago":
            break
        elif city == "newyorkcity":
            city = "new york city"
            break
        elif city == "washington":
            break
        elif city == "exit":
            print ("\nThank you for using this service!\nGoodbye!")
            sys.exit()

        # if input is not the if/else block above - invalid input
        print ('\n!!! You entered a not valid input !!!')
        print('Please only use "Chicago", "New York City" or "Washington".\nIf you want to exit the programm, please type "exit".\n\n')
        print("-"*20, "\n")



    # get user input for month (all, january, february, ... , june)
    # month as number (1-12) is also possible (not specified in text but accepted anyway)
    print("\n\nFurther filters - choose a month!")
    print("_"*35, "\n")

    while True:
        # Input
        month = input('Which month do you like to filter?\nType "all" to apply no month filter.\nMonth: ')

        #Check if month is entered as int
        try:
            month = int(month)
        except:
            # Replace possible spaces and convert to lower case
            month = month.lower().replace(" ","")    
        
        # Check if the input matches the given parameters
        if month == "january" or month == 1:
            month = 1
            break
        elif month == "february" or month == 2:
            month = 2
            break
        elif month == "march" or month == 3:
            month = 3
            break
        elif month == "april" or month == 4:
            month = 4
            break
        elif month == "may" or month == 5:
            month = 5
            break
        elif month == "june" or  month == 6:
            month = 6
            break
        elif month == "july" or month == 7:
            month = 7
            break
        elif month == "august" or month == 8:
            month = 8
            break
        elif month == "september" or month == 9:
            month = 9
            break
        elif month == "october" or month == 10:
            month = 10
            break
        elif month == "november" or month == 11:
            month = 11
            break
        elif month == "december" or month == 12:
            month = 12
            break
        elif month == "all":
            month = "all"
            break
        elif month == "exit":
            print ("\nThank you for using this service!\nGoodbye!")
            sys.exit()

        # if input is not the if/else block above - invalid input
        print ('\n!!! You entered a not valid input !!!')
        print('Please type the name of the month you like to filter (e.g. "January") or type "all" to apply no month filter.\nIf you want to exit the programm, please type "exit".\n\n')
        print("-"*20, "\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print("\n\nFurther filters - choose a day!")
    print("_"*35, "\n")

    while True:
        # Input
        day = input('Which day do you like to filter?\nType "all" to apply no day filter.\nDay: ')
        
        # Check if the input matches the given parameters
        day = day.lower().replace(" ","")
        #Only string is possible, for int-values: starting point (monday=0) is not intuitive/clear -> not accepted
        if day == "monday":
            day = 0
            break
        elif day == "tuesday":
            day = 1
            break
        elif day == "wednesday":
            day = 2
            break
        elif day == "thursday":
            day = 3
            break
        elif day == "friday":
            day = 4
            break
        elif day == "saturday":
            day = 5
            break
        elif day == "sunday":
            day = 6
            break
        elif day == "all":
            day = "all"
            break
        elif day == "exit":
            print ("\nThank you for using this service!\nGoodbye!")
            sys.exit()

        # if input is not the if/else block above - invalid input
        print ('\n!!! You entered a not valid input !!!')
        print('Please type the name of the day you like to filter (e.g. "Monday") or type "all" to apply no day filter.\nIf you want to exit the programm, please type "exit".\n\n')
        print("-"*20, "\n")


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

    print("_"*70, "\n")
    print("Loading data...")

    
    #import data for the choosen city
    df = pd.read_csv("./" + CITY_DATA[city])  

    #New column for the month of "start time": 1= January, ...
    df.insert(2, "Start Month",pd.to_datetime(df["Start Time"]).dt.month)
    #New column for the day of the week of "start time": 0 = Monday, 1 = Tuesday, 2 = Wednesday, ..., 6 = Sunday
    df.insert(3, "Start Day",pd.to_datetime(df["Start Time"]).dt.day_of_week)
    #New column for start hour
    df.insert(4, "Start Hour",pd.to_datetime(df["Start Time"]).dt.hour)

    #Filter list by month, for "all" no filter
    try:
        month = int(month)
    except:
        #no filter is set
        month = month
    else:
        #filter by month
        df = df[df["Start Month"] == month]

        
    #Filter list by day of the week, for "all" no filter
    try:
        day = int(day)
    except:
        #no filter is set
        month = month
    else:
        #filter by day
        df = df[df["Start Day"] == day]

    #check if data is available, exit if not (month July-December in the test-data set)
    if df.size == 0:
        print("Sorry, no data is available for this month.\nPlease start again.")
        print("Test data set: data is only available from January to June.")
        sys.exit()

    raw_data = input("Data is loaded and filterd correctly.\nDo you like to see the first 5 lines of the raw data? [yes/no] ")
    i=0
    while raw_data == "yes":
        print("\nLine {} to {}:".format(i, i+4))
        print(df[i:i+5])
        raw_data = input("\nDo you want to see the next 5 lines of the dataset? [yes/no] ")
        if raw_data != "yes":
            break
        else:
            i +=5
        
    print("\n")
    print("_"*70, "\n")

    #Further optional statistic (for testing)
    #print(df.head(40))
    #print("Data Size: ", df.shape)
    #print("Missing values:\n", df.isnull().sum())
    #print(df.describe())
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    monat = df.groupby(["Start Month"])["Start Time"].count()
    #if month-filter is active, no statistic will be shown
    if monat.size > 1:
        print ("Most popular month: ",calendar.month_name[monat.idxmax()], "with a count of", format(max(monat), ","), "rentals")

    # display the most common day of week
    tag = df.groupby(["Start Day"])["Start Time"].count()
    # if day-filter is active, no statisic will be shown 
    if tag.size > 1:
        print ("Mot popular day: ",calendar.day_name[tag.idxmax()], "with a count of", format(max(tag), ","), "rentals")

    # display the most common start hour
    uhr = df.groupby(["Start Hour"])["Start Time"].count()
    print ("Most popular hour: {}:00 to {}:00 with a count of {} rentals".format(uhr.idxmax(), uhr.idxmax()+1, format(max(uhr), ",")))

    print("\n     >> This took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df.groupby(["Start Station"])["Start Station"].value_counts()
    print ("Start Station: '{}' with a count of {} rentals".format(common_start.idxmax(),format(max(common_start), ",")))

    # display most commonly used end station
    common_end = df.groupby(["End Station"])["End Station"].value_counts()
    print ("End Station: '{}' with a count of {} rentals".format(common_end.idxmax(),format(max(common_end), ",")))

    # display most frequent combination of start station and end station trip
    common_start_end = df.groupby(["Start Station", "End Station"])["Start Station"].value_counts()
    print ("Comination of Start/End Station: From '{}' to '{}' with a count of {} rentals".format(common_start_end.idxmax()[0], common_start_end.idxmax()[1], format(max(common_start_end), ",")))

    print("\n     >> This took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df["Trip Duration"].sum()
    print ("The total travel time is", format(travel_time, ","), "minutes (aprox.", format(round(travel_time/10080), ","), "weeks).")

    # display mean travel time
    travel_average = df["Trip Duration"].mean()
    print ("The mean travel time is", format(travel_average, ","), "minutes (aprox.", format(round(travel_average/60), ","), "hours)")

    print("\n     >> This took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df.groupby(["User Type"])["User Type"].count()
    print("Here the type of users in the filtered data set:")
    for user in user_count.index:
        print(user, "with a count of", format(user_count[user], ","), "users")
    # User type might not be available for all data
    if df["User Type"].isnull().sum() > 0:
            print("No user type-information available for", format(df["User Type"].isnull().sum(), ","), "users")

    # Display counts of gender
    # Try, if gender information is available
    try:
        gender_count = df.groupby(["Gender"])["Gender"].count()
    except:
        print("\nThe gender is not available for this data set.")

    else:
        print("\nHere the gender of the users in the filtered data set:")
        for user in gender_count.index:
            print(user, "with a count of", format(gender_count[user], ","), "users")
        if df["Gender"].isnull().sum() > 0:
            print("No gender-information available for", format(df["Gender"].isnull().sum(), ","), "users")

    # Display earliest, most recent, and most common year of birth
    # Try, if birth year is available
    try:
        birth_year = df.groupby(["Birth Year"])["Start Time"].count()
    except:
        print("\nThe birth year is not available for this data set.")
    else:
        print("\nThe earlies year of birth is:", int(birth_year.idxmin()),"(for", format(min(birth_year), ","), "users)")
        print("The recent year of birth is", int(birth_year.idxmax()),"(for", format(max(birth_year), ","), "users)")
        print ("The most common year of birth is",int(birth_year.idxmax()), "with a count of", format(max(birth_year), ","), "users")

    print("\n     >> This took %s seconds." % (time.time() - start_time))
    print('-'*60)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print ("\nThank you for using this service!\nGoodbye!")
            break
            


if __name__ == "__main__":
	main()
