#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring.
"""
import urllib2
import json
import random

class Cell(object):
	"""
	Cell object of the maze.
	"""
	def __init__(self, json_dump):

		self.number = ""
		self.name = ""
		self.url = ""
		self.neighbors = {}
		self.type = ""
		

		self.number = str(json_dump["cells"][0]["id"])
		self.url = "http://apibunny.com/cells/" + self.number
		self.name = json_dump["cells"][0]["name"]
		self.neighbors = json_dump["cells"][0]["links"]
		del self.neighbors["maze"]
		self.type = json_dump["cells"][0]["type"]

	def __str__(self):

		string = "Cell: \"{}\" ID: {}\nNeighbors:\n".format(self.name, self.number)
		for key in self.neighbors.keys():
			string += "{} ID: {}\n".format(key, self.neighbors[key])

		return string

	def __repr__(self):
		return self.__str__()

	def random_neighbors(self):
		"""
		Return a random neighbor of the cell.
		"""
		keys = self.neighbors.keys()
		rand = random.randrange(len(keys))

		return self.neighbors[keys[rand]]

start_url = urllib2.urlopen('http://apibunny.com/cells/taTKQ3Kn4KNnmwVI')

start_cell = Cell(json.load(start_url))
