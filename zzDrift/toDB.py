# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     toDB
# Author:      张正桃Anthony
# Datetime:    1/21/2022 1:38 PM
# Description：
# -------------------------------------------------------------------------------------------------
import pymongo


dbs = pymongo.MongoClient("mongodb://test:xxxxx@172.xxx.xxx.xxx:27017/test?authSource=aiot-test&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
the_db =dbs["aiot-test"]
my_coll =the_db["device_device"]
# if context.case["api1"]=="设备注册":
a = my_coll.count_documents({"nodeId": "0120100016c0aa04a00"})
if a:
	print(a, "有东西")
else:
	print(a, "没东西")
# print(the_db)
# print(a)
# print(my_coll)