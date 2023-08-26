# sqlalchemy-challenge
Before You Begin
Create a new repository for this project called sqlalchemy-challenge. Do not add this assignment to an existing repository.

Clone the new repository to your computer.

Inside your local Git repository, create a directory for this Challenge. Use a folder name that corresponds to the Challenge, such as SurfsUp.

Add your Jupyter notebook and app.py to this folder. They’ll contain the main scripts to run for analysis. Also add the Resources folder, which contains the data files you will be using for this challenge.

Push the changes to GitHub or GitLab.
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. 
The following sections outline the steps that you need to take to accomplish this task.
Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.

Use SQLAlchemy create_engine to connect to your sqlite database.

Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.

Link Python to the database by creating an SQLAlchemy session.

Important Don't forget to close out your session at the end of your notebook. Precipitation Analysis

Start by finding the most recent date in the data set.

Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query.

Select only the date and prcp values.

Load the query results into a Pandas DataFrame and set the index to the date column.

Sort the DataFrame values by date.

Plot the results using the DataFrame plot method.

Use Pandas to print the summary statistics for the precipitation data. Station Analysis

Design a query to calculate the total number of stations in the dataset.

Design a query to find the most active stations (i.e. which stations have the most rows?). o List the stations and observation counts in descending order. o Which station id has the highest number of 
observations? o Using the most active station id, calculate the lowest, highest, and average temperature. o Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.

Design a query to retrieve the last 12 months of temperature observation data (TOBS). o Filter by the station with the highest number of observations. o Query the last 12 months of temperature observation data for this station. o Plot the results as a histogram with bins=12.

Close out your session.

Step 2 - Climate App Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

Use Flask to create your routes. Routes
/ o Home page. o List all routes that are available.
/api/v1.0/precipitation o Convert the query results to a dictionary using date as the key and prcp as the value. o Return the JSON representation of your dictionary.
/api/v1.0/stations o Return a JSON list of stations from the dataset.
/api/v1.0/tobs o Query the dates and temperature observations of the most active station for the last year of data. o Return a JSON list of temperature observations (TOBS) for the previous year.
/api/v1.0/ and /api/v1.0// o Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range. o When given the start only, calculate 
TMIN, TAVG, and TMAX for all dates greater than and equal to the start date. o When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive. Hints
You will need to join the station and measurement tables for some of the queries.
Use Flask jsonify to convert your API data into a valid JSON response object.
