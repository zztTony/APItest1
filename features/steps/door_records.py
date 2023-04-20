# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     door_records
# Author:      张正桃Anthony
# Datetime:    1/11/2022 3:17 PM
# Description：开门记录
# -------------------------------------------------------------------------------------------------
from behave import *
import ast
import time
from utils.seek import locating
from utils.send_requests import ReadyRequesting
from utils.pictures_decoding import decoding_picture

sq = ReadyRequesting()


@Given("用例编号{caseID}; 用例描述{description}")
def step_implement(context, caseID, description):
	context.case["caseID"] = caseID
	context.case["description"] = description
	global start_time  # 用于开门记录查询的开始时间
	start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	pass


@When("上报开门记录: 请求参数{parameter1}, 预期结果{expected1}")
def step_implement(context, parameter1, expected1):
	head = context.vars["head0"]
	head.update(context.vars["bav_apiAccount"])
	link = context.vars["bav_hp"] + context.vars["bav_link_doorRecords"]
	context.case["api1"] = "上报开门记录"
	context.case["parameter1"] = ast.literal_eval(parameter1)
	context.case["parameter1"]["time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	if "base64Img" in context.case["parameter1"]:  # 判断base64Img的值是不是""---空字符串
		if context.case["parameter1"]["base64Img"]:
			context.case["parameter1"]["base64Img"] = decoding_picture((locating()+context.case["parameter1"]["base64Img"]).replace("\\", "/"))
	context.case["expected1"] = ast.literal_eval(expected1)
	a = sq.requesting(link, "POST", head, context.case["parameter1"])
	context.case["response1"] = a.text
	# 开始断言
	try:
		assert a.json()["code"] == context.case["expected1"]["code"]
		assert a.json()["msg"] == context.case["expected1"]["msg"]
		context.case["judgement1"] = "通过"
	except AssertionError:
		context.case["judgement1"] = "失败"
	pass


@Then("查询开门记录: 请求参数{parameter2}, 预期结果{expected2}")
def step_implement(context, parameter2, expected2):
	link = context.vars["bav_hp"] + context.vars["bav_link_searchRecords"]
	head = context.vars["bav_apiAccount"]
	context.case["api2"] = "查询开门记录"
	context.case["parameter2"] = ast.literal_eval(parameter2)
	time.sleep(1)
	end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 查询开门记录参数的结束时间
	context.case["parameter2"]["startTime"] = start_time
	context.case["parameter2"]["endTime"] = end_time
	context.case["expected2"] = ast.literal_eval(expected2)
	a = sq.requesting(link, "get", head, context.case["parameter2"], content_type=0)
	context.case["response2"] = a.text
	try:
		assert a.json()["code"] == context.case["expected2"]["code"]
		assert a.json()["msg"] == context.case["expected2"]["msg"]
		assert a.json()["data"]["totalCount"] == context.case["expected2"]["totalCount"]
		context.case["judgement2"] = "通过"
	except AssertionError:
		context.case["judgement2"] = "失败"
	pass
