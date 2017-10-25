#coding: utf-8
import socket

#aishowcompany.com 测试用例配置文件
#metinfo 5.3.12

HOST = "test.ai.moresec.cn"
PORT = 80

API_IP="222.186.57.204"
API_PORT= 8009

# 测试邮件发送功能case
EMAIL_ADDR='feihongbo1234@163.com'
EMAIL_PASSWD='feihongbo123'

#导入资产
domain_asset = ["aishowcompany.com"]
ip_asset = ["180.97.33.30-.18097.33.40", "192.168.199.145"]
url_asset = ["http://192.168.1.86/"]    #第一个url资产会添加高级监控

local_ip = socket.gethostbyname(socket.gethostname())

#网站可用性监控
alive_monitor_data = [
    {
        "target": "aishowcompany.com",
        "period": 1,
        "resp_time": 30
    },
    {
        "target": "www.yahoo.com",
        "period": 5,
        "resp_time": 110
    }
]
