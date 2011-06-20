# Chai Project 0.1
# (c) 2011 Web Notes Technologies
# Chai Project may be freely distributed under MIT license
# Authors: Rushabh Mehta (rmehta at gmail)

def handle():
	"""
	Handle client requests
	"""
	from chai.handler.request import HTTPRequest
	from chai.handler.response import HTTPResponse
	from chai.handler.session import Session

	chai.request = HTTPRequest()
	chai.session = Session()
	chai.response = HTTPResponse()
	
	chai.request.execute()
