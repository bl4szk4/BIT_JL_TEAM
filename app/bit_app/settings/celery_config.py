from bit_app.settings import Redis

broker_url = f"redis://:{Redis.REDIS_PASSWORD}@redis:6379/0"
result_backend = f"redis://:{Redis.REDIS_PASSWORD}@redis:6379/1"
task_soft_time_limit = 5 * 60
task_time_limit = 10 * 60
worker_prefetch_multiplier = 2
