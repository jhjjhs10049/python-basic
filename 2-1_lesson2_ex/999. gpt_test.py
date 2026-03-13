# 자신의 이름, 나이, 키(cm) 를 각각 변수에 저장하고, 아래 형식으로 출력하는 코드 작성해줘.

# 이름: 홍길동
# 나이: 20살
# 키: 175.5cm

# name = "홍길동"
# age = 20
# height = 175.5

# print(f"이름 : {name}")
# print(f"나이 : {age}살")
# print(f"키 : {height}cm")

#==================================================================================

# 변수 price = 15000, quantity = 3일 때
# 총 금액을 계산해서 아래처럼 출력하는 코드 작성해줘.

# 상품 단가: 15000원
# 구매 수량: 3개
# 총 금액: 45000원

# price = 15000
# quantity = 3

# print(f"상품 단가 : {price}원")
# print(f"구매 수량 : {quantity}개")
# print(f"총 금액 : {price * quantity}원")

#==================================================================================

# 아래 변수들의 데이터 타입을 type() 함수로 확인하여 출력하시오.

# a = 42
# b = 3.14
# c = "Python"
# d = True

# print(f"{type(a).__name__}")
# print(f"{type(b).__name__}")
# print(f"{type(c).__name__}")
# print(f"{type(d).__name__}")

#==================================================================================

# 사용자로부터 국어, 영어, 수학 점수를 input()으로 입력받아
# 총점과 평균을 계산하고,
# 평균은 소수점 첫째 자리까지 출력하는 프로그램을 작성해줘.

# kor_score = int(input("국어 점수를 입력하세요 : "))
# eng_score = int(input("영어 점수를 입력하세요 : "))
# math_score = int(input("수학 점수를 입력하세요 : "))

# sum_score = kor_score + eng_score + math_score
# average_score = round(sum_score / 3, 1)

# print(f"총점 : {sum_score}점")
# print(f"평균 : {average_score}점")

#==================================================================================

# 사용자로부터 초(seconds) 를 입력받아
# 시, 분, 초로 변환하여 출력하는 프로그램을 작성해줘.

# 예시:

# 초를 입력하세요: 3725
# 3725초 = 1시간 2분 5초

input_seconds = int(input("초 를 입력해주세요 : "))

hours = input_seconds // 3600
minutes = input_seconds % 3600 // 60
seconds = input_seconds % 60

print(f"{input_seconds}초 = {hours}시간 {minutes}분 {seconds}초")



