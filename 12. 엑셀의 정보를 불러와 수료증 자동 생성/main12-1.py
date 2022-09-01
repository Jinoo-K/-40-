# pip install openpyxl
# pip install python-docx
# pip install docx2pdf

import pandas as pd     # pandas는 데이터 등을 다루는 유명한 라이브러리임

df = pd.DataFrame([["김진우", "1991.01.23", "2022-0001"],
                   ["홍길동", "1991.10.30", "2022-0002"],
                   ["이순신", "1993.03.09", "2022-0003"],
                   ["김시민", "1990.10.23", "2022-0004"],
                   ["강감찬", "1990.03.21", "2022-0005"]])

print(df)
df.to_excel(r"12. 엑셀의 정보를 불러와 수료증 자동 생성\수료증명단.xlsx", index = False, header = False)