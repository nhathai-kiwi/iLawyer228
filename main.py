# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question

import iLawyer_lib as il
import iLawyer_scikit as isk
import iLawyer_basic as ib
#########################
# Part 1: training process
# Part 1.1: pre-processing
# training data being stored in a file named "tableTraining.xlsx" with specific format TODO add file descritpion

id_column_question = 2
id_column_label = 3

# generate dictionaryib
dict_file_name = "dict001.xlsx" # currently we use tableTraining.xlsx for generate dictionary
dict_num_rows = 214
dict, num_words = il.gen_dict_from_xlsx_with_count(dict_file_name, dict_num_rows, id_column_question)
print len(dict)
ib.print_txt_from_array(dict, 'dictQuestion01.txt')

# search all keywords in tableTraining, reshape in matrix form (X, y)

# 1.2: training

# training_file_name = "train004.xlsx"
# training_num_rows = 372
# num_features = 213
#
# X, y = il.gen_feature_table_labels(training_file_name, training_num_rows, id_column_question, id_column_label, dict)
#
# clf = isk.train_by_MLPClassifier_regularization(X, y, hidden_layer_sizes=(num_features), alpha=0.7, max_iter=400)
#
# cal_labels = isk.gen_prediction(clf, X)
# correct_labels = y
#
# performance = isk.cal_performance(correct_labels, cal_labels)
# print "Performances MLP training set: ", performance

# 1.3: post-processing
# ask_file_name = "ask001.xlsx"
# ask_num_rows = 5
# X = ib.gen_feature_table_from_xlsx(ask_file_name, ask_num_rows, id_column_question, dict)
# y = isk.gen_prediction(clf, X)
# # print "Label: ", y
# print "Label: ", y
#ib.print_txt_from_prediction('lawInEnterprise.xlsx', y[0], 2, 'output.txt')


#########################
# Part 2: cross evaluation
# print "Performances MLP cross evaluation: ", performance


#########################
# Part 3: validation, prediction
