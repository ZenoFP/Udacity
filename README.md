# Bike Share Data Project Description

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, i used the data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.
I compared the system usage between three large cities: Chicago, New York City, and Washington, DC.
The Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

    Start Time (e.g., 2017-01-01 00:07:57)
    End Time (e.g., 2017-01-01 00:20:53)
    Trip Duration (in seconds - e.g., 776)
    Start Station (e.g., Broadway & Barry Ave)
    End Station (e.g., Sedgwick St & North Ave)
    User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

    Gender
    Birth Year

Data for the first 10 rides in the new_york_city.csv file

The original files are much larger and messier, these files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make my analysis and the evaluation of my Python skills more straightforward. In the Data Wrangling course that comes later in the Data Analyst Nanodegree program, i learned how to wrangle the dirtiest, messiest datasets.

# Statistics Computed

I learned about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. The code was written to provide the following information:

1- Popular times of travel (i.e., occurs most often in the start time)

    Most common month
    Most common day of week
    Most common hour of day

2- Popular stations and trip

    Most common start station
    Most common end station
    Most common trip from start to end (i.e., most frequent combination of start station and end station)

3- Trip duration

    Total travel time
    Average travel time

4- User info

    Counts of each user type
    Counts of each gender (only available for NYC and Chicago)
    Earliest, most recent, most common year of birth (only available for NYC and Chicago)

5- The Files

To answer these questions using Python, i wrote a Python script. To help guide my work in this project, a template with helper code and comments was provided in a bikeshare.py file, and i did my scripting in there also. I used the three city dataset files too:

    chicago.csv
    new_york_city.csv
    washington.csv
