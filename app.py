import redis
from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def home():
    visit_count = redis_client.get('visit_count')
    if visit_count is None:
        redis_client.set('visit_count', 1)
        visit_count = 1
    else:
        redis_client.incr('visit_count')
        visit_count=int(visit_count)

    app.logger.info(f"Home route accessed, visit count: {visit_count}")
    return f"Hello, Devops Engineer! This page has been visited {visit_count} times. Also LenDenClub is India's largest Peer-to-Peer (P2P) lending platform."

@app.route('/reset')
def reset_count():
    redis_client.set('visit_count', 0)
    app.logger.info("Visit count reset to 0")
    return "Visit count has been reset to 0."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
