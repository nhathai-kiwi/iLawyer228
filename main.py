# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question
import iLawyer_lib as il
import iLawyer_scikit as isk
import iLawyer_basic as ib
#########################
# Part 1: training process
# Part 1.1: pre-processing
# training data being stored in a file named "tableTraining.xlsx" with specific format TODO add file descritpion

# generate dictionary
dict_file_name = "table002.xlsx" # currently we use tableTraining.xlsx for generate dictionary
dict_num_rows = 214
id_column_question = 2
id_column_label = 4
dict, num_words = il.gen_dict_from_xlsx(dict_file_name, dict_num_rows, id_column_question)
print "Len dict: ", len(dict)
print "Dict: ", dict

# search all keywords in tableTraining, reshape in matrix form (X, y)
training_file_name = "table002.xlsx"
num_examples = 213
num_features = 213
performance_xlsx = 'performanceTable002.xlsx'

X, y = il.gen_feature_table_labels(training_file_name, dict_num_rows, id_column_question, id_column_label, dict)


print "Label: ", y
outLabel = ib.gen_column_from_xlsx(training_file_name, dict_num_rows, id_column_label)

isk.print_xlsx_prediction(performance_xlsx, training_file_name, dict_num_rows, id_column_question, X, y, num_features)

# 1.2: training

clf = isk.train_by_MLPClassifier(X, y, num_features)
cal_labels = isk.predict(clf, X)
correct_labels = y
performance = isk.cal_performance(correct_labels, cal_labels)
print "Performances MLP", performance


# 1.3: post-processing



#########################
# Part 2: cross evaluation





#########################
# Part 3: validation, prediction


# http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
