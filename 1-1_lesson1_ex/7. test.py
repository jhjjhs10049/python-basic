# 문제22
# name = "홍길동"
# age = 20
# height = 175.5

# print(f"이름: {name}\n나이: {age}\n키: {height}")

#문제 23
# price = 15000
# quantity = 3
# amount_price = price * quantity

# print(f"상품 단가: {price}원\n구매수량: {quantity}개\n총 금액: {amount_price}원")

#문제 24
# a = 42
# b = 3.14
# c = "Python"
# d = True

# print(f"{a} -> {type(a).__name__}\n{b} -> {type(b).__name__}\n{c} -> {type(c).__name__}\n{d} -> {type(d).__name__}")

#문제 25

# kor_score = int(input("국어점수를 입력해주세요 : "))
# eng_score = int(input("영어점수를 입력해주세요 : "))
# math_score = int(input("수학점수를 입력해주세요 : "))

# print(f"\n=== 성적 계산기 ===")
# print(f"국어점수: {kor_score}")
# print(f"영어점수: {eng_score}")
# print(f"수학점수: {math_score}")
# print(f"--------------------")

# sum_score = kor_score+eng_score+math_score
# average_score = sum_score / 3

# print(f"총점: {sum_score}")
# print(f"평균: {round(average_score,2)}")

#문제 26
input_seconds = int(input("초를 입력하세요: "))
hours = input_seconds // 3600
minutes = (input_seconds % 3600) // 60
seconds = input_seconds % 60 

print(f"{input_seconds}초 = {hours}시간 {minutes}분 {seconds}초")

