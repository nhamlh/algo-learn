# My venture into common algorithms implementation

## Leaky bucket
"The leaky bucket is an algorithm based on an analogy of how a bucket with a constant leak will overflow if either the average rate at which water is poured in exceeds the rate at which the bucket leaks or if more water than the capacity of the bucket is poured in all at once." - Wikipedia.

### Demo
Demo application is a small web app which use leaky bucket as a rate limitter. It allows users to burst to 5 requests at a time, then throttled to 1 requests per 20 seconds (5 requests per minute).

To run the demo app, install flask:

``` sh
pip3 install flask
```

Run the demo application:
``` sh
python3 leaky_bucket_example.py
```

The demo app will be listening on port 5000. Using curl to get some result:

``` sh
curl -v localhost:5000
```

throttled requests will get response with status code 429 
