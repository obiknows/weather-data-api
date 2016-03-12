:umbrella: weather-data-api :umbrella:
==========================================


This data stream acquired using the
[The Dark Sky Forecast API](https://developer.forecast.io/)
polls the API every minute to grab the distance of the nearest storm to Columbia University (rel. to [Butler Library](https://en.wikipedia.org/wiki/Butler_Library))  and stores that in a redis store. At the same time,
on every entry on the redis store, we calculate a moving average of the
distance of the storm and we send an alert via twitter, alerting us of whether a storm is moving closer or further


### Usage

1. Install numpy, [redis](http://redis.io/) and [birdy](https://github.com/inueni/birdy) 
2. In one tab start an instance of redis: 
		
		redis-server
3. In another tab run the command:

		./pipeline.sh
4. Observe the Twitter account: [@realtimetestin](https://twitter.com/realtimetestin)
5. Bask in the beauty of the notifications