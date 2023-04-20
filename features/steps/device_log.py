# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     device_log
# Author:      张正桃Anthony
# Datetime:    1/14/2022 4:13 PM
# Description：对应device_log.feature
# -------------------------------------------------------------------------------------------------
from behave import *
import ast
import time
from utils.send_requests import ReadyRequesting

sq = ReadyRequesting()


@Given("测试用例编号{caseID}和用例描述{description}")
def step_implement(context, caseID, description):
	context.case["caseID"] = caseID
	context.case["description"] = description
	context.case["api"] = "设备日志上报"
	pass


@Then("请求参数{parameter}和预期结果{expected}")
def step_implement(context, parameter, expected):
	link = context.vars["bav_hp"] + context.vars["bav_link_deviceLog"]
	head = context.vars["head0"]
	head.update(context.vars["bav_apiAccount"])
	context.case["parameter"] = ast.literal_eval(parameter)
	context.case["parameter"]["time"] = time.strftime(context.case["parameter"]["time"], time.localtime())
	context.case["expected"] = ast.literal_eval(expected)
	a = sq.requesting(link, "post", head, context.case["parameter"])
	context.case["response"] = a.text
	try:
		assert a.json()["code"] == context.case["expected"]["code"]
		assert a.json()["msg"] == context.case["expected"]["msg"]
		context.case["judgement"] = "通过"
	except AssertionError:
		context.case["judgement"] = "失败"
	pass
