# -*- coding:utf-8 -*-
import subprocess as sp
class addCommonds(object):
	#连接设备
	adb_devices= "adb devices"
	#获取当前运行与手机前端的应用名
	adb_getPackage = "adb shell dumpsys window windows | grep \"mCurrentFocus\""
	#采集电池信息
	adb_battery = "adb shell dumpsys battery "
