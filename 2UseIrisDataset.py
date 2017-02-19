from sklearn.datasets import load_iris
from sklearn import tree

import numpy as np

iris = (load_iris())

# output dataset
print iris.feature_names #'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'
print iris.target_names # 'setosa' 'versicolor' 'virginica'
print iris.data[0] #5.1  3.5  1.4  0.2
print iris.target[0] #0

for i in range(len(iris.target)):
    print "Example %d: label %s, features %s" % (i,iris.target[i], iris.data[i])


# testing
test_idx = [0, 50, 100] #remove the first of each type of iris flower
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis = 0)

test_target = iris.target[test_idx] # to print the removed data
test_data = iris.data[test_idx] # data used to be predicted using the remaining data

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
print test_target 
print clf.predict(test_data)

# vizualization code using Graphviz

from sklearn.externals.six import StringIO
import pydotplus

#tree.export_graphviz(clf,
#out_file='irisTree.dot',  feature_names=iris.feature_names,  
 #                        class_names=iris.target_names,  
#                       filled=True, rounded=True,  
   #                      special_characters=True)



dot_data = StringIO()
tree.export_graphviz(clf, 
                        out_file=dot_data, 
                        feature_names=iris.feature_names,  
                        class_names=iris.target_names,  
                        filled=True, rounded=True,  
                        impurity=False)  

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("Iris.pdf")