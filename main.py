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
dict_file_name = "dict002.xlsx" # currently we use tableTraining.xlsx for generate dictionary
dict_num_rows = 372
id_column_question = 2
id_column_label = 3
dict, num_words = il.gen_dict_from_xlsx(dict_file_name, dict_num_rows, id_column_question)
print len(dict)
dict001_Gen01_txt = 'dict002_Gen01.txt'
ib.print_txt_from_array(dict, dict001_Gen01_txt)

# search all keywords in tableTraining, reshape in matrix form (X, y)
training_file_name = "dict002.xlsx"
num_examples = 371
num_features = 213
performance_xlsx = 'performanceDict002.xlsx'

X, y = il.gen_feature_table_labels(training_file_name, dict_num_rows, id_column_question, id_column_label, dict)
print "Vector X:"
for i in X:
    print i
print "Label:"
print y
#print "Print file XLSX"
#isk.print_xlsx_prediction(performance_xlsx, training_file_name, dict_num_rows, id_column_question, X, y, num_features)

# 1.2: training
print "Training"
clf = isk.train_by_MLPClassifier(X, y, num_features)
cal_labels = isk.predict(clf, X)
correct_labels = y

print "Cal_labels: ", cal_labels
print "Correct_labels: ", correct_labels

performance = isk.cal_performance(correct_labels, cal_labels)
print "Performances MLP", performance


# 1.3: post-processing



#########################
# Part 2: cross evaluation





#########################
# Part 3: validation, prediction


# http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
