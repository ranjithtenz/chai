# Chai Project 0.1
# (c) 2011 Web Notes Technologies
# Chai Project may be freely distributed under MIT license
# Authors: Rushabh Mehta (rmehta at gmail)

request = None
response = None
session = None
db_session = None

def T(text):
	"""
	Translate the string in the given language
	"""
	from chai.utils.translate import translate
	translate(s)