import csv
import pandas as pd
import numpy as np
import math
import random
from sklearn.cross_validation import train_test_split






# Creating Testing and Training Data
rawdataset = pd.read_csv("iris.csv")
#print(dataset)

trainSet = rawdataset.sample(frac=0.8, random_state = 1)# split data into 80% training with 20% for testing

testSet = rawdataset.loc[~rawdataset.index.isin(trainSet.index)]


# Fitting Data
features = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']

def findMean(dataset, feature, label):

	featureTotal = 0
	numRows = 0

	for  index, row in dataset.iterrows():
		if row['Species'] == label:
			numRows = numRows + 1
			featureTotal = featureTotal + row[feature]
	mean = featureTotal / numRows
	return mean



def findSD(dataset, feature, label, mean):
	tmp = []
	for index, row in dataset.iterrows():
		if row['Species'] == label:
			tmp.append(row[feature])
		
	return np.std(tmp, ddof=1)

def findPDF(x, mean, sd):
	exponent = math.exp(-(math.pow((x-mean),2)/(2*math.pow(sd,2))))
	return ( 1 / (math.sqrt(2*math.pi) * sd) * exponent)

def gaussianCF(vector):
	
	features = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
	labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']
	bestProb = -1000
	bestClass = ""
	
	for i in range(0,3):

		probabilities = []
		for x in range(len(vector)):
			mean = findMean(trainSet, features[x], labels[i])
			sd = findSD(trainSet, features[x], labels[i], mean)
			pdf = findPDF(vector[x], mean, sd)
			probabilities.append(math.log(pdf))
		prob = np.sum(probabilities)
		if prob > bestProb or bestProb == -1000:
			bestProb = prob
			bestClass = labels[i]

	
	return bestClass


def accuracy():

	features = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
	labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']
	numCorrect = 0
	numAttempts = 0

	for index, row in testSet.iterrows():
		
		vector = [row[features[0]],row[features[1]],row[features[2]],row[features[3]]]

		guess = gaussianCF(vector)
		# print("Guess is: ", guess, "and actual class is: ", row['Species'])
		if guess == row['Species']:
			numCorrect = numCorrect + 1
			numAttempts = numAttempts + 1
		else:
			numAttempts = numAttempts + 1

	print("Number Correct:  ", numCorrect)
	print("Number Attempts: ", numAttempts)
	accuracy = numCorrect/numAttempts	
	return accuracy



print("Accuracy: ", accuracy()*100,"%")


















