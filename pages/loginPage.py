# -*- coding:utf-8 -*-



def userLoginButton(driver):
	'''账号登录按钮'''
	return driver(resourceId=
				  "com.circle.youyu:id/tv_id_login")
def userSignButton(driver):
	'''新注册按钮'''
	return driver(resourceId = "com.circle.youyu:id/tv_register")

def usernameText(driver):
	return driver(resourceId=
				  "com.circle.youyu:id/et_phone_num")

def passwordText(driver):
	'''账号登录密码输入框'''
	return driver(resourceId=
				  "com.circle.youyu:id/et_input_psw")

def loginButton(driver):
	'''登录界面的登录按钮'''
	return driver(text = "登录")

def forgetPassword(driver):
	'''登录界面，忘记密码'''
	return driver(resourceId=
				  "com.circle.youyu:id/tv_forget_psw")

def PhoneNumText(driver):
	return driver(resourceId=
				  "com.circle.youyu:id/et_phone_num")

def NextButton(driver):
	return driver(resourceId="com.circle.youyu:id/btn_next_step")

def codeText(driver):
	return driver(resourceId="com.circle.youyu:id/et_validate")

def setPasswordText(driver):
	return driver(resourceId="com.circle.youyu:id/et_psw")

def submitButton(driver):
	return driver(resourceId="com.circle.youyu:id/btn_next_step")


