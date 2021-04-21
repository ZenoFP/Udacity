import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while (True):
        city = input("Enter a city between Chicago, New York City or Washington")
        if city.lower() in CITY_DATA.keys():
            break
        continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while (True):
        month = input("Enter a valid month")
        month = month.lower()
        if month in MONTHS or month == 'all':
            break
        continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (True):
       day = input("Enter a valid day of the week")
       day = day.lower()
       if day in DAYS or day == 'all':
           break
       continue

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
    df = pd.read_csv(city)

    # convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # month and day of week from Start Time and create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # BY ME: display the most common month
    print('The most common month is ', df['month'].mode()[0], '\n')

    # BY ME: display the most common day of week
    print('The most common day of the week is ', df['day_of_week'].mode()[0], '\n')

    # BY ME: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # BY ME: display most commonly used start station
    print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")

    # BY ME: display most commonly used end station
    print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")

    # BY ME: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # BY ME: display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # BY ME: display mean travel time
    print("The total mean time is", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # BY ME: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")

    # BY ME: Display counts of gender
    try:
        aux = df['Gender']

    except KeyError:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # BY ME: Display earliest, most recent, and most common year of birth
    mryob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
    eyob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
    mcyob = df['Birth Year'].mode()[0]
    print("The earliest year of birth is ", eyob, "\n")
    print("The most recent year of birth is ", mryob, "\n")
    print("The most common year of birth is ", mcyob, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    counter = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            counter += 5
        else:
            break


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
            break


if __name__ == "__main__":
	main()
