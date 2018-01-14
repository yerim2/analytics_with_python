import sys

import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)

# drop() 메서드를 이용하여 특정 인덱스 값을 갖는 행을 제외한 데이터 프레임을 얻는다.
data_frame = data_frame.drop([0, 1, 2, 16, 17, 18])
# iloc() 메서드를 이용하여 첫 번째 행을 선택하여, data_frame의 컬럼으로 사용한다.
data_frame.columns = data_frame.iloc[0]
# reindex() 메서드를 이용하여 새로운 인덱스를 적용한다.
data_frame = data_frame.reindex(data_frame.index.drop(3))

data_frame.to_csv(output_file, index=False)
