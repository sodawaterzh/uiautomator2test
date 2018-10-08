# -*- coding:utf-8 -*-
import subprocess as sp
from utils.adb.adbCommonds import addCommonds
def get_battery_info(info):
	'''	获取电池信息
	      AC powered: false 是否连接AC（电源）充电线
  		  USB powered: true 是否连接USB（PC或笔记本USB插口）充电
		  Wireless powered: false 是否使用了无线电源
		  Max charging current: 0
		  Max charging voltage: 0
		  Charge counter: 0
		  status: 5	电池状态，2为充电状态，其他为非充电状态
		  health: 2
		  present: true
		  level: 100 电量（%）
		  scale: 100 电量最大数值
		  voltage: 4388 当前电压（mV）
		  temperature: 340 电池温度，单位为0.1摄氏度
		  technology: Li-poly'''
	(code, results) = sp.getstatusoutput(addCommonds.adb_battery)
	c = results.split('\n')
	c.pop(0)
	battery = {}
	for item in c:
		list_battery = item.split(':')
		battery[list_battery[0].strip()] = list_battery[1].strip()
	return battery[info]
	# print(eval(b))
if __name__ == '__main__':
	# print(get_battery_info('temperature'))
	(code, results) = sp.getstatusoutput(addCommonds.adb_battery)
	print(results)