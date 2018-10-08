# -*- coding:utf-8 -*-


#我的模块
#登录后的用户名
def showUserName(driver):
	return driver(resourceId="com.circle.youyu:id/show_user_name")
#登录／注册
def loginButton(driver):
	return driver(resourceId="com.circle.youyu:id/show_user_name")

def myAdpraiseButton(driver):
	return driver(text = "我赞过的")

	#积分中心
def activity_center(driver):
	return driver(resourceId="com.circle.youyu:id/rl_item_my_integral")

	#粉丝推广
def fansButton(driver):
	return driver(resourceId="com.circle.youyu:id/tv_me_fans")

	#草稿箱
def draftButton(driver):
	return driver(resourceId="com.circle.youyu:id/layout_item_draft_box")

	#我赞过的
def myAddpraiseButton(driver):
	return driver(resourceId="com.circle.youyu:id/rl_item_my_favourite")

	#我的话题
def myTopicButton(driver):
	return driver(resourceId="com.circle.youyu:id/tv_mine_topic")

	#我的勋章
def myMedalButton(driver):
	return driver(resourceId="com.circle.youyu:id/layout_item_my_medal")

	#推荐好友
def newfriendButton(driver):
	return driver(resourceId="com.circle.youyu:id/rl_item_my_new_friend")

	#设置界面
def setButton(driver):
	return driver(text="设置")
def logoutButton(driver):
	return driver(text="退出登录")

