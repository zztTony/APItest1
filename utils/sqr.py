# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     sqr
# Author:      张正桃Anthony
# Datetime:    1/6/2022 5:27 PM
# Description：获取测试健康码工具
# -------------------------------------------------------------------------------------------------
import requests


def get_sqr(color):
	"""
	获取测试健康码
	:param color: 获取健康码的请求参数
	:return: 健康码串
	"""
	link = "http://172.16.100.70:10001/aiot-device/hea-device/get-health-code"
	send = requests.request(url=link, method="post", json=color)
	line = send.json()["data"]["data"]["code_content"]  # 健康码码串
	return line


if __name__ == "__main__":
	a = {"certificate_type": "10", "certificate_id": "xxxxxxxxxxxxx", "name": "xxxxxx"}
	print(get_sqr(a))
