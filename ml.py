import sklearn
import json

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

soberFile = open("sober.json", "r")
fileString = soberFile.read()
dataJSON = json.loads(fileString)
features = dataJSON['data']
labels = dataJSON['drunk']
soberFile.close()

drunkFile = open("drunk.json", "r")
fileString = drunkFile.read()
dataJSON = json.loads(fileString)
features = features + dataJSON['data']
labels = labels + dataJSON['drunk']
drunkFile.close()

train, test, train_labels, test_labels = train_test_split(features,
                                                          labels,
                                                          test_size=0.33,
                                                          random_state=42)

# Initialize our classifier
gnb = GaussianNB()

# Train our classifier
model = gnb.fit(train, train_labels)
preds = gnb.predict(test)

# Evaluate accuracy
print(accuracy_score(test_labels, preds))


def isDrunk(inputData):
    return gnb.predict([inputData])

