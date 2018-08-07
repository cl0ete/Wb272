import math
"""A point in two-dimentional Euclidean space"""
class Point:
	"""Initialise a new point with coordinates (x,y)"""
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def distance_to(self, p):
		dx =self.x - p.x
		dy =self.y - p.y
		return math.sqrt(dx*dx + dy*dy)

	def __str__(self):
		"""x.__str__() <==> str(x)"""
		return '('+ str(self.x) + ', '+ str(self.y)+')'
