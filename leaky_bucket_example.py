from flask import Flask, Response
from leaky_bucket import LeakyBucket

app = Flask(__name__)

rate_limitter = LeakyBucket(capacity=5, leak_rate=20) # Can burst to 5 requests, accrue 1 request every 20s

@app.route("/")
def hello_world():
    if not rate_limitter.can_add():
        return "", 429

    return "<p>Hello, World!</p>", 200

if __name__ == '__main__':
    app.run()
