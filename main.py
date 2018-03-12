# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question

import iLawyer_lib as il
import iLawyer_scikit as isk
import numpy as np

#########################
# Part 1: training process
# Part 1.1: pre-processing
# training data being stored in a file named "tableTraining.xlsx" with specific format TODO add file descritpion

id_column_question = 2
id_column_label = 3

# generate dictionary
dict_file_name = "dict002.xlsx" # currently we use tableTraining.xlsx for generate dictionary
dict_num_rows = 372
dict, num_words = il.gen_dict_from_xlsx(dict_file_name, dict_num_rows, id_column_question)


# search all keywords in tableTraining, reshape in matrix form (X, y)

# 1.2: training

print "STT 02"
training_file_name = "train004.xlsx"
training_num_rows = 372
num_features = 213
train_sizes = [1, 100, 200, 250, 296]


X, y = il.gen_feature_table_labels(training_file_name, training_num_rows, id_column_question, id_column_label, dict)

# alphas = np.logspace(-5, 1, 7)
# alphas = np.linspace(0.1, 1, 10)
# max_iters = np.linspace(200, 2000, 10)
#
training_cross_evaluation_file_name = "test001.xlsx"
training_num_rows = 117
X1, y1 = il.gen_feature_table_labels(training_cross_evaluation_file_name, training_num_rows, id_column_question,
                                           id_column_label, dict)
alphas = np.linspace(0.1, 1, 10)
max_iters = [400]


for alpha in alphas:
    for max_iter in max_iters:
        print "Alpha: ", alpha, "max_iter: ", max_iter
        clf = isk.train_by_MLPClassifier_regularization(X, y, num_features, alpha, max_iter)

        cal_labels = isk.predict(clf, X)
        correct_labels = y
        performance = isk.cal_performance(correct_labels, cal_labels)
        print "Performances MLP training set: ", performance


        cal_labels = isk.predict(clf, X1)
        correct_labels = y1

        performance = isk.cal_performance(correct_labels, cal_labels)
        print "Performances MLP test set: ", performance

#clf = isk.train_by_MLPClassifier_regularization(X, y, num_features, 0.7, 400)

# 1.3: post-processing



#########################
# Part 2: cross evaluation
#
# print "STT 03"
# training_cross_evaluation_file_name = "test001.xlsx"
# training_num_rows = 117
# X, y = il.gen_feature_table_labels(training_cross_evaluation_file_name, training_num_rows, id_column_question, id_column_label, dict)
#
# cal_labels = isk.predict(clf, X)
# correct_labels = y
#
# print "Cal_labels CE: ", cal_labels
# print "Correct_labels CE: ", correct_labels
#
# performance = isk.cal_performance(correct_labels, cal_labels)
# print "Performances MLP cross evaluation: ", performance


#########################
# Part 3: validation, prediction


# http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
