# _*_ coding:utf-8 _*_

import unittest
import sys


class demoTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("我是setupclass")
	@classmethod
	def tearDownClass(cls):
		print("我是tearDownclass")
	def setUp(self):
		print("我是setup")
	def tearDown(self):
		print("我是teardown")

	def test1(self):
		print("我是test1")
	def test2(self):
		print("我是test2")


if __name__ == '__main__':
	unittest.main()
