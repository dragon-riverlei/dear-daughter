#!/usr/bin/python2

from xlrd import open_workbook

book = open_workbook('/cygdrive/d/GitHub/dragon-riverlei/dear-daughter/2017_to_primary_school/shanghai_private_primary_schools.xlsx')
sheet = book.sheet_by_index(0)
for row_index in range(2, sheet.nrows):
  for col_index in range(sheet.ncols):
    if(col_index==0 or col_index==1 or col_index==5):
      print sheet.cell(row_index, col_index).value.encode('utf-8')
    else:
      print sheet.cell(row_index, col_index).value


