#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring.
"""
import urllib2
import json

class Cell(object):
	"""
	Cell object of the maze.
	"""
	def __init__(self, json_dump):

		self.number = ""
		self.name = ""
		self.url = ""
		self.neighbors = {}
		

		self.number = str(json_dump["cells"][0]["id"])
		self.url = "http://apibunny.com/cells/" + self.number
		self.name = json_dump["cells"][0]["name"]
		self.neighbors = json_dump["cells"][0]["links"]
		del self.neighbors["maze"]

	def __str__(self):

		string = "Cell: \"{}\" ID: {}\nNeighbors:\n".format(self.name, self.number)
		for key in self.neighbors.keys():
			string += "Direction: {} ID: {}".format(key, self.neighbors[key])

		return string


start_url = urllib2.urlopen('http://apibunny.com/cells/taTKQ3Kn4KNnmwVI')

start_cell = json.load(start_url)
