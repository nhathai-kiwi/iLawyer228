#!/usr/bin/env python
# -*- coding: utf-8 -*-

final_answer = 'Đề nghị tư vấn luật sư để có câu trả lời chính xác'

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# Switch-case
class Switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == Switch.value for arg in args))

# Question level 01

print "Xin mời lựa chọn"
print "1. CÔNG TY TRÁCH NHIỆM HỮU HẠN MỘT THÀNH VIÊN"
print "2. CÔNG TY TRÁCH NHIỆM HỮU HẠN HAI THÀNH VIÊN TRỞ LÊN"
print "3. DOANH NGHIỆP NHÀ NƯỚC"
print "4. CÔNG TY CỔ PHẦN"
print "5. KHÁC"

value = 5

# Check the value in level 01
while Switch(value):
    if case(1):
        print "Ban hoi ve cong ty trach nhiem huu han mot thanh vien."

        break
    if case(3):
        print "Ban hoi ve Doanh nghiep nha nuoc."

        break

    print final_answer
    break

