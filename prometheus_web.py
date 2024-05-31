from prometheus_client import start_http_server, Summary, Counter, Gauge
import random
import time

# 创建Prometheus指标
RESPONSE_TIME = Summary('response_time', 'Response time of the service')
ERROR_RATE = Counter('error_rate', 'Number of errors')
AVAILABILITY = Gauge('availability', 'Service availability')

class SLA:
    def __init__(self, availability_target, response_time_target, error_rate_target):
        self.availability_target = availability_target
        self.response_time_target = response_time_target
        self.error_rate_target = error_rate_target

    @RESPONSE_TIME.time()
    def log_data(self, uptime, response_time, errors, total_requests):
        AVAILABILITY.set(uptime)
        RESPONSE_TIME.observe(response_time)
        ERROR_RATE.inc(errors)

    def evaluate_sla(self):
        # 这里可以添加评估SLA的逻辑
        pass

# 示例用法
sla = SLA(availability_target=0.99, response_time_target=0.5, error_rate_target=0.01)

# 启动一个HTTP服务器以暴露指标
start_http_server(8000)

# 模拟记录数据
while True:
    uptime = random.choice([1, 1, 1, 0])  # 75% uptime
    response_time = random.uniform(0.2, 0.6)  # 随机响应时间在0.2到0.6秒之间
    errors = random.choice([0, 0, 0, 1])  # 25%的错误率
    total_requests = 100
    sla.log_data(uptime, response_time, errors, total_requests)
    time.sleep(10)
