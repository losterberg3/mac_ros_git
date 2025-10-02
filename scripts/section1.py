#!/usr/bin/env python3

import numpy as np

if __name__ == "__main__":

	# code goes here
	print("hello world")
	np.random.seed(42)
	x = np.random.normal(size=(4, 10))
	a = np.ones((10,4))
	b = np.ones((4,10))
	asquare = np.square(x)
	atsquare = np.square(x.T)
	square = np.array((asquare @ a) - 2 * (x @ x.T) + (b @ atsquare)) #using the formula (a - b)^2 = a^2 -2ab + b^2
	print(square)
