# -*- coding:utf-8 -*-
#弹出框
dialog_sureButton_text = "确定"
#
mineButton_text = "我的"
def dialog_sureButton(driver):
	return driver(text = "确定")
def mineButton(driver):
	return driver(text="我的")
#首页闪屏弹窗关闭
def screenClose(driver):
	return driver(resourceId="com.circle.youyu:id/iv_dialog_ad_close")
def find(driver):
	return driver(text="发现")