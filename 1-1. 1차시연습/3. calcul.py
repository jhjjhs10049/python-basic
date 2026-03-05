# 두 숫자를 더하는 간단한 계산기
print("=== 간단한 덧셈 계산기 ===")

# 첫 번째 숫자 입력받기
num1 = input("첫 번째 숫자를 입력하세요: ")
num1 = int(num1)  # 문자열을 정수로 변환

# 두 번째 숫자 입력받기
num2 = input("두 번째 숫자를 입력하세요: ")
num2 = int(num2)  # 문자열을 정수로 변환

# 계산 및 결과 출력
result = num1 + num2
print(num1, "+", num2, "=", result)