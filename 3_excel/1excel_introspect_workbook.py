import sys

from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)  # 엑셀 파일의 시트 개수를 출력
for worksheet in workbook.sheets():
    # 시트의 이름, 행 개수, 열 개수를 출력한다.
    print('Worksheet name:', worksheet.name, '\tRows:', worksheet.nrows, '\tColumns:', worksheet.ncols)
