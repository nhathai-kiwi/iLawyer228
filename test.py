#!/usr/bin/env python
# -*- coding: utf-8 -*-

import iLawyer_basic as ib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

array_string_question = ib.gen_string_array_from_txt('input.txt')
for word  in array_string_question:
    print word, " ", len(word)
if ib.check_question_at_least_2_keywords(array_string_question) == False:
    print "Please retype your question."


# string_array = ib.gen_array_from_txt('articles_out.txt')
#
# print len(string_array)
# num_word = len(string_array)
#
# cnt = 0
# list_word_questions = []
# question = []
# for word in string_array:
#     word_remove_last_char = word[:-1]
#     if word_remove_last_char == '$':
#         cnt += 1
#         list_word_questions.append(question)
#         question = []
#     else:
#         question.append(word_remove_last_char)
#
# question.append(question)
# f = open('articles_word_out.txt', "w")
# print "Cnt: ", cnt
# for i in range(1, 30):
#     dem = 0
#     for j in list_word_questions:
#         if i == len(j):
#             dem += 1
#     print i, " ", dem

# for i in list_word_questions:
#     print len(i), i
    #f.write(str(len(i)) + i )
