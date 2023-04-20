# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     DataDivision
# Author:      张正桃Anthony
# Datetime:    1/4/2022 10:35 AM
# Description：数据分离
# -------------------------------------------------------------------------------------------------
from behave import *
import ast
import time
import random
from utils.send_requests import ReadyRequesting
from utils.pictures_decoding import decoding_picture

sq = ReadyRequesting()


@Given("用例编号{caseID}和用例描述{description}")
def step_implement(context, caseID, description):
	context.case["caseID"] = caseID
	context.case["description"] = description
	pass


@When("数据制造: 接口{api1}, api账号{api_cA}, 请求参数{parameter1}, 期望值{expected1}")
def step_implement(context, api1, api_cA, parameter1, expected1):
	context.case["api1"] = ast.literal_eval(api1)["接口名"]
	link = context.vars["bav_hp"] + ast.literal_eval(api1)["url"]
	# 下面处理原api账号
	global api_k0
	api_k0 = ast.literal_eval(api_cA)["api_key"]
	global api_v0
	api_v0 = ast.literal_eval(api_cA)["api_secret"]
	head = {"Content-Type": "application/json", "api_key": api_k0, "api_secret": api_v0}
	context.case["parameter1"] = ast.literal_eval(parameter1)
	context.case["expected1"] = ast.literal_eval(expected1)
	if "time" in context.case["parameter1"]:
		global startTime  # 方便查询的时候用
		startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		context.case["parameter1"]["time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		time.sleep(1)
		global endTime  # 方便查询的时候用
		endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	if "base64Img" in context.case["parameter1"]:
		context.case["parameter1"]["base64Img"] = decoding_picture(context.case["parameter1"]["base64Img"])
	a = sq.requesting(link, ast.literal_eval(api1)["请求方法"], head, context.case["parameter1"])
	context.case["response1"] = a.text
	context.taskId = None
	if isinstance(context.case["parameter1"], list):
		context.taskId = a.json()["data"][0]["taskId"]
	try:
		assert a.json()["code"] == ast.literal_eval(expected1)["code"]
		assert a.json()["msg"] == ast.literal_eval(expected1)["msg"]
		context.case["judgement1"] = "通过"
	except AssertionError:
		context.case["judgement1"] = "失败"
	pass


@Then("数据查询: 接口{api2}, 本api账号, 请求参数{parameter2}, 预期{expected2}")
def step_implement(context, api2, parameter2, expected2):
	context.case["api2"] = ast.literal_eval(api2)["接口名"]
	context.link_search = ast.literal_eval(api2)["url"]
	link = context.vars["bav_hp"] + context.link_search
	head = {"api_key": api_k0, "api_secret": api_v0}
	global request_method  # 查询接口的请求方法全局化, 方便不同的api账号下的相同请求
	request_method = ast.literal_eval(api2)["请求方法"]
	# 给请求参数中的size赋值
	global dic  # 将查询参数全局化, 方便不同的api账号下的相同请求
	dic = ast.literal_eval(parameter2)
	if "startTime" in dic:
		dic["startTime"] = startTime
		dic["endTime"] = endTime
	if "taskId" in dic:
		dic["taskId"] = context.taskId
	dic["size"] = random.choice([10, 15, 20, 30, 50, 100])
	context.case["parameter2"] = dic
	a = sq.requesting(link, request_method, head, context.case["parameter2"], content_type=0)
	context.case["response2"] = a.text
	try:
		assert a.json()["code"] == ast.literal_eval(expected2)["code"]
		assert a.json()["msg"] == ast.literal_eval(expected2)["msg"]
		assert a.json()["data"]["totalCount"] == ast.literal_eval(expected2)["totalCount"]
		context.case["judgement2"] = "通过"
	except AssertionError:
		context.case["judgement2"] = "失败"
	pass


@Then("同空间异api账号{api_cB}查询: 参数同上, 预期{expected3}")
def step_implement(context, api_cB, expected3):
	head = {"api_key": ast.literal_eval(api_cB)["api_key"], "api_secret": ast.literal_eval(api_cB)["api_secret"]}
	link = context.vars["bav_hp"] + context.link_search
	context.case["parameter3_同空间异api账号查询"] = dic
	context.case["expected3"] = ast.literal_eval(expected3)
	context.case["parameter3_同空间异api账号查询"]["size"] = random.choice([10, 15, 20, 30, 50, 100])
	a = sq.requesting(link, request_method, head, context.case["parameter3_同空间异api账号查询"], content_type=0)
	context.case["response3"] = a.text
	try:
		assert a.json()["code"] == ast.literal_eval(expected3)["code"]
		assert a.json()["msg"] == ast.literal_eval(expected3)["msg"]
		assert a.json()["data"]["totalCount"] == ast.literal_eval(expected3)["totalCount"]
		context.case["judgement3"] = "通过"
	except AssertionError:
		context.case["judgement3"] = "失败"
	pass


@Then("同租户异空间的api账号{api_cC}查询: 参数同上, 预期{expected4}")
def step_implement(context, api_cC, expected4):
	head = {"api_key": ast.literal_eval(api_cC)["api_key"], "api_secret": ast.literal_eval(api_cC)["api_secret"]}
	link = context.vars["bav_hp"] + context.link_search
	context.case["parameter4_同租户异空间api账号查询"] = dic
	context.case["expected4"] = ast.literal_eval(expected4)
	context.case["parameter4_同租户异空间api账号查询"]["size"] = random.choice([10, 15, 20, 30, 50, 100])
	a = sq.requesting(link, request_method, head, context.case["parameter4_同租户异空间api账号查询"], content_type=0)
	context.case["response4"] = a.text
	try:
		assert a.json()["code"] == context.case["expected4"]["code"]
		assert a.json()["msg"] == context.case["expected4"]["msg"]
		assert a.json()["data"]["totalCount"] == context.case["expected4"]["totalCount"]
		context.case["judgement4"] = "通过"
	except AssertionError:
		context.case["judgement4"] = "失败"
	pass


@Then("异租户的api账号{api_cD}查询: 参数同上, 预期{expected5}")
def step_implement(context, api_cD, expected5):
	head = {"api_key": ast.literal_eval(api_cD)["api_key"], "api_secret": ast.literal_eval(api_cD)["api_secret"]}
	link = context.vars["bav_hp"] + context.link_search
	context.case["parameter5_异租户api账号查询"] = dic
	context.case["parameter5_异租户api账号查询"]["size"] = random.choice([10, 15, 20, 30, 50, 100])
	context.case["expected5"] = ast.literal_eval(expected5)
	a = sq.requesting(link, request_method, head, context.case["parameter5_异租户api账号查询"], content_type=0)
	context.case["response5"] = a.text
	try:
		assert a.json()["code"] == context.case["expected5"]["code"]
		assert a.json()["msg"] == context.case["expected5"]["msg"]
		assert a.json()["data"]["totalCount"] == context.case["expected5"]["totalCount"]
		context.case["judgement5"] = "通过"
	except AssertionError:
		context.case["judgement5"] = "失败"
	pass
