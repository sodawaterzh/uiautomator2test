# -*- coding:utf-8 -*-
import time
from functools import wraps
import logging
import uiautomator2 as u2
import os,sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + r'\..')  # 返回脚本的路径
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log_test.log',
                    filemode='w')
logger = logging.getLogger()
def getImage(function):
	@wraps(function)
	def get_ErrImage(self,*args,**kwargs):
		try:
			result = function(self,*args,**kwargs)
		except Exception as msg:
			logging.info(" %s 用例执行异常" %
						 (function.__name__)
						 )
			timestr = time.strftime("%Y-%m-%d_%H_%M_%S")
			# screenshot(self.d, function.__name__+timestr, "getcrren/")#截图，并上传到项目getscreen目录下
			self.d.screenshot("getscreen/"+function.__name__+timestr+".png")
			raise msg #抛出异常，不抛出的话每次执行都是pass
		else:
			logging.info(" %s 脚本运行正常" %
						 (function.__name__)
						 )
			return result
	return get_ErrImage

# def screenshot(d,filename,path):
# 	filename_phone = "/sdcard/"+filename+'.png'
# 	output, exit_code = d.shell(["screencap",'-p',filename_phone])
# 	d.pull(filename_phone,sys.path[0]+'/getscreen/'+filename+'.png')
# 	output_del,exit_code_del = d.shell(["rm",'-f',filename_phone])

