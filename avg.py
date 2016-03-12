#
# avg.py
#
# by - sam nnodim (son2105)
#
# adapted by: https://github.com/mikedewar/RealTimeStorytelling/blob/master/2/avg.py

# import libraries
import redis
import json
import time
import sys

# Connect to the instatce of the redis database
conn = redis.Redis()

while True:
    # get the keys from the redis database
    keys = conn.keys()

    if len( keys ) == 0:
        continue

    values = conn.mget( keys )

    try:
        deltas =[float(v) for v in values]
    except TypeError:
        print keys
        continue

    if len( deltas ):
        rate =  sum( deltas ) / float( len( deltas ) )
    else:
        rate = 0

    # Rate notifications
    # If the rate is
    #   less than -5   - "storm's a coming"
    #   greater than 5 - "clear skies ahead"


    print ( json.dumps({"rate":rate}) )
    sys.stdout.flush()

    time.sleep( 5 )