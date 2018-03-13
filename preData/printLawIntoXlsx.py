#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import json
import pprint
import re
import codecs
from openpyxl import Workbook


lawInEnterprise_txt = 'lawInEnterprise.txt'
lawInEnterprise_xlsx = 'lawInEnterprise.xlsx'

# only apply for LawInEnterprise.txt
def print_LawInEnpterprise_Into_Xlsx(inp_txt):
    data = ''
    lines = []

    with open(inp_txt, 'r') as myfile:
        for line in myfile:
            if (line[0] == '$'):
                line += '#'
            lines.append(line)
    for line in lines:
        data += line
    articles = data.split('$$$$')

    book = Workbook()
    sheet = book.active

    sheet.append(("STT", "Nội dung"))
    number = 0
    for i in range(1, 214):
        number += 1
        content = articles[i].split('#')
        mainContent = content[0].split('. ')
        row = (number, mainContent[0] + ': ' + mainContent[1] + content[1])
        sheet.append(row)
    book.save(lawInEnterprise_xlsx)
    return 0
# DONE


if __name__ == "__main__":
    print_LawInEnpterprise_Into_Xlsx(lawInEnterprise_txt)


