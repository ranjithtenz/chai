class HTTPRequest:
	"""
	Wrapper around HTTPRequest

	- selects database
	- manages session
	- calls "action"

	"""
	def __init__(self):
		self.action = None
		self.database = None
		
		self.set_cookies()
		self.select_db()
	
	def set_cookies(self):
		"""
		Builds cookies dictionary
		"""
		def get_incoming_cookies(self):
			import os
			import Cookie

			cookies = Cookie.SimpleCookie()
			self.cookies = {}
			
			if 'HTTP_COOKIE' in os.environ:
				c = os.environ['HTTP_COOKIE']
				cookies.load(c)
				
				for c in cookies.values():
					self.cookies[c.key] = c.value

				
	def select_db(self):
		"""
		Selects db
		"""