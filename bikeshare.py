import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("""\nInput the city you would like to explore its bikeshare data?
            Newyork, Chicago or Washington!\n""").lower()

            #Check input validity
            if (city.replace(' ','') == 'washington') or (city.replace(' ','') == 'newyork') or (city.replace(' ','') == 'chicago'):
                if (city.replace(' ','') in CITY_DATA):
                    break
            else:
                print('\nWrong input, try again! \n')
                continue

        except (ValueError, KeyboardInterrupt) as e:
            print('\nInvalid Input, try again!! \n')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        try:
            print('\nInput which month to display its data')

            month = input('Data is valid from January to June, enter "all" to consider all months\n').lower()

            #Check input validity
            if month.isalpha():
                if (month == 'january') or (month == 'february') or (month == 'march') or (month == 'april') or (month == 'may') or (month == 'june') or (month == 'all'):
                    break
            else:
                print('\nPlease try again\n')
                continue
        except KeyboardInterrupt:
            print('\nError, try again!! \n')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\nEnter the days to veiw as Monday, Tuesday..etc, enter "all" to consider all\n').lower()

            #Check input validity
            if day.isalpha():
                if (day == 'monday') or (day == 'tuesday') or (day == 'wednesday') or (day == 'thursday') or (day == 'friday') or (day == 'saturday') or (day == 'sunday') or (day == 'all'):
                    break
            else:
                print('\nWrong input, try again\n')
                continue
        except KeyboardInterrupt:
            print('Error, try again! \n')
            continue


    print('+'*50)
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

    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int

        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nThe Most Common Times of Trips..\n')
    start_time = time.time()

    # TO DO: display the most common month

    # find the most common month (Jan to June)
    common_month = df['month'].mode()[0]

    # find count of popular month
    month_count = df['month'].value_counts()[common_month]

    print('\nMost Common Month of travel:\n', months[common_month-1].title(), '\n Count: ', month_count)


    # TO DO: display the most common day of week

    # find the most common day_of_week

    common_day_of_week = df['day_of_week'].mode()[0]

    # find popular day of the week count
    common_day_of_week_count = df['day_of_week'].value_counts()[common_day_of_week]

    print('\nMost Common Day of travel:\n', common_day_of_week, '\n Count: ', common_day_of_week_count)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    frequent_hour = df['hour'].mode()[0]

    # find count of popular hour
    frequent_hour_count = df['hour'].value_counts()[frequent_hour]

    print('\nMost Common Start Hour of travel:\n', frequent_hour, '\n Count: ', frequent_hour_count)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('+'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nFinding The Most Frequent Stations and Trips...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['Most Common Start Station'] = df['Start Station']

    # find most common Start Station
    common_start_station = df['Most Common Start Station'].mode()[0]

    # find most common Start Station count
    common_StartStation_count = df['Most Common Start Station'].value_counts()[common_start_station]

    print('\nMost Commmon Start Station: \n', common_start_station, '\n Count: ', common_StartStation_count)

    # TO DO: display most commonly used end station

    df['Most Common End Station'] = df['End Station']

    # find most common End Station
    common_end_station = df['Most Common End Station'].mode()[0]

    # find most common End Station count
    common_EndStation_count = df['Most Common End Station'].value_counts()[common_end_station]

    print('\nMost Frequent End Station: \n', common_end_station, '\n Count: ', common_EndStation_count)

    # TO DO: display most frequent combination of start station and end station trip

    df['Routes'] = df['Start Station'] + '   - & -   ' + df['End Station']

    # find most common Routes
    common_trip = df['Routes'].mode()[0]

    # count the iteration of coomon routes
    common_trip_count = df['Routes'].value_counts()[common_trip]

    print('\nMost Common Trip: \n', common_trip, '\n Count: ', common_trip_count)


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('+'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    #Sum the trip duration column
    tot_travel_time = df['Trip Duration'].sum()

    #print total travel time
    print(str(tot_travel_time) + ' seconds')

    #find travel time in hh:mm:ss
    #https://stackoverflow.com/questions/1384406/convert-seconds-to-hhmmss-in-python

    tot_travel_time = (str(int(tot_travel_time//86400)) +
                         'd ' +
                         str(int((tot_travel_time%86400)//3600)) +
                         'h ' +
                         str(int(((tot_travel_time%86400) % 3600)//60)) +
                         'm ' +
                         str(int(((tot_travel_time%86400)%3600)% 60)) +
                         's')

    print('Travel time is: ', tot_travel_time)


    # TO DO: display mean travel time
    time_mean = df['Trip Duration'].mean()

    #print mean travel time
    print(str(time_mean) + ' seconds')

    #Calculation procedure was adopted from here:
    #https://stackoverflow.com/questions/1384406/convert-seconds-to-hhmmss-in-python
    #Below we check if mean < 3600 or > 3600 seconds
    if time_mean < 3600:
        time_mean = (str(int(time_mean//60)) + 'm '
                                  + str(int(time_mean%60)) + 's')
    else:
        time_mean = (str(int(time_mean//3600)) + 'h '
                         + str(int((time_mean%3600)//60)) + 'm '
                         + str(int((time_mean%3600)%60)) + 's')

    print('Mean travel time is: ', time_mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('+'*50)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Statistics...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    #Counts each user type, if none is given, they are replaced by 'Not Specified'
    user_types_count = df['User Type'].value_counts()

    print('\n++++++++++++++++++\n')
    print(user_types_count)


    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if (city.replace(' ','').isalpha()) and (city.replace(' ','') != 'washington'):

        #Counts the gender types, if none is given, they are replaced by 'Not Specified'
        gender_count = df['Gender'].value_counts()

        print('\n++++++++++++++++++\n')

        print(gender_count)

        #find earliest birth year
        earliest_BirthYear = int(df['Birth Year'].min())
        print('\n++++++++++++++++++\n')

        print('\n Earliest birth year is... ',earliest_BirthYear)
        print('\n++++++++++++++++++\n')

        #find most recent birth year
        recent_BirthYear = int(df['Birth Year'].max())
        print('\n Most recent birth year is... ',recent_BirthYear)
        print('\n++++++++++++++++++\n')

        #find frequent birth year
        common_BirthYear = int(df['Birth Year'].mode()[0])
        print('\n Most common birth year is... ', common_BirthYear)
        print('\n++++++++++++++++++\n')

    else:

        print('\n{} does not include gender/birthdate data!'.format(CITY_DATA[city].title()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('+'*50)


def raw_data(df):
    """ This function displays raw data upon user approval """
    #Ask user to display raw data
    try:
        view = input('\nDisplay raw data?\n')
    except KeyboardInterrupt:
        print('\nError, Exiting raw_data()')
        return None

    start = 0

    if (view.lower() != 'yes'):

        return None
    else:
        #iterate through the index of df
        for i in range(len(df.index)):
            print('\n')
            print(df.iloc[start : start + 10].to_string())
            start +=10
            print('\n')

            try:
                x = input('\nContinue printing?\n')

            except KeyboardInterrupt:

                print('\nError')
                return None

            if x != 'yes':

                break
            else:

                continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        try:
            restart = input('\nRestart program? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except KeyboardInterrup:
            print('\nError encountred')
            break


if __name__ == "__main__":
	main()
