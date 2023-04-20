# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     seek
# Author:      张正桃Anthony
# Datetime:    1/19/2022 3:49 PM
# Description：该模块用于获取项目文件路径
# -------------------------------------------------------------------------------------------------
import os


def locating():
	"""
	:return: 项目地址——脚本目录
	"""
	return os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")


if __name__ == '__main__':
	print(locating())
