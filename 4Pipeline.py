#import a dataset of 150 samples
from sklearn import datasets
iris = datasets.load_iris()

# f(x) = y --> f(x) = features, y = label
x = iris.data
y = iris.target

# split to use 75 for training and 75 for testing
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)

from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

#train the classifier
my_classifier.fit(x_train, y_train)

predictions = my_classifier.predict(x_test)
print (predictions)
print (y_test)

#compared how accurate is the classifier in percentage
from sklearn.metrics import accuracy_score
print (accuracy_score(y_test, predictions))