import os
import redis

redis_db = redis.StrictRedis(
    host="redis", port="6379", db=1,
    charset="utf-8", decode_responses=True
)
