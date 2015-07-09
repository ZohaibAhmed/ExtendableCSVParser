from nose.tools import *
import unittest

from run import *

class TestRules(unittest.TestCase):
	def setUp(self):
		self.parser = ParseHandler()

	@raises(IOError)
	def test_parsing_empty(self):
		self.parser.run('xyz123.csv') # this file shouldn't exist

	@raises(KeyError)
	def test_values(self):
		self.parser.run('testmissing.csv')

	def test_valid_rules_files(self):
		self.parser.run('test.csv')

		# check to see if output files are created
		f = open('valid.csv', 'r')
		f = open('invalid.csv', 'r')

		assert True
		
	def test_valid_rules_output(self):
		self.parser.run('test.csv')

		valid_file = open('valid.csv')
		valid_num_lines = sum(1 for line in valid_file)
		valid_file.close()

		self.assertEquals(valid_num_lines, 347)

		invalid_file = open('invalid.csv')
		invalid_num_lines = sum(1 for line in invalid_file)
		invalid_file.close()

		self.assertEquals(invalid_num_lines, 655)
