#
# diff.py
#
# by - sam nnodim (son2105)
#
# adapted from: https://github.com/mikedewar/RealTimeStorytelling/blob/master/2/diff.py

# import some more very useful libs
import json
import sys

# intialize a var. last for delta comparisons
last = 0

while True:
    # read a line of input being piped in from stdin
    line = sys.stdin.readline()

    # convert the line to usable JSON data
    # and get the pressure measurement
    data = json.loads( line )

    # Check the first edge case if we are
    # reading in data for the first time
    if last == 0:
        last = data["stormDistance"]
        continue

    # Create a var delta that tracks the time between
    # 2 pressure points taken from the data
    delta = data["stormDistance"] - last
    print ( json.dumps({"delta":delta, "stormDist":data["stormDistance"]}) )
    sys.stdout.flush()

    # Set last equal to the current measurement and start again
    last = data["stormDistance"]

