# -----*----- coding:utf8 -----*----- #
# -----------------------------------------------------------------------------------
# ProjectName:   bdd2
# FileName:     pictures_decoding
# Author:      张正桃Anthony
# Datetime:    12/30/2021 6:07 PM
# Description：图片base64转码
# -------------------------------------------------------------------------------------------------
import base64
from utils.seek import locating


def decoding_picture(pic_path):
	"""
	图片base64解码
	:param pic_path: 要解码的图片的地址
	:return: 图片被解码成的字符串
	"""
	with open(pic_path, "rb") as p:
		base64_data = base64.b64encode(p.read())  # base64转码
		pic_code = base64_data.decode()  # 这是图片解码后的码串
		return pic_code


if __name__ == '__main__':
	where = locating() + r"\documents\kkk.jpg".replace("\\", "/")
	print(decoding_picture(where))
