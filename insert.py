#
# insert.py
#
# by - sam nnodim (son2105)
#
# adapted from: https://github.com/mikedewar/RealTimeStorytelling/blob/master/2/insert.py

# import some useful libs
import json
import sys
import redis

# Connect a redis database
conn = redis.Redis()

while True:
    # read a line from stdin
    line = sys.stdin.readline()

    # parse the data as a json obj.
    data = json.loads( line )
    distance = data["stormDist"]
    delta = data["delta"]

    # Add object to database w/ an expiration date
    # This is so that we can keep a window of measurements
    # For which to calculate rates
    conn.setex(distance, delta, 120)

    # Print the data to stdout so it can be 
    # resued in the pipeline
    print ( json.dumps({"stormDist":distance, "delta":delta}) )
    sys.stdout.flush()