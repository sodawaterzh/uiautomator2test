# -*- coding:utf-8 -*-
import uiautomator2 as u2
import unittest
import uiautomator2.ext.htmlreport as htmlreport
import time
from pages import indexPage
from pages import MinePage
from pages import loginPage
from utils.ScreenShot import getImage
from utils.getCode import getCode
from utils.handles import handl
from events import MinePageEvs
from utils import Config
class test01(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# cls.u= u2.connect('192.168.1.40')
		cls.u = u2.connect_usb("5LM0216524006922")
		# cls.u.app_install("/Users/zh/Downloads/app-baidu-release(7).apk")
		cls.u.healthcheck()
		hrp = htmlreport.HTMLReport(cls.u,"report")
		hrp.patch_click()
		# cls.u.disable_popups(True)#允许自动处理弹出框
		cls.u.make_toast("测试开始",3)
		# cls.d = cls.u.session("com.circle.youyu")  # 只在开始时restart app
	@classmethod
	def tearDownClass(cls):
		cls.u.make_toast("测试结束", 3)
		cls.u.app_stop_all()

	def setUp(self):
		self.d = self.u.session("com.circle.youyu")  # 每跑完一个test就restart app
		time.sleep(3)  # 等待首页广告结束

	def tearDown(self):
		pass

	@getImage
	# @unittest.skip('tiaoguo')
	def test0(self):
		handl.swipeToLeft(self.d)
		handl.swipeToLeft(self.d)
		self.d(resourceId="com.circle.youyu:id/iv_gif").click()
		handl.swipeToLeft(self.d)
	@getImage
	# @unittest.skip('tiaoguo')
	def test1(self):
		'''
		检查登录功能能否正常使用
		:return:
		'''
		try:
			indexPage.screenClose(self.d).click()#关闭首页可能出现的闪屏弹窗
		except Exception as e:
			print(str(e)+"当前未出现闪屏")
		indexPage.mineButton(self.d).click()
		handl.swipeToUp(self.d)
		MinePage.setButton(self.d).click()
		loginPage.userLoginButton(self.d).click()
		self.d.clear_text()
		time.sleep(1)
		loginPage.usernameText(self.d).send_keys(Config.loginUser)
		time.sleep(1)
		loginPage.passwordText(self.d).send_keys(Config.loginPsd)
		loginPage.loginButton(self.d).click()
		handl.swipeToDown(self.d)
		MinePage.activity_center(self.d).click()
		print(self.d(text=u"超赞福利社").get_text())
		self.assertEqual(self.d(text=u"超赞福利社").get_text(),"超赞福利社","登录成功")

	@getImage
	# @unittest.skip('tiaoguo')
	def test_2(self):
		'''检查忘记密码功能'''
		MinePageEvs.loggout(self.d)
		MinePage.setButton(self.d).click()
		loginPage.userLoginButton(self.d).click()
		loginPage.forgetPassword(self.d).click()
		loginPage.PhoneNumText(self.d).send_keys(Config.loginUser)
		loginPage.NextButton(self.d).click()
		code = getCode(Config.loginUser,4)
		print(code)
		loginPage.codeText(self.d).send_keys(code)
		loginPage.setPasswordText(self.d).send_keys(Config.loginPsd)
		loginPage.submitButton(self.d).click()
		MinePageEvs.loggout(self.d)
		indexPage.mineButton(self.d).click()
		handl.swipeToUp(self.d)
		MinePage.setButton(self.d).click()
		loginPage.userLoginButton(self.d).click()
		self.d.clear_text()
		loginPage.usernameText(self.d).send_keys(Config.loginUser)
		loginPage.passwordText(self.d).send_keys(Config.loginPsd)
		loginPage.loginButton(self.d).click()
		handl.swipeToDown(self.d)
		MinePage.activity_center(self.d).click()
		print(self.d(text=u"超赞福利社").get_text())
		self.assertEqual(self.d(text=u"超赞福利社").get_text(), "超赞福利社", msg="登录成功")
	@getImage
	# @unittest.skip('tiaoguo')
	def test_3(self):
		'''检查未登录时，点击我的界面各个按钮是否跳转到登录界面'''
		MinePageEvs.loggout(self.d)
		MinePage.fansButton(self.d).click()
		self.assertEqual(loginPage.userLoginButton(self.d).get_text(),"账号登录")
		self.d(resourceId="com.circle.youyu:id/iv_close").click()
		MinePage.draftButton(self.d).click()#
		self.assertEqual(loginPage.userLoginButton(self.d).get_text(), "账号登录")
		self.d(resourceId="com.circle.youyu:id/iv_close").click()
		MinePage.myAddpraiseButton(self.d).click()
		self.assertEqual(loginPage.userLoginButton(self.d).get_text(), "账号登录")
		self.d(resourceId="com.circle.youyu:id/iv_close").click()
		MinePage.myTopicButton(self.d).click()
		self.assertEqual(loginPage.userLoginButton(self.d).get_text(), "账号登录")
		self.d(resourceId="com.circle.youyu:id/iv_close").click()
		MinePage.myMedalButton(self.d).click()
		self.assertEqual(loginPage.userLoginButton(self.d).get_text(), "账号登录")
		self.d(resourceId="com.circle.youyu:id/iv_close").click()
		MinePage.newfriendButton(self.d).click()
		self.assertEqual(loginPage.userLoginButton(self.d).get_text(), "账号登录")
		self.d(resourceId="com.circle.youyu:id/iv_close").click()

	@getImage
	# @unittest.skip('tiaoguo')
	def test_4(self):
		indexPage.mineButton(self.d).click()
		MinePage.loginButton(self.d).click()
		loginPage.userLoginButton(self.d).click()
		self.d.clear_text()
		loginPage.usernameText(self.d).send_keys(Config.loginUser)
		loginPage.passwordText(self.d).send_keys(Config.loginPsd)
		loginPage.loginButton(self.d).click()
		MinePage.activity_center(self.d).click()
		time.sleep(3)
		handl.swipeToUp(self.d)
		self.d(text=u"draw").click()
		MinePageEvs.share(self,self.d)

	@getImage
	# @unittest.skip('tiaoguo')
	def test_5(self):
		'''
		用户主页分享功能检测
		:return:
		'''
		indexPage.mineButton(self.d).click()
		MinePage.showUserName(self.d).click()
		self.d(resourceId="com.circle.youyu:id/menusBlack").click()
		time.sleep(3)
		self.d(resourceId="com.circle.youyu:id/iv_share_wechat").click()
		time.sleep(3)
		# print(self.d(resourceId="com.tencent.mm:id/nr", text=u"wo").get_text())
		self.assertEqual(self.d(resourceId="com.tencent.mm:id/ave").get_text(), u"创建新聊天")
		time.sleep(3)
		self.d.press("back")
		self.d(resourceId="com.circle.youyu:id/iv_share_circle").click()
		time.sleep(3)
		self.assertEqual(self.d(resourceId="android:id/text1").get_text(), "微信")
		self.d.press("back")
		self.d(resourceId="com.tencent.mm:id/apj").click()

	@getImage
	# @unittest.skip('tiaoguo')
	def test_5(self):
		"""
		王牌悬赏令活动分享检测
		:return:
		"""
		indexPage.mineButton(self.d).click()
		MinePage.activity_center(self.d).click()
		time.sleep(3)
		handl.swipeToUp(self.d)
		self.d(text=Config.activityNOMoney).click()
		time.sleep(3)
		self.d(text=u"已结束" ).click()
		time.sleep(3)
		MinePageEvs.share(self,self.d)

	@getImage
	# @unittest.skip('tiaoguo')
	def test_6(self):
		"""
		聚集地分享检测
		:return:
		"""
		indexPage.find(self.d).click()
		self.d.tap(100,100)
		self.d.tap(100,100)
		handl.swipeToUp(self.d)
		handl.swipeToUp(self.d)
		self.d(resourceId="com.circle.youyu:id/layout_tip").click()
		MinePageEvs.share_jujidi(self,self.d)

	@getImage
	# @unittest.skip('tiaoguo')
	def test_7(self):
		'''
		悬赏话题分享
		:return:
		'''
		indexPage.find(self.d).click()
		self.d(resourceId="com.circle.youyu:id/rlXSTopic").click()
		MinePageEvs.share(self, self.d)

if __name__ == "__main__":
	unittest.main()
