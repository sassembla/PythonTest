import unittest
class TestTarget(object):
	def plusOne(self, o):
		return o+1

	def minusOne(self, o):
		return o-1

class Test(unittest.TestCase):
	def setUp(self):
		self.obj = TestTarget()

	def tearDown(self):
		pass

	def testPlusOne(self):
		assert self.obj.plusOne(5) == 6


	def testMinusOne(self):
		assert self.obj.minusOne(5) == 4

unittest.main()