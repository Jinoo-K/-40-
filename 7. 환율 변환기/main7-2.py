# pip install currencyconverter

from currency_converter import CurrencyConverter

cc = CurrencyConverter("http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip")        # 최신 환율 정보 업데이트
print(cc.convert(1,"USD","KRW"))        # 1달러를 원화로 출력