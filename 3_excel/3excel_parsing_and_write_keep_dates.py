import sys
from datetime import date

from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for col_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index, col_index) == 3:  # cell type 3번은 날짜 셀을 의미한다.
                # xldate_as_tuple(값, datemode) : 엑셀 시트에 설정된 datemode에 따라 날짜 값을 변환한다.
                # (2013, 1, 1, 0, 0, 0) 과 같이 튜플 형태로 날짜값을 얻게된다. (년도, 월, 일, 시, 분, 초)
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
                print('org_data: ', date_cell)

                # date((년도, 월, 일)).strftime(날짜 표시 형식) : date_cell에서 년도, 월, 일 값을 월/일/년도 형식으로 변환한다.
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                print('formatting: ', date_cell)

                output_worksheet.write(row_index, col_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                output_worksheet.write(row_index, col_index, non_date_cell)

output_workbook.save(output_file)
