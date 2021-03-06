#!/usr/bin/env python
# -*- coding: utf-8 -*-

# iLawyer library
import iLawyer_basic as ib


# generate dictionary from xlsx file, keep monosyllable words
# TODO add description for input xlsx
def gen_dict_from_xlsx(inp_xlsx, num_rows, id_column):
    all_questions = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column)
    ib.print_txt_from_array(all_questions, out_txt='vncore_inp.txt') # print output to a file, this file will be deleted later
    ib.process_vncore('vncore_inp.txt', 'vncore_out.txt')
    dict_replicated = ib.gen_words_from_vncore_out_txt('vncore_out.txt')
    dict = ib.gen_distinct_array(dict_replicated)
    dict.sort()
    ib.process_delete_file('vncore_inp.txt')
    ib.process_delete_file('vncore_out.txt')
    return dict, len(dict)
# DONE


# generate dictionary from xlsx file, keep multiple syllable words only
def gen_dict_from_xlsx_02(inp_xlsx, num_rows, id_column):
    all_questions = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column)
    ib.print_txt_from_array(all_questions, out_txt='vncore_inp.txt') # print output to a file, this file will be deleted later
    ib.process_vncore('vncore_inp.txt', 'vncore_out.txt')
    dict_replicated = ib.gen_words_from_vncore_out_txt_02('vncore_out.txt')
    dict = ib.gen_distinct_array(dict_replicated)
    dict.sort()
    ib.process_delete_file('vncore_inp.txt')
    ib.process_delete_file('vncore_out.txt')
    return dict, len(dict)
# DONE


# generate dictionary from xlsx file, keep multiple syllable words only
def gen_dict_from_xlsx_with_count(inp_xlsx, num_rows, id_column):
    all_questions = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column)
    ib.print_txt_from_array(all_questions, out_txt='vncore_inp.txt') # print output to a file, this file will be deleted later
    ib.process_vncore('vncore_inp.txt', 'vncore_out.txt')
    dict_replicated = ib.gen_words_from_vncore_out_txt('vncore_out.txt')
    dict = ib.gen_distinct_array_with_count(dict_replicated)
    #dict.sort()
    ib.process_delete_file('vncore_inp.txt')
    ib.process_delete_file('vncore_out.txt')
    return dict, len(dict)
# DONE


# generate feature table and labels from a training set stored in xlsx
# TODO add description for input xlsx
def gen_feature_table_labels(inp_xlsx, num_rows, id_column_question, id_column_label, dict):
    feature_table = ib.gen_feature_table_from_xlsx(inp_xlsx, num_rows, id_column_question, dict)
    labels = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column_label)
    return feature_table, labels
