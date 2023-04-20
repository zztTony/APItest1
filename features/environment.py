# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd1
# FileName:     environment
# Author:      张正桃Anthony
# Datetime:    12/16/2021 10:56 AM
# Description：
# -------------------------------------------------------------------------------------------------
import pandas as pd
# from pandas import ExcelWriter
from utils.seek import locating
import pymongo
import time


def before_all(context):
    context.vars = {}
    context.vars["bav_api_key"] = "ugp1zdjvhfsht16a"
    context.vars["bav_api_secret"] = "0eb9trdq29yj8q7ruc0nrokm4obstd7s"
    context.vars["head0"] = {"Content-Type": "application/json"}
    # 主要的api账号
    context.vars["bav_apiAccount"] = {"api_key": "ugp1zdjvhfsht16a", "api_secret": "0eb9trdq29yj8q7ruc0nrokm4obstd7s"}
    context.vars["bav_hp"] = "http://172.16.100.70:10001"
    context.vars["bav_link_heartbeat"] = "/aiot-device/v1/mac/api/kas/device-heartbeat"
    context.vars["bav_link_instruction"] = "/aiot-device/v1/mac/api/kas/dispatch-tasks"
    context.vars["bav_link_taskTrace"] = "/aiot-device/v1/mac/api/kas/task-tracking"
    context.vars["bav_link_searchInstruction"] = "/aiot-device/v1/mac/api/kas/find-tasks-status"
    context.vars["bav_link_deviceRegister"] = "/aiot-device/v1/mac/api/aes/device-register"
    context.vars["bav_link_searchDevice"] = "/aiot-device/v1/mac/api/kas/device-list"
    context.vars["bav_link_healthCheck"] = "/aiot-paas/v1/healthcode/api/kas/verify-health-status"
    context.vars["bav_link_doorRecords"] = "/aiot-paas/v1/door/api/kas/access-records"
    context.vars["bav_link_searchRecords"] = "/aiot-paas/v1/door/api/kas/sync-access-records"
    context.vars["bav_link_deviceLog"] = "/aiot-device/v1/mac/api/kas/device-logs"
    # 下面这个变量放所有用例
    context.file_name = r"{}\results\outcomes{}.xlsx".format(locating(),
                                                             time.strftime("%Y年%m月%d日_%H时%M分%S秒",
                                                                           time.localtime())).replace("\\", "/")
    context.sheets = []
    context.sheet_names = []
    pass


def after_all(context):
    with pd.ExcelWriter(context.file_name, mode="w") as wr:
        for i in context.sheets:
            df = pd.DataFrame(i)
            df.to_excel(wr, sheet_name=context.sheet_names[context.sheets.index(i)])
    pass


def before_feature(context, feature):
    context.cases = []
    pass


def after_feature(context, feature):
    # 将所有用例写入excel表
    sheet_name = time.strftime("%Y年%m月%d日%H时%M分%S秒_", time.localtime()) + context.cases[0].get("caseID")
    # df = pd.DataFrame(context.cases)
    # df.to_excel(context.file_name, sheet_name=, m)
    context.sheets.append(context.cases)
    context.sheet_names.append(sheet_name)
    pass


def before_scenario(context, scenario):
    # 下面这个变量放每个用例
    context.case = {}
    pass


def after_scenario(context, scenario):
    # 将每个用例放到所有用例的列表中
    context.cases.append(context.case)
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    if tag == "设备注册和数据分离":
        dbs = pymongo.MongoClient(
            "mongodb://test:test@172.16.100.70:27017/test?authSource=aiot-test&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
        the_db = dbs["aiot-test"]
        my_coll = the_db["device_device"]
        if context.case["api1"] == "设备注册":
            if my_coll.count_documents({"nodeId": context.case["parameter1"]["deviceId"]}):
                my_coll.delete_one({"nodeId": context.case["parameter1"]["deviceId"]})
    pass
