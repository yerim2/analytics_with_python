import sys

from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()  # Workbook 객체를 생성
output_worksheet = output_workbook.add_sheet('jan_2013_output')  # 생성한 Workbook 에 'jan_2013_output'이라는 시트를 추가

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')  # 'january_2013' 이름을 가진 시트를 변수에 할당
    for row_index in range(worksheet.nrows):  # 열의 개수 만큼 반복
        for column_index in range(worksheet.ncols):  # 행의 개수 만큼 반복
            # 결과 파일에 읽어온 데이터를 쓴다.
            # .write(행의 위치, 열의 위치, 값) 로 해당 행, 열에 값을 쓴다.
            # .cell_value(행의 위치, 열의 위치) 로 해당 행,열에 해당하는 값을 가져온다.
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))

# 값을 입력한 output_workbook 을 output_file(결과 파일 path) 에 저장한다.
output_workbook.save(output_file)
