from pages import indexPage,MinePage
from utils.handles import handl
import time
def loggout(dirver):
	indexPage.mineButton(dirver).click()
	handl.swipeToUp(dirver)
	MinePage.setButton(dirver).click()
	handl.swipeToUp(dirver)
	MinePage.logoutButton(dirver).click()
	indexPage.dialog_sureButton(dirver).click()
def share(self,driver):
	driver(resourceId="com.circle.youyu:id/menusBlack").click()
	time.sleep(3)
	driver(resourceId="com.circle.youyu:id/iv_share_wechat").click()
	time.sleep(7)
	# print(driver(resourceId="com.tencent.mm:id/nr", text=u"wo").get_text())
	self.assertEqual(driver(resourceId="com.tencent.mm:id/ave").get_text(), u"创建新聊天")
	time.sleep(5)
	driver.press("back")
	driver(resourceId="com.circle.youyu:id/menusBlack").click()
	driver(resourceId="com.circle.youyu:id/iv_share_circle").click()
	time.sleep(5)
	self.assertEqual(driver(resourceId="android:id/text1").get_text(), "微信")
	driver.press("back")
	driver(resourceId="com.tencent.mm:id/au_").click()
def share_jujidi(self,driver):
	driver(resourceId="com.circle.youyu:id/special_share").click()
	time.sleep(3)
	driver(resourceId="com.circle.youyu:id/iv_share_wechat").click()
	time.sleep(7)
	# print(driver(resourceId="com.tencent.mm:id/nr", text=u"wo").get_text())
	self.assertEqual(driver(resourceId="com.tencent.mm:id/ave").get_text(), u"创建新聊天")
	time.sleep(5)
	driver.press("back")
	driver(resourceId="com.circle.youyu:id/special_share").click()
	driver(resourceId="com.circle.youyu:id/iv_share_circle").click()
	time.sleep(5)
	self.assertEqual(driver(resourceId="android:id/text1").get_text(), "微信")
	driver.press("back")
	driver(resourceId="com.tencent.mm:id/au_").click()