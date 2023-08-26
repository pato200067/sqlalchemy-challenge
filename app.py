# Import Dependencies
import numpy as np
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify, Response
# Database set up
###################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)
app = Flask(__name__)
#session.query(Measurement.date).order_by(Measurement.date.desc()).first()
#year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#session.close()

######################################################
# Flask Setup

#################################################
# app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"welcome to hawaii climate analysis api:<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start_end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    #session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    """Return a list """
    # Query all passengers
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    session.close()

# Create a dictionary from the row data and append to a list 
    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
   

    """Return a list of stations """
    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Create a list of all_stations
    stations = list (np.ravel(results))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    # Create our session (link) from Python to the DB
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    """Return a list of stations """
    # Query all dates and temperature observations of the most active station for the last year of data
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    session.close()

    # Create a list of all_stations
    temps=list (np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    # Create our session (link) from Python to the DB
   

    """Return a list of agg data"""
    # Query TMIN, TAVG, and TMAX for all dates greater than and equal to the start date
    sel =[func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

  

    # Create a list of min, max, and avg
    if not end:
        start = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()

        session.close()

        temps = list(np.ravel(results))
        return jsonify(temps)
    start = dt.datetime.strptime(start, "%m%d%Y")
    end = dt.datetime.strptime(end, "%m%d%Y")
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    session.close()

    # Create a list of min, max, and avg
    temps=list(np.ravel(results))
        
    return jsonify(temps=temps)

if __name__ == '__main__':
    app.run(debug=True)
