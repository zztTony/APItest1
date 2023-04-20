# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     HealthCheck
# Author:      张正桃Anthony
# Datetime:    1/6/2022 5:24 PM
# Description：
# -------------------------------------------------------------------------------------------------
from behave import *
import ast
from utils.send_requests import ReadyRequesting
from utils.sqr import get_sqr  # 获取健康码码串

sq = ReadyRequesting()


@Given("用例编号{caseID}，用例描述{description}")
def step_implement(context, caseID, description):
	context.case["caseID"] = caseID
	context.case["description"] = description
	context.case["api"] = "健康核验"
	pass


@Then("api账号{api_kv}, 健康核验请求参数{parameter}和预期结果{expected}")
def step_implement(context, api_kv, parameter, expected):
	link = context.vars["bav_hp"] + context.vars["bav_link_healthCheck"]
	# 请求头
	head = {"Content-Type": "application/json"}
	head.update(ast.literal_eval(api_kv))
	context.case["parameter"] = ast.literal_eval(parameter)
	context.case["expected"] = ast.literal_eval(expected)
	if isinstance(context.case["parameter"].get("codeContent"), dict):
		context.case["parameter"]["codeContent"] = get_sqr(context.case["parameter"]["codeContent"])
	a = sq.requesting(link, "POST", head, context.case["parameter"])
	context.case["response"] = a.text
	try:
		assert a.json()["code"] == ast.literal_eval(expected)["code"]
		assert a.json()["msg"] == ast.literal_eval(expected)["msg"]
		if "riskAssessmentGrade" in ast.literal_eval(expected):
			assert a.json().get("data").get("riskAssessmentGrade") == ast.literal_eval(expected).get(
				"riskAssessmentGrade")
		context.case["judgement"] = "通过"
	except:
		context.case["judgement"] = "失败"
	pass
