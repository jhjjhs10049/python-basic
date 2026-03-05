# 환율 설정
'''USD_RATE = 1300  # 1달러 = 1300원
JPY_RATE = 900   # 100엔 = 900원
EUR_RATE = 1400  # 1유로 = 1400원'''

# 여기에 코드를 작성하세요
'''
usd_rate = float(1400)
jpy_rate = float(1250/100)
eur_rate = float(1400)
'''

print("환율 계산기입니다. (USD,JPY,EUR 출력)")
kor_mount = float(input("원하시는 KOR 금액을 입력해주세요 : "))

usd_rate = round(kor_mount/1400,2)
jpy_rate = round(kor_mount/(1250/100),2)
eur_rate = round(kor_mount/1600,2)

print(f"\n해당 금액의 미국환율 : {usd_rate}\n해당 금액의 일본환율 : {jpy_rate}\n해당금액의 유럽환율 : {eur_rate} ")

