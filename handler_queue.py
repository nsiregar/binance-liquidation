import logging
import time
from datetime import datetime

from redis import Redis
from rq.registry import StartedJobRegistry

from config import config

logger = logging.getLogger(__name__)

redis_conn = Redis.from_url(config.REDIS_URL)
job_registry = StartedJobRegistry(connection=redis_conn)

while True:
    print("start rq job monitor")
    started_jobs = job_registry.get_job_ids()
    if started_jobs:
        msg = f"{datetime.now()} list started jobs: {started_jobs}"
        print(msg)
    time.sleep(25)
