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

		self.number = u""
		self.name = u""
		self.url = u""
		self.neighbors = {}
		self.type = u""
		

		self.number = str(json_dump["cells"][0]["id"])
		self.url = "http://apibunny.com/cells/" + self.number
		self.url.encode("utf-8")
		self.name = json_dump["cells"][0]["name"].encode("utf-8")
		
		self.neighbors = json_dump["cells"][0]["links"]
		del self.neighbors["maze"]
		
		self.type = json_dump["cells"][0]["type"].encode("utf-8")

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
		self.known_cells.append(start_cell.number)
		
		for neigh in start_cell.neighbors.values():
			neigh_cell = return_cell(neigh)
			self.known_cells.append(neigh_cell.number)
		
		self.visited_cells.append(self.current_cell.number)

	def __repr__(self):
		return "Character in\n{}".format(self.current_cell)

	def __str__(self):
		return self.__str__()

	def random_advance(self):
		"""
		Advance in an direction.
		"""

		neigh_vals = self.current_cell.neighbors.values()
		rand_cell = random.randrange(len(neigh_vals))

		new_key = neigh_vals[rand_cell]
		new_cell = return_cell(new_key)

		self.current_cell = new_cell
		if new_cell.number not in self.visited_cells:
			self.visited_cells.append(new_cell.number)
			
			for neigh in new_cell.neighbors.values():
				neigh_cell = return_cell(neigh)
				if neigh_cell.number not in self.known_cells:
					self.known_cells.append(neigh_cell.number)

		print "New cell type: {}".format(self.current_cell.type)

	def whole(self, method):
		i = 0
		while self.current_cell.type != "exit":
			print "Current Cell: {}".format(self.current_cell.name)
			self.random_advance()
			i += 1

		print "Found the exit in {} steps.\nVisiting {} cells.".format(i, len(self.visited_cells))
			




def return_cell(cell_id):
	"""
	Return a Cell object from a cell id
	"""

	url = 'http://apibunny.com/cells/'+cell_id
	neigh_url = urllib2.urlopen(url)
	neigh_cell = Cell(json.load(neigh_url))

	return neigh_cell


start_cell = return_cell('taTKQ3Kn4KNnmwVI')

valiant = Character(start_cell)
