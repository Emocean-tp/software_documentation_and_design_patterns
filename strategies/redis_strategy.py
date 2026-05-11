from strategies.output_strategy import OutputStrategy
import redis
import json

class RedisStrategy(OutputStrategy):

    def __init__(self, config):
        self.redis_client = redis.Redis(
            host=config["host"],
            port=config["port"],
            db=config["db"],
            decode_responses=True
        )

    def output(self, data):
        print("Saving data to Redis...")

        for i, row in enumerate(data):
            key = f"user:{i}"
            self.redis_client.set(key, json.dumps(row))

        print(f"Saved {len(data)} records to Redis")