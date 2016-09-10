"""

Parth Mishra

pami5341

parth.mishra@colorado.edu

Week 1

"""

import random
import numpy as np



def decision(previousLetter):
	if (previousLetter == 'I'):
		return np.random.choice(["_"], p=[1])
	elif (previousLetter == '_'):
		return np.random.choice(["a","l"], p=[0.5,0.5])
	elif (previousLetter == 'a'):
		return np.random.choice(["m","l"], p=[0.4,0.6])
	elif (previousLetter == 'm'):
		return np.random.choice(["_","!"], p=[0.8,0.2])
	elif (previousLetter == 'l'):
		return np.random.choice(["i"], p=[1])
	elif (previousLetter == 'i'):
		return np.random.choice(["v","n"], p=[0.95,0.05])
	elif (previousLetter == 'v'):
		return np.random.choice(["e"], p=[1])
	elif (previousLetter == 'n'):
		return np.random.choice(["e"], p=[1])
	elif (previousLetter == 'e'):
		return np.random.choice(["!"], p=[1])
	elif (previousLetter == '!'):
		return np.random.choice(["_","I","!"], p=[0.7,0.2,0.1])

for i in range(0,10):
	previousLetter = 'I'
	print(previousLetter,end=""),
	for j in range(0,100):
		nextLetter = decision(previousLetter)
		print(nextLetter,end="")
		previousLetter = nextLetter
	print("\n")


