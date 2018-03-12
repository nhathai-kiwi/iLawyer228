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
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import pandas as pd

# training by support vector classification http://scikit-learn.org/stable/tutorial/basic/tutorial.html
def train_by_SVC(X, y):
    clf = SVC(gamma=0.001, C=100.)
    return clf.fit(X, y)


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
def train_by_MLPClassifier(X, y, num_features):
    clf = MLPClassifier(activation = 'logistic', solver='lbfgs', alpha=1e-5, learning_rate = 'adaptive', hidden_layer_sizes=(num_features), max_iter=400, random_state=1)
    return clf.fit(X, y)
# DONE

def train_by_MLPClassifier_regularization(X, y, num_features, alpha, max_iter):
    clf = MLPClassifier(activation='logistic', solver='lbfgs', alpha=alpha, learning_rate='adaptive',
                        hidden_layer_sizes=(num_features), max_iter=max_iter, random_state=1)
    return clf.fit(X, y)

# training by decision Tree - http://scikit-learn.org/stable/modules/tree.html
def train_by_DecisionTreeClassifier(X, y):
    clf = tree.DecisionTreeClassifier()
    # dot_data = tree.export_graphviz(clf, out_file=None)
    # graph = graphviz.Source(dot_data)
    # graph.render("ilaw")
    # dot_data = tree.export_graphviz(clf, out_file=None,
    #                                 feature_names=ilaw.feature_names,
    #                                 class_names=ilaw.target_names,
    #                                 filled=True, rounded=True,
    #                                 special_characters=True)
    # graph = graphviz.Source(dot_data)
    # print "Graph:"
    # print graph
    return clf.fit(X, y)


# return label from clf model, input: X is vector 2D
def predict(clf, X):
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


def learning_curves(estimator, features, target, train_sizes, cv):
    train_sizes, train_scores, validation_scores = learning_curve(
        estimator, features, target, train_sizes=train_sizes,
        cv=cv, scoring='neg_mean_squared_error')
    train_scores_mean = -train_scores.mean(axis=1)
    validation_scores_mean = -validation_scores.mean(axis=1)

    print('Mean training scores\n\n', pd.Series(train_scores_mean, index=train_sizes))
    print('\n', '-' * 20)  # separator
    print('\nMean validation scores\n\n', pd.Series(validation_scores_mean, index=train_sizes))


    plt.plot(train_sizes, train_scores_mean, label='Training error')
    plt.plot(train_sizes, validation_scores_mean, label='Validation error')

    plt.ylabel('MSE', fontsize=14)
    plt.xlabel('Training set size', fontsize=14)
    title = 'Learning curves for a ' + str(estimator).split('(')[0] + ' model'
    plt.title(title, fontsize=18, y=1.03)
    plt.legend()
    plt.ylim(0, 40)


def print_xlsx_prediction(out_xlsx, training_file_name, num_rows, id_column_question, X, y, num_features):
    questions = ib.gen_column_from_xlsx(training_file_name, num_rows, id_column_question)
    correct_labels = y

    cal_labels = []

    cal_labels.append( predict(train_by_SVC(X, y), X))
    cal_labels.append( predict(train_by_OneVsOneClassifier(X, y), X))
    cal_labels.append( predict(train_by_OneVsRestClassifier(X, y), X))
    cal_labels.append( predict(train_by_OutputCodeClassifier(X, y), X))
    cal_labels.append( predict(train_by_MLPClassifier(X, y, num_features), X))

    book = Workbook()
    sheet = book.active

    sheet.append(("STT", "Question", "Label", "SVC", "OvOC", "OvRC", "OCC", "MLPC"))

    number_question = 0
    for i in range(0, len(questions)):
        number_question += 1
        question = questions[i]
        label = correct_labels[i]
        label_svc = cal_labels[0][i]
        label_ovoc = cal_labels[1][i]
        label_ovrc = cal_labels[2][i]
        label_occ = cal_labels[3][i]
        label_mlpc = cal_labels[4][i]
        row = (number_question, question, label, label_svc, label_ovoc, label_ovrc, label_occ, label_mlpc)
        sheet.append(row)

    book.save(out_xlsx)
    return 0
# DONE