# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     HeartBeats
# Author:      张正桃Anthony
# Datetime:    1/5/2022 5:35 PM
# Description：对应心跳feature文件
# -------------------------------------------------------------------------------------------------
from behave import *
import ast
from utils.send_requests import ReadyRequesting

sq = ReadyRequesting()


@Given("用例编号{caseID}和描述{description}")
def step_implement(context, caseID, description):
	context.case["caseID"] = caseID
	context.case["description"] = description
	pass


@When("接口信息: 接口名和请求方法{api}; api账号{api_kv}")
def step_implement(context, api, api_kv):
	context.case["api"] = ast.literal_eval(api)["接口名"]
	global request_method  # 为心跳上报请求做准备
	request_method = ast.literal_eval(api)["请求方法"]
	global head  # 为心跳上报请求做准备
	head = {"Content-Type": "application/json", "api_key": ast.literal_eval(api_kv)["api_key"],
	        "api_secret": ast.literal_eval(api_kv)["api_secret"]}
	pass


@Then("上报设备心跳: 请求参数{parameter}和预期值{expected}")
def step_implement(context, parameter, expected):
	# 接口url
	link = context.vars["bav_hp"] + context.vars["bav_link_heartbeat"]
	# 请求参数
	context.case["parameter"] = ast.literal_eval(parameter)
	context.case["expected"] = ast.literal_eval(expected)
	a = sq.requesting(link, request_method, head, context.case["parameter"])
	context.case["response"] = a.text
	try:
		assert a.json()["code"] == context.case["expected"]["code"]
		assert a.json()["msg"] == context.case["expected"]["msg"]
		context.case["judgement"] = "通过"
	except AssertionError:
		context.case["judgement"] = "失败"
	pass
