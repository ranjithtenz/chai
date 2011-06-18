# Chai Project 0.1
# (c) 2011 Web Notes Technologies
# Chai Project may be freely distributed under MIT license

# based on Backbone.js by Jeremy Ashkenas, DocumentCloud Inc.


class Events:
	"""
		Implementation of Backbone.Events class
	"""
	def __init__(self):
		pass
	
	def bind(self, callback):
		"""
			Bind an event, specified by a string name, ev, 
			to a callback function. Passing "all" will bind the callback to all 
			events fired.
		"""
		if not self._callbacks: 
			self._callbacks = {}
		if not self._callbacks.has_key(ev):
			self._callbacks[ev]=[]
		
		self._callbacks[ev].append(callback)
		