from flask import Flask
import config
# from redis import Redis
# from pymongo import MongoClient

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)
# client = MongoClient(
#     'mongo',
#     27017
# )

# test_db = client.test

@app.route('/')
def hello():
    # count = redis.incr('hits')
    # data = {"count": count}
    # result = test_db.count.insert_one(data)
    # return 'Hello Spence! I have been seen {} times.\n'.format(count)
    return 'Hello {}'.format(config.CONFIG_DICT['NAME'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
