# Checks accuracy of predicitions.txt

pred = open('predictions.txt', "r")
f = open('iris.vw', "r")
numCorrect = 0
numAttempts = 0
predictions = []
test = []

for line in pred:
	predictions.append(line.split(None,1)[0])

for l in f:
	test.append(l.split(None,1)[0])

pred.close()
f.close()

for i in range(0,len(predictions)):
	if predictions[i] == test[i]:
		numCorrect = numCorrect+1
		numAttempts = numAttempts+1
	else:
		numAttempts = numAttempts+1

accuracy = (numCorrect/numAttempts)*100
print("Accuracy is: ", accuracy,"%")