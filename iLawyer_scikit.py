# collection of all functions using scikit

import iLawyer_basic as ib
from openpyxl import Workbook
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.multiclass import OutputCodeClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn import tree


# training by support vector classification http://scikit-learn.org/stable/tutorial/basic/tutorial.html
def train_by_SVC(X, y):
    clf = SVC(gamma=0.001, C=100.)
    return clf.fit(X, y)
# DONE


# training by One-Vs-One http://scikit-learn.org/stable/modules/multiclass.html#id1
def train_by_OneVsOneClassifier(X, y):
    clf = OneVsOneClassifier(LinearSVC(random_state=0))
    return clf.fit(X, y)
# DONE


# training by One-Vs-Rest http://scikit-learn.org/stable/modules/multiclass.html
def train_by_OneVsRestClassifier(X, y):
    clf = OneVsRestClassifier(LinearSVC(random_state=0))
    #clf = OneVsRestClassifier(estimator=SVC(random_state=0))
    return clf.fit(X, y)
# DONE


# training by Output-Codes http://scikit-learn.org/stable/modules/multiclass.html
def train_by_OutputCodeClassifier(X, y):
    clf = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)
    return clf.fit(X, y)
# DONE


# training by stochastic gradient descent classification http://scikit-learn.org/stable/modules/sgd.html#classification
def train_by_SGDClassifier(X, y):
    clf = SGDClassifier(loss="hinge", penalty="l2")
    return clf.fit(X, y)
# DONE


# training by multi-layer perceptron (MLP) algorithm that trains using Backpropagation
# http://scikit-learn.org/stable/modules/neural_networks_supervised.html#classification
def train_by_MLPClassifier(X, y, hidden_layer_sizes):
    clf = MLPClassifier(activation = 'logistic', solver='lbfgs', alpha=1e-5, learning_rate = 'adaptive', hidden_layer_sizes=hidden_layer_sizes, max_iter=400, random_state=1)
    return clf.fit(X, y)
# DONE


def train_by_MLPClassifier_regularization(X, y, hidden_layer_sizes, alpha, max_iter):
    clf = MLPClassifier(activation='logistic', solver='lbfgs', alpha=alpha, learning_rate='adaptive',
                        hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter, random_state=1)
    return clf.fit(X, y)
# DONE


# training by decision Tree - http://scikit-learn.org/stable/modules/tree.html
def train_by_DecisionTreeClassifier(X, y):
    clf = tree.DecisionTreeClassifier()
    return clf.fit(X, y)
# DONE


# return label from clf model, input: X is vector 2D
def gen_prediction(clf, X):
    return clf.predict(X)
# DONE


# calculate performance: percentage (number of prediction label that equal correct label)
def cal_performance(correct_lables, cal_labels):
    number_label = len(cal_labels)
    cnt = 0
    for i in range(0, number_label):
        if cal_labels[i] == correct_lables[i]:
            cnt += 1
    return 1.0 * cnt / number_label
# DONE
