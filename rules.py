class Rule(object):
	''' Abstract class which defines what a rule will look like '''
	def execute(self, row): 
		''' Return a predicate for the given input '''
		pass

class PrivacyRule(Rule):
	def execute(self, row):
		return row['privacy'] == 'anybody'

class LikesAndPlaysRule(Rule):
	def execute(self, row):
		return int(row['total_likes']) > 10 and int(row['total_plays']) > 200

class TitleRule(Rule):
	def execute(self, row):
		return len(row['title']) < 30