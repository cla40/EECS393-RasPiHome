import unittest

class TestHomeAutomation(unittest.TestCase):

	def setUp(self):
		print '\nsetup'
		
	def test_flipstate(self):
		print 'flipstate test'
		
	def test_log(self):
		print 'log test'
		
	def test_whattest(self):
		print 'whattest test'
		
if __name__ == '__main__':
	unittest.main()