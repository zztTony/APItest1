# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd1
# FileName:     drift
# Author:      张正桃Anthony
# Datetime:    11/29/2021 11:14 AM
# Description：
# -------------------------------------------------------------------------------------------------
# import ast
# from utils.send_requests import ReadyRequesting

"""
issue = requests.request(url="http://aiot.xxxxxx.com.cn:xxxxxx/aiot-device/v1/mac/api/kas/find-tasks-status",
                         method="GET",
                         headers={"api_key": "ugp1zdxxxxht16a", "api_secret": "0eb9trxxxxxrokm4obstd7s"},
                         params={"tag": "tagr", "deviceId": "0120100016c0aa01a00", "status": "", "current": "1",
                                 "size": "40"})
print(issue.text)
b = issue.json()["data"]["totalCount"]
print(b, type(b))
"""
# beat = requests.request(url="http://aiot.keydom.com.cn:30001/aiot-device/v1/mac/api/kas/device-heartbeat",
#                         method="POST",
#                         headers={"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s",
#                                  "Content-Type": "application/json"}, json={"deviceId": "0120100016c0aa01a00"})
# print(beat.text)


# aa = {"code": 200, "msg": "设备心跳上报成功", "time": 1638416194474,
#       "data": [{"taskId": "61a8386ad70fe770534814fd", "instruction": "3001", "instruParams": {}}]}
#
# # a = aa["data"][0]["taskId"]
# # print(a)
#
# s = ReadyRequesting()
# sq = s.requesting("http://172.16.100.70:10001/aiot-device/v1/mac/api/kas/find-tasks-status", "GET",
#                   {"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s"},
#                   {"tag": "tag_结果展示时长", "deviceId": "0120100016c0aa01a00", "status": "COMPLETED", "current": 1,
#                    "size": 10,
#                    "taskId": "61cbbfabd93bdf084033c8bd"}, content_type=0)
# print(type(sq.text))


a = '[{"n": "q", "1": "2", "9": "3"}, {"qq": "q2", "11": "12"}]'

# print(ast.literal_eval(a))
# print(type(ast.literal_eval(a)))
# print(type(ast.literal_eval(a)[0]))
#
#
# b = [1, 2, 4, 5, "i"]
# for i in b:
# 	print(b.index(i))

b = [{"operationType": "delete", "personId": "511028199603080010", "personName": "张正涛", "uid": "AA3E34F7",
      "cardType": "CPU", "base64Img": r"C:\Users\ASUS\Desktop\kkk.jpg", "format": "jpg", "type": "ADMIN"}]
for i in b:
    if "base64Img" in i:
        i["base64Img"] = "已经换了"

print(b)
