# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd1
# FileName:     shijian
# Author:      张正桃Anthony
# Datetime:    11/30/2021 10:52 AM
# Description：
# -------------------------------------------------------------------------------------------------
import time
import datetime
import pandas as pd
import random
import os
from utils.seek import locating
import ast
import json

# a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(a)
# print(type(a))
#
# assert "a".upper() == "A"
# print("bOw".upper())
#
# fn = os.path.abspath(__file__)
# print(fn)
# fn = os.path.dirname(__file__)
# print(fn)
#
# a = "-1"
# b = int(a)
# print(b)
# print(type(b))
# print("=============================================")
# d = '{"deviceId": "0120100016c0aa04a00", "deviceType": "AIO_MACHINE", "uid": "", "current": 1, "size": None, "productId": "61b1beb3d256694905d12221"}'
# size = random.choice([10, 15, 20, 30, 50, 100])
# e= ast.literal_eval(d)
# e["size"]=size
# print(e)
# d1 = '{"code":200,"msg":"指令下发成功","time":1641292166396,"data":[{"taskCode":200,"taskMsg":"成功","taskId":"61d42186d93bdf084033c8f9","taskRequest":None}]}'
# d = "{'tag': '展示时长设置2秒', 'deviceId': '0120100016c0aa02a00', 'status': 'CREATED', 'current': 1, 'size': 100, 'taskId': ''}"
# print(ast.literal_eval(d1)["data"][0]["taskId"])
# print(["data"][0]["taskId"])


# head = {"Content-Type": "application/json"}
# tail = {"7": "是数字", "8": "也是数字"}
# a = head.update(tail)
# print(a)
# print(head)
# print(type({}))
# if isinstance({}, dict):
# 	print("没问题")

# if "":
# 	print("空")
# print("斗牛犬")
# the_time =time.strftime("%Y年%m月%d日%H时%M分%S秒", time.localtime())
# print(type(the_time))
# print(the_time)
# print("\\")
# ll = []
# ll.append(None)
# ll.append(None)
# print(ll)
# print(locating())
# ll = ["ss", "22", "t同意", 9]
# for i in ll:
# print(time.asctime())
# print(type(time.asctime()))


# ll = [[{"age": 2}, {"age": 3}],
#       [{"where": "北京", "when": "昨天", "who": "别人"}, {"where": "东京", "when": "今天", "who": "人家"}]]
#
# with pd.ExcelWriter(r"C:\Users\ASUS\Desktop\nnn.xlsx", mode="w") as wr:
# 	for i in ll:
# 		df = pd.DataFrame(i)
# 		time.sleep(1)  # 因程序会在1秒内完成这两个sheet的写入，所以为了防止sheet重名，就要等待1秒。
# 		df.to_excel(wr, sheet_name=time.strftime("%Y_%m_%d,%H-%M-%S"))

# print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)).replace("\\", "/"))
# print(os.path.dirname(os.path.abspath(__file__)))