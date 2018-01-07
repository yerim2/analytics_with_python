# 2.CSV 파일

**CSV**(comma-separated values) 파일 포맷은 숫자나 문자열로 구성된 표 형태의 데이터가 일반 텍스트로 저장된다. 

#### 예시

| ID | 은행명 | 계좌주 | 계좌번호 |
| --- | --- | --- | --- |
| 1 | 신한은행 | 이연태 |  111-1111-1111 |
| 2 | 국민은행 | 김준호 | 222-2222-2222 |
| 3 | 기업은행 | 이남홍 | 333-3333-3333 |
| 4 | 우리은행 | 김현주 | 444-4444-4444 |
| 5 | 농협은행 | 박호성 | 555-5555-5555 |

위와 같은 표 형태의 데이터의 csv 파일은 아래와 같다. 

```
# csv 파일

ID,은행명,계좌주,계좌번호
1,신한은행,이연태,111-1111-1111
2,국민은행,김준호,222-2222-2222
3,기업은행,이남홍,333-3333-3333
4,우리은행,김현주,444-4444-4444
5,농협은행,박호성,555-5555-5555
```

각 행마다 `,`로 구분되어 데이터가 저장된다.   
CSV 파일에서 구분자로 사용된 `,`는 엑셀 파일의 열에 해당한다.

# 2.2 CSV 파일 읽고 쓰기(파트1)

## 2.2.1 csv 모듈을 사용하지 않는 기본 파이썬 코드

```python
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline()
        header_list = header.strip().split(',')
        filewriter.write(','.join(map(str, header_list))+'\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            filewriter.write(','.join(map(str, row_list))+'\n')
```
- CSV 파일을 한줄씩 읽으면서 `,`를 기준으로 값을 나누어 리스트로 변환한다. 
- 리스트로 변환된 행의 데이터를 `,`로 구분된 문자열로 변환한 후 결과 파일에 쓴다.

### sys 모듈
- sys는 파이썬 기본 내장 모듈이다.
- 명령줄에서 추가적으로 입력된 인수를 스크립트로 넘겨준다.
- sys의 argv인수를 이용하면 명령줄에서 입력된 인수를 리스트 자료형으로 받을 수 있다.

```
python script_name.py "C:\path\to\unput_file.csv" "C:\path\to\output_file.csv"
```
명령줄에서 위와 같이 입력했다면 sys.argv는 다음과 같은 리스트 자료형이 된다.

```
sys.argv = ['script_name.py,' 'C:\path\to\unput_file.csv', 'C:\path\to\output_file.csv']
```

따라서   
sys.argv[0]은 `script_name.py`  
sys.argv[1]은 `"C:\path\to\unput_file.csv"`  
sys.argv[2]은 `"C:\path\to\output_file.csv"`
값을 갖게 된다.
 

[sys - 파이썬 문서](https://docs.python.org/3/library/sys.html#sys.argv)


## 2.2.2 팬더스

```python
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame.to_csv(output_file, index=False)
```
`DataFrame`: 팬더스의 기본 데이터 구조이며 데이터를 `표` 형태로 저장한다.  
데이터프레임은 팬더스 패키지의 자료형이기 떄문에 팬더스 패키지를 임포트 해야 사용할 수 있다. 

`read_csv()`: csv 파일을 DataFrame으로 읽어들인다.  
`to_csv()`: DataFrame을 csv 파일로 쓴다.

[DataFrame - 팬더스 문서](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)

# 2.3 기본 문자열 파싱이 실패하는 경우
CSV는 각 열의 구분을 `,`를 사용하기 때문에 열의 값 내부에 `,`가 포함되어 있는 경우에는 문자열 파싱에 실패할 수 있다. 

`2.2.1 csv 모듈을 사용하지 않는 기본 파이썬 코드` 에서 사용한 코드는 `,`를 기준으로 각 행의 데이터를 파싱하고 있기 때문에 데이터 자체에 `,`가 있다면 올바르게 파싱되지 않을 것이다. 

#### 예시

```
# csv 파일

1, $860, 111-1111-1111
2, $920, 222-2222-2222
3, $4,250, 333-3333-3333
```
위와 같은 파일을 2.2.1에 사용한 코드로 파싱을 하게 된다면 다음과 같은 결과를 얻을 것이다.

```
[1, $860, 111-1111-1111]
[2, $920, 222-2222-2222]
[3, $4, 250, 333-3333-3333]
```

`,`가 포함된 값을 처리하기 위해 파이썬에 내장된 `csv`모듈을 사용할 수 있다.

# 2.4 CSV 파일 읽고 쓰기(파트2)
## 2.4.1 기본 파이썬(csv 모듈 사용)
파이썬에 내장된 csv모듈을 사용하면 데이터 값에 포함된 쉼표 및 기타 복잡한 패턴을 정확하게 처리할 수 있다.

```python
import csv
import sys

print(sys.argv)
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            filewriter.writerow(row_list)
```
- csv 모듈의 reader() 함수로 입력된 파일을 읽는 객체를 생성한다.  
- csv 모듈의 writer() 함수로 출력 파일에 사용할 객체를 생성한다.  
- reader, writer 함수의 두번째 인수인 delimiter는 기본값을 `,`로 갖고 있다. 구분자가 `,`가 아닌 다른 기호라면 해당 기호를 인수로 지정해야한다.
- writerow() 함수를 사용하면 각 행의 값을 리스트 자료형으로 출력 파일에 쓴다. 

[csv - 파이썬 문서](https://docs.python.org/3/library/csv.html)

# 2.5 특정 행을 필터링하기
특정 행을 필터링 하기 위해서 다음과 같은 과정을 거친다.

1. 필터링할 조건을 정의한다. 
2. 조건에 부합하는 행인지 판별한다. 
3. 조건을 충족하는 경우, 해당하는 행에 원하는 행동을 적용한다.(예: 파일에 쓰기, 연산하기 등)


```
# 예제 CSV 파일

Supplier Name,Invoice Number,Part Number,Cost,Purchase Date
Supplier X,001-1001,2341,$500.00,1/20/14
Supplier X,001-1001,5467,$750.00,1/20/14
Supplier Y,50-9501,7009,$250.00,1/30/14
Supplier Y,50-9505,6650,$125.00,2/3/14
Supplier Z,920-4803,3321,$615.00,2/3/14
Supplier Z,920-4806,3321,$615.00,2/24/14
```

## 2.5.1. 특정 조건을 충족하는 행의 필터링

### 조건

- Supplier Name이 Supplier Z 인 모든 행
- Cost가 $600.00 이상인 모든 행

### 기본 파이썬

```python
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            supplier = str(row_list[0]).strip()
            cost = str(row_list[3]).strip('$').replace(',', '')
            if supplier == 'supplier Z' or float(cost) > 600.0:
                filewriter.writerow(row_list)
```

- 각 행을 돌면서 supplier와 cost의 값을 구한다.
- supplier가 'Supplier Z'이거나, cost가 600이상인 경우에 해당하는 행을 `csv_out_file` 파일에 쓴다.

### 팬더스

```python
import sys

import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[
                                   (data_frame['Supplier Name'].str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
data_frame_value_meets_condition.to_csv(output_file, index=False)
```
- `.read_csv()` : `data_frame` 변수에 input_file.csv를 DataFrame 형태의 데이터로 읽어 저장한다.
- `data_frame['Cost']`를 재정의: `Cost` 열에 해당하는 데이터에 `$` 기호를 제거 하고 `float` 타입으로 형태 변환을 한다.	
- `.loc`함수를 이용하여 필터링 조건을 작성한다.
	-  `.contains(pattern)`: 문자열이 pattern을 포함하는지 여부를 판단한다.

> `data_frame['Cost']` 의 타입은 `Series`이다. 이를 문자열로 취급하여 핸들링하려면 `.str`을 붙여 제공되는 여러가지 함수를 사용할 수 있다.  
> 
- [Series](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#series)  
- [string handling](https://pandas.pydata.org/pandas-docs/stable/api.html#string-handling)  


### 결과

```
# output CSV 파일

Supplier Name,Invoice Number,Part Number,Cost,Purchase Date
Supplier X,001-1001,5467,$750.00,1/20/14  # Cost가 600 이상
Supplier Z,920-4803,3321,$615.00,2/3/14  # Supplier Name에 Z가 포함됨
Supplier Z,920-4806,3321,$615.00,2/24/14  # Supplier Name에 Z가 포함됨
```

## 2.5.2 특정 집합의 값을 포함하는 행의 필터링

### 조건
- 구매일자가 {'1/20/14', '1/30/14'} 집합의 원소인 경우에 해당하는 모든 행

### 기본 파이썬

```python
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)
```

- 필터링 조건에 해당하는 집합을 정의한다. (important_dates에 특정 날짜를 담은 리스트를 할당)  
- `a_date = row_list[4]`: 구매일자의 데이터는 행의 4번째 인덱스에 해당한다.
- `a_date`가 `important_dates`의 원소에 포함된다면 `csv_out_file` 파일에 해당 행을 쓴다.


### 팬더스

```python
import sys

import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

important_dates = ['1/20/14', '1/30/14']
date_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]

date_frame_value_in_set.to_csv(output_file, index=False)
```

- 필터링 조건에 해당하는 집합을 정의한다.
- `.loc`함수를 이용하여 필터링 조건을 작성한다.
	-  `.isin(values)` : DataFrame의 요소가 values에 포함되는지 여부를 판단한다.

### 결과

```
# 결과 CSV 파일

Supplier Name,Invoice Number,Part Number,Cost,Purchase Date
Supplier X,001-1001,2341,$500.00,1/20/14
Supplier X,001-1001,5467,$750.00,1/20/14
Supplier Y,50-9501,7009,$250.00,1/30/14
```

## 2.5.3 패턴/정규 표현식을 활용한 필터링 
특정한 패턴과 일치하거나 패턴이 포함된 행을 선택하는 방법이다. 

> 예를 들면...  
> - Invoice Number 열의 데이터 값이 001- 로 시작하는 행을 모두 선택하고 싶을 때  
> - Supplier Name 열의 데이터 값에 Y가 포함되는 행을 모두 선택하고 싶을 때

### 조건
Invoce Number 열의 데이터 값이 `001-` 로 시작하는 모든 행

### 기본 파이썬

```python
import csv
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_outfile:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_outfile)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)
```

- pattern을 정의한다. : 정규표현식을 사용하여 `001-`로 시작하는 패턴을 정의하였다.
- `invoice_number = row_list[1]`: Invoice Number 데이터는 행의 1번째 인덱스에 해당한다.
	- `pattern.search(invoice_number)`: re 모듈의 .search 메서드를 이용하여 invoice_number의 값에서 패턴을 찾는다.
	- 정의된 패턴이 invoice_number의 값에 있다면 `csv_outfile`에 쓴다. 

### 팬더스

```python
import sys

import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number'].str.startswith('001-'), :]
data_frame_value_matches_pattern.to_csv(output_file, index=False)
```

- `.startswith(pattern)`: pattern으로 시작하는 문자열인지 판단한다.

> [.startswith()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.startswith.html)

# 2.6 특정 열 선택하기
- 열의 인덱스 값을 사용하는 방법
- 열의 헤더를 사용하는 방법

## 2.6.1 열의 인덱스 값을 사용하여 특정 열을 선택하는 방법

### 언제 사용하는것이 좋을까?
- 열의 인덱스 값을 쉽게 식별할 수 있을 때  
- 여러개의 입력 파일을 처리할 때  
- 모든 입력 파일에서 열의 위치가 변경되지 않을 때

### 기본 파이썬
`column_by_index.py`

```python
#!/usr/bin/env python3

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_colums = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output= []
            for index_value in my_colums:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)
```

**스크립트 실행**  

```
python column_by_index.py supplier_data.csv output_index.csv
```

1. 선택하고자 하는 열의 index값을 리스트로 `my_columns`라는 변수에 할당
2. `filereader` 반복문을 돌면서 다음을 반복한다.
	1. `row_list_output`이라는 빈 리스트를 생성
	2. `my_columns`를 for문을 돌면서, 현재의 인덱스에 해당하는 값을 `row_list_output`에 할당
	3. `my_columns`를 도는 for문이 끝나면 `row_list_output`을 출력 파일에 쓰기


### 팬더스 

`pandas_column_by_index.py`

```python
#!/usr/bin/env python3

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
data_frame_column_by_index.to_csv(output_file, index=False)
```

**스크립트 실행**  

```
python pandas_column_by_index.py supplier_data.csv pandas_output_index.csv
```


## 2.6.2 열의 헤더를 사용하여 특정 열을 선택하는 방법

### 언제 사용하는것이 좋을까?
- 열 헤더를 식별하기 쉬울 때
- 처리할 파일들의 열의 헤더는 같으나 열의 위치가 다를 때

### 기본 파이썬
`column_by_header.py`

```python
#!/usr/bin/env python3

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', new_line='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        filewriter.writerow(my_columns)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value[)
            filewriter.writerow(row_list_output)
```

**스크립트 실행**  

```
python column_by_header.py supplier_data.csv output_header.csv
```

1. 선택하고자 하는 열의 헤더를 리스트로 `my_columns`라는 변수에 할당
2. 헤더의 길이만큼 반복하면서 헤더가 `my_columns`에 들어있다면, 해당 index값을 `my_columns_index`에 할당
3. `filereader`를 for문을 돌면서 다음을 반복한다.
	1. `row_list_output`이라는 빈 리스트를 생성
	2. `my_columns`를 for문을 돌면서, 현재의 인덱스에 해당하는 값을 `row_list_output`에 할당
	3. `my_columns`를 도는 for문이 끝나면 `row_list_output`을 출력 파일에 쓰기

헤더로 필요한 인덱스 리스트를 구한 후, index로 선택하는 방법을 사용하는 방식이다.


### 팬더스 
`pandas_column_by_header.py`

```python
#!/usr/bin/env python3

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]

data_frame_column_by_name.to_csv(output_file, index=False)
```

**스크립트 실행**  

```
python pandas_column_by_header.py supplier_data.csv pandas_output_header.csv
```

## pandas로 데이터 선택하기

참고영상: [How do I use .loc, .iloc, .ix?](https://www.youtube.com/watch?v=xvpNA7bC8cs) 

### data frame의 슬라이싱

1. 특정 열에 해당하는 데이터 가져오기  
	
	```
	data_frame['column_name']
	```

2. 특정 행의 범위에 해당하는 데이터 가져오기(인덱스 이용)  
	
	```
	data_frame[start_index:end_index]
	```    
	> `start_index` 부터 `end_index` 앞의 범위 까지 데이터를 가져온다. `end_index`는 포함하지 않는다.   
	

### `.iloc`
정수 값(위치) 이용해 데이터를 선택할 수 있다.

```
# 1, 3, 5번째 열에 해당하는 모든 데이터를 가져온다.
data_frame.iloc[:, [1, 3, 5]]

# 0번째 부터 4번째 까지의 열에 해당하는 모든 데이터를 가져온다.
data_frame.iloc[:, 0:5]

# 0번째 부터 2번째 까지의 행에서 5번째 부터 9번째 까지의 열에 해당하는 데이터를 가져온다.
data_frame.iloc[0:3, 5:10]
```

### `.loc`
label을 이용하여 데이터를 선택할 수 있다. 

```
# A열에 해당하는 모든 데이터를 가져온다.
data_frame.loc[:, 'A']

# 0번째부터 4번째 까지의 행에서 A, C 열에 해당하는 데이터를 가져온다.
data_frame.loc[0:5, ['A', 'C']]

# 0번째 부터 4번째 까지의 행에서 A부터 F열에 해당하는 데이터를 가져온다.
data_frame.loc[0:5, 'A':'F']
```

### `.ix` 
혼합 된 위치 및 label 기반의 색인을 다룰 때 매우 유용하지만, 이러한 예외적인 상황이 아니라면 명시적으로 `.loc` 또는 `.iloc`을 사용하는 것이 좋다. 

```
# 1번째의 행에서 Cost 열에 해당하는 데이터를 가져온다.
data_frame.ix[1, 'Cost']

# 0번째 부터 2번째 까지의 행에서, 0번째 부터 1번째 까지의 열에 해당하는 데이터를 가져온다.
# .ix에서 행의 슬라이스 end_position을 포함하기 때문에 0, 1, 2 번째의 행이 선택된다. 
data_frame.ix[0:2, 0:2]
```

[.ix - 팬더스 문서](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.ix.html)






