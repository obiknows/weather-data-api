import numpy as np
import time
import sys
import json

rate = np.random.exponential( 2 )

while True:
    print json.dumps({"t": time.time()})
    sys.stdout.flush()
    time.sleep( rate )
