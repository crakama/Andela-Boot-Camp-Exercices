import unittest

from mathx.super_sum import super_sum

#class  superSumTest(object):
class  superSumTest(unittest.TestCase):
	"""docstring for  superSumTest"""
	#def __init__(self, arg):
		#super( superSumTest, self).__init__()
		#self.arg = arg
	def test_add_twonumbers(self):
			result = super_sum(20,20)
			#TESTS TWO THINGS
			self.assertEqual(result,40)

	def test_four_numbers(self):
		result = super_sum(10, 30, 50, 20)
		self.assertEqual(result, 110)

		#result = super_s

		#a function to sum two arrays or two lists
	def test_list_and_numbers(self):
		a = [10,30,50]
		result = super_sum(a, 50)
		self.assertEqual(result, 140)

	def test_four_lists(self):
		a,b,c,d = [1,2], [2,3], [3], [4,10]
		result = super_sum(a, b,c, d)
		self.assertEqual(result, 25)

