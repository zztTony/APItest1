# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     issueInstruction
# Author:      张正桃Anthony
# Datetime:    12/21/2021 5:19 PM
# Description：
# -------------------------------------------------------------------------------------------------
from behave import *
import time
import ast
from utils.pictures_decoding import decoding_picture
import random
from utils.seek import locating
from utils.send_requests import ReadyRequesting

sq = ReadyRequesting()


@Given("用例{caseID}描述{description}")
def step_implement(context, caseID, description):
	context.case["caseID"] = caseID
	context.case["description"] = description
	pass


@When("参数准备: 请求头")
def step_implement(context):
	global head_js
	head_js = {"api_key": context.vars["bav_api_key"], "api_secret": context.vars["bav_api_secret"],
	           "Content-Type": "application/json"}
	global head0
	head0 = {"api_key": context.vars["bav_api_key"], "api_secret": context.vars["bav_api_secret"]}
	pass


@Then("下发指令: 接口{api1}请求参数{parameter1}期望值{expected1}")
def step_implement(context, api1, parameter1, expected1):
	link = context.vars["bav_hp"] + context.vars["bav_link_instruction"]
	context.case["api1"] = ast.literal_eval(api1)["接口名"]
	context.case["para1"] = ast.literal_eval(parameter1)
	context.case["expected1"] = ast.literal_eval(expected1)
	# 判断要下发的指令中是否有人脸信息
	for i in context.case["para1"]:
		if "base64Img" in i["instruParams"]:
			# 再用例中,base64Img的值是图片路径, 所以要如下地获取图片码串
			i["instruParams"]["base64Img"] = decoding_picture((locating()+i["instruParams"]["base64Img"]).replace("\\", "/"))
	a = sq.requesting(link, ast.literal_eval(api1)["请求方法"], head_js, context.case["para1"])
	context.case["response1"] = a.text  # 指令下发的返回值也要写入excel表
	context.taskId = []
	for i in a.json()["data"]:
		if i["taskCode"] == 200:
			context.taskId.append(i["taskId"])
	try:
		assert a.json()["code"] == ast.literal_eval(expected1)["code"]
		assert a.json()["msg"] == ast.literal_eval(expected1)["msg"]
		assert len(context.case["para1"]) == len(context.taskId)  # 判断命令是否都下发成功了
		context.case["judgement1"] = "通过"
	except AssertionError:
		context.case["judgement1"] = "失败"
	pass


@Then("心跳接收: 接口{api2}请求参数{parameter2}期望值{expected2}")
def step_implement(context, api2, parameter2, expected2):
	link = context.vars["bav_hp"] + context.vars["bav_link_heartbeat"]
	context.case["api2"] = ast.literal_eval(api2)["接口名"]
	context.case["para2"] = ast.literal_eval(parameter2)
	context.case["expected2"]=ast.literal_eval(expected2)
	a = sq.requesting(link, ast.literal_eval(api2)["请求方法"], head_js, context.case["para2"])
	context.case["response2"] = a.text  # 心跳的返回值要写入excel
	try:
		assert a.json()["code"] == ast.literal_eval(expected2)["code"]
		assert a.json()["msg"] == ast.literal_eval(expected2)["msg"]
		if len(a.json()["data"]):
			context.taskId2 = []
			for i in a.json()["data"]:
				context.taskId2.append(i["taskId"])
			assert context.taskId == context.taskId2
		context.case["judgement2"] = "通过"
	except AssertionError:
		context.case["judgement2"] = "失败"
	pass


@Then("任务执行: 接口{api3}任务反馈{feedback}期望值{expected3}")
def step_implement(context, api3, feedback, expected3):
	link = context.vars["bav_hp"] + context.vars["bav_link_taskTrace"]
	context.case["api3"] = ast.literal_eval(api3)["接口名"]
	context.case["para3"] = []
	context.case["response3"] = []
	context.case["expected3"] = ast.literal_eval(expected3)
	context.case["judgement3"] = []
	for i in context.taskId:
		context.case["judgement3"].append(None)
		sv_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		# 任务跟踪的请求参数
		para = {"taskId": i, "status": feedback, "time": sv_time, "message": "任务{}".format(feedback),
		        "data": {"时间": "{}".format(sv_time)}, "errorData": {}}
		context.case["para3"].append(para)
		a = sq.requesting(link, ast.literal_eval(api3)["请求方法"], head_js, para)
		context.case["response3"].append(a.json())
		try:
			assert a.json()["code"] == ast.literal_eval(expected3)["code"]
			assert a.json()["msg"] == ast.literal_eval(expected3)["msg"]
			context.case["judgement3"][context.taskId.index(i)] = "通过"
		except AssertionError:
			context.case["judgement3"][context.taskId.index(i)] = "失败"
	pass


@Then("指令查询: 接口{api4}请求参数{parameter4}期望值{expected4}")
def step_implement(context, api4, parameter4, expected4):
	link = context.vars["bav_hp"] + context.vars["bav_link_searchInstruction"]
	context.case["api4"] = ast.literal_eval(api4)["接口名"]
	context.case["para4"] = []
	context.case["expected4"] = ast.literal_eval(expected4)
	context.case["response4"] = []
	context.case["judgement4"] = []
	for i in context.taskId:  # 期望值未实现在多指令情况下的一一对应!
		context.case["judgement4"].append(None)
		size = random.choice([10, 15, 20, 30, 50, 100])
		para = {"tag": context.case["para1"][context.taskId.index(i)]["tag"],
		        "deviceId": context.case["para2"]["deviceId"],
		        "status": ast.literal_eval(parameter4)["status"], "current": ast.literal_eval(parameter4)["current"],
		        "size": size, "taskId": i}
		context.case["para4"].append(para)
		a = sq.requesting(link, ast.literal_eval(api4)["请求方法"], head0, para, content_type=0)
		context.case["response4"].append(a.json())
		try:
			assert a.json()["code"] == ast.literal_eval(expected4)["code"]
			assert a.json()["msg"] == ast.literal_eval(expected4)["msg"]
			assert a.json()["data"]["totalCount"] == ast.literal_eval(expected4)["total"]
			context.case["judgement4"][context.taskId.index(i)] = "通过"
		except AssertionError:
			context.case["judgement4"][context.taskId.index(i)] = "失败"
	pass
