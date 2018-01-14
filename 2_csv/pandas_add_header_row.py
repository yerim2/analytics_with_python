import sys

import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'cost', 'Purchase Date']

# read_csv()에서 names는 헤더 리스트를 받는다. 파일에 헤더가 없는 경우 header=None 을 명시적으로 적어주어야함.
data_frame = pd.read_csv(input_file, header=None, names=header_list)
data_frame.to_csv(output_file, index=False)

