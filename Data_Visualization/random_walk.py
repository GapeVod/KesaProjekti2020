from random import choice

class RandomWalk:
	"""A class to generate random walks."""

	def __init__(self, num_points=5000):
		"""Initialize attributes of a walk."""
		self.num_points = num_points

		#All walks start at (0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		"""Get the step's of x and y axis."""
		#Decide which direction to go and how far to go in that direction.
		x_direction = choice([1, -1])
		#x_direction = choice([1])
		x_distance = choice(range(0,9))
		x_step = x_direction * x_distance

		y_direction = choice([1, -1])
		y_distance = choice(range(0,9))
		y_step = y_direction * y_distance


		#Calculate the new position.
		x = self.x_values[-1] + x_step
		y = self.y_values[-1] + y_step

		self.x_values.append(x)
		self.y_values.append(y)						

	def fill_walk(self):
		"""Calculate al the points in the walk."""

		#Keep taking steps until the alk reaches the desired length.
		while len(self.x_values) < self.num_points:

			#Decide which direction to go and how far to go in that direction.
			#x_direction = choice([1, -1])
			#x_direction = choice([1])
			#x_distance = choice(range(0,9))
			x_step = self.get_step()

			#y_direction = choice([1, -1])
			#y_distance = choice(range(0,9))
			y_step = self.get_step()

			#Reject moves that go nowhere.
			if x_step == 0 and y_step == 0:
				continue

			#Calculate the new position.
			#x = self.x_values[-1] + x_step
			#y = self.y_values[-1] + y_step

			#self.x_values.append(x)
			#self.y_values.append(y)