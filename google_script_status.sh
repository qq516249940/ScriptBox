#!/bin/bash

# 获取当前时间
current_time=$(date +"%H:%M:%S")

# 设置代理服务器地址和端口
your_proxy_address="127.0.0.1"
port="8889"
name="google"

# 使用 curl 访问 Google 并检查 HTTP 状态码
if curl -s -o /dev/null -w "%{http_code}" https://www.google.com --proxy http://$your_proxy_address:$port | grep 200 > /dev/null; then
    echo "$name Internet: Connected at $current_time"
else
    echo "$name Internet: Disconnected at $current_time"
fi
