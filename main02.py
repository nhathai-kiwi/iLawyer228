#!/usr/bin/env python
# -*- coding: utf-8 -*-


import iLawyer_basic as ib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

final_answer = 'Đề nghị tư vấn luật sư để có câu trả lời chính xác'

lawInEnterprise_xlsx = 'lawInEnterprise.xlsx'
columnArticle = 2
# Switch-case
class Switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == Switch.value for arg in args))


# Chapter III.3 Handle Mục 2: CÔNG TY TRÁCH NHIỆM HỮU HẠN MỘT THÀNH VIÊN 73 - 87: 15
def messageForChoice01(choiceNumber):
    while Switch(choiceNumber):
        if case(1):
            print "Bạn hỏi về vốn."
            print "Xin mời lựa chọn"
            print "\t1. Thực hiện góp vốn thành lập công ty"
            print "\t2. Thay đổi vốn điều lệ"
            print "\t3. Khác"

            choiceNumber = int(raw_input("Lựa chọn của bạn? "))
            if choiceNumber == 1:
                # print "Dieu 74 Luat DN 2014"
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 74, columnArticle)
            elif choiceNumber == 2:
                # print "Dieu 87 Luat DN 2014"
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 87, columnArticle)
            else:
                print final_answer
            break

        if case(3):
            print "Bạn hỏi về chủ sở hữu công ty."
            print "Xin mời lựa chọn"
            print "\t1. Quyền của chủ sở hữu công ty"
            print "\t2. Nghĩa vụ của chủ sở hữu công ty"
            print "\t3. Thực hiện quyền của chủ sở hữu công ty trong một số trường hợp đặc biệt"
            print "\t4. Khác"

            choiceNumber = int(raw_input("Lựa chọn của bạn? "))
            if choiceNumber == 1:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 75, columnArticle)
            elif choiceNumber == 2:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 76, columnArticle)
            elif choiceNumber == 3:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 77, columnArticle)
            else:
                print final_answer
            break

        print final_answer
        break


# Chapter IV handle: DOANH NGHIỆP NHÀ NƯỚC 88 - 109: 22
def messageForChoice02(choiceNumber):
    while Switch(choiceNumber):
        if case(1):
            print "Bạn hỏi về hội đồng thành viên."
            print "Xin mời lựa chọn"
            print "\t1. Quyền và nghĩa vụ của Hội đồng thành viên"
            print "\t2. Tiêu chuẩn và điều kiện đối với thành viên Hội đồng thành viên"
            print "\t3. Quyền và nghĩa vụ của các thành viên khác của Hội đồng thành viên"
            print "\t4. Khác"

            choiceNumber = int(raw_input("Lựa chọn của bạn? "))
            if choiceNumber == 1:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 91, columnArticle)
            elif choiceNumber == 2:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 92, columnArticle)
            elif choiceNumber == 3:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 95, columnArticle)
            else:
                print final_answer
            break

        if case(3):
            print "Bạn hỏi về kiểm soát viên."
            print "Xin mời lựa chọn"
            print "\t1. Tiêu chuẩn và điều kiện đối với Kiểm soát viên"
            print "\t2. Trách nhiệm của Kiểm soát viên"
            print "\t3. Miễn nhiệm, cách chức Kiểm soát viên"
            print "\t4. Khac"

            choiceNumber = int(raw_input("Lựa chọn của bạn? "))
            if choiceNumber == 1:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 103, columnArticle)
            elif choiceNumber == 2:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 106, columnArticle)
            elif choiceNumber == 3:
                print ib.gen_article_from_prediction(lawInEnterprise_xlsx, 107, columnArticle)
            else:
                print final_answer
            break

        print final_answer
        break


# Question level 01

print "Xin mời lựa chọn"
print "\t1. Công ty trách nhiệm hữu hạn một thành viên"
print "\t2. Công ty trách nhiệm hữu hạn hai thành viên trở lên"
print "\t3. Doanh nghiệp nhà nước"
print "\t4. Công ty cổ phần"
print "\t5. Khác"
choiceNumber = int(raw_input("Lựa chọn của bạn? "))


# Check the value in level 01
while Switch(choiceNumber):
    if case(1):
        print "Bạn hỏi về công ty trách nhiệm hữu hạn một thành viên."
        # article 73 -> 87
        print "Xin mời lựa chọn"
        print "\t1. Vốn"
        print "\t2. Chủ sở hữu công ty"
        print "\t3. Khác"

        choiceNumber = int(raw_input("Lựa chọn của bạn? "))
        messageForChoice01(choiceNumber)

        break

    if case(3):
        print "Bạn hỏi về doanh nghiệp nhà nước."
        # article 88 -> 109
        print "Xin mời lựa chọn"
        print "\t1. Hội đồng thành viên:"
        print "\t2. Kiểm soát viên"
        print "\t3. Khác"

        choiceNumber = int(raw_input("Lựa chọn của bạn? "))
        messageForChoice02(choiceNumber)

        break

    print final_answer
    break

