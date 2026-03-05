# 성적 평균 계산 프로그램
print("=== 성적 평균 계산기 ===")

# 학생 정보 입력
student_name = input("학생 이름: ")

# 점수 입력 (문자열을 정수로 변환)
korean = int(input("국어 점수: "))
english = int(input("영어 점수: "))
math = int(input("수학 점수: "))

# 평균 계산 (정수를 실수로 변환하여 정확한 평균 계산)
total = korean + english + math
average = total / 3  # 자동으로 실수 결과 반환

# 결과 출력
print(f"\n{student_name} 학생의 성적")
print(f"국어: {korean}점")
print(f"영어: {english}점")
print(f"수학: {math}점")
print(f"총점: {total}점")
print(f"평균: {average:.2f}점")  # 소수점 둘째 자리까지 표시