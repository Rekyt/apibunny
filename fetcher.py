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

class Character(object):
	"""
	Character class to move in the maze.
	"""

	def __init__(self, start_cell):
		
		self.known_cells = []
		self.visited_cells = []
		self.current_cell = None

		self.current_cell = start_cell
		self.known_cells.append(start_cell)
		for neigh in start_cell.neighbors.values():
			self.known_cells.append(neigh)
		self.visited_cells.append(start_cell)

	def __repr__(self):
		return "Character in\n{}".format(self.current_cell)


start_url = urllib2.urlopen('http://apibunny.com/cells/taTKQ3Kn4KNnmwVI')

start_cell = Cell(json.load(start_url))
