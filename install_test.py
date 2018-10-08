import uiautomator2 as u2
u = u2.connect('192.168.43.172')

u.push("/Users/zh/Downloads/app-baidu-release(7).apk","/sdcard/1")
# u.app_install("/Users/zh/Downloads/app-baidu-release(7).apk")