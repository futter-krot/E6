from redis import Redis
from flask import jsonify, Flask, request
import os, logging

app = Flask(__name__)
REDIS_HOST = os.environ.get('REDIS_HOST')
redis_client = Redis(host=REDIS_HOST)
logger = logging.getLogger(__name__)

@app.route("/<number>", methods=['GET'])
def get_fibonacci_api(number):
    number = int(number)
    stored_value = redis_client.get(number)
    if stored_value:
        logger.info("For {} stored value is used".format(number))
        return jsonify({number: stored_value.decode()}), 200
    new_value = get_fibonacci(number)
    logger.info("For {} new value is calculated".format(number))
    redis_client.set(number, new_value)
    return jsonify({number: new_value}), 200

def get_fibonacci(number):
    if (number == 0) or (number == 1): 
        return number
    return get_fibonacci(number-1) + get_fibonacci(number-2)
