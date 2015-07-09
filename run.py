import csv
import sys
from rules import *

class ParseHandler:
	def __init__(self):
		# Get all the subclasses of Rule
		self.rules = Rule.__subclasses__()

		# Create files for valid and invalid outputs
		self.valid_file = open('valid.csv', 'w+')
		self.invalid_file = open('invalid.csv', 'w+')

		fieldnames = ['id','title','privacy','total_plays','total_comments','total_likes']
   		self.valid_writer = csv.DictWriter(self.valid_file, fieldnames=fieldnames)
   		self.invalid_writer = csv.DictWriter(self.invalid_file, fieldnames=fieldnames)

   		# Write the headers
   		self.valid_writer.writeheader()
   		self.invalid_writer.writeheader()

	def run(self, filename):
		try:
			with open(filename) as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					valid = self.parse(row)

					if valid:
						# add to valid.csv
						self.valid_writer.writerow(row)
					else:
						# add to invalid.csv
						self.invalid_writer.writerow(row)

			self.valid_file.close()
			self.invalid_file.close()

		except IOError:
			raise IOError('The file does not exist')
		except KeyError:
			raise KeyError('The CSV has missing headers')

	def parse(self, line):
		# Given a line, see if it matches all of the rules 
		count = 0

		for rule in self.rules:
			if rule().execute(line):
				count += 1

		if count == len(self.rules):
			return True
		else:
			return False

if __name__ == "__main__":
	parser = ParseHandler()

	if len(sys.argv) == 2:
		parser.run(sys.argv[1])
	else:
		print 'Usage: python run.py filename'



	
	
