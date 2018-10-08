# -*- coding:utf-8 -*-
import subprocess as sp
def getCode(phoneNum,type):
	'''
	测试服注册：type = 1
	  忘记密码：type = 2
	正式服注册：type = 3
	忘记密码：type = 4
	:param phoneNum:
	:param type:
	:return:
	'''
	if str(type) == "3" :#正式服注册

		(s, result) = sp.getstatusoutput(
			"ssh -l yangdongke 120.26.137.41 -p 5068 \"/home/view/scripts/verification-code.sh \" %s %s " % (
			phoneNum, "3"))
	elif str(type) == "4":#正式服忘记密码

		(s, result) = sp.getstatusoutput(
			"ssh -l yangdongke 120.26.137.41 -p 5068 \"/home/view/scripts/verification-code.sh \" %s %s " % (
				phoneNum, "2"))
	else:

		(s, result) = sp.getstatusoutput(
			"ssh -l yangdongke 120.26.37.196 -p 5068 \"/home/view/scripts/verification-code.sh \" %s %s " % (
			phoneNum, type))

	return result
def test():
	(s, result) = sp.getstatusoutput(
		"adb shell input tap 543 1475")
if __name__ == "__main__":
	a = getCode("13123815793",3)
	print(a)
	# for i in range(10000):
	# 	test()