'''
연도를 입력받아 윤년인지 판별하는 프로그램을 작성하세요. 윤년 조건은 다음과 같습니다:

4로 나누어떨어지고
100으로 나누어떨어지지 않거나
400으로 나누어떨어지는 해
'''


# 힌트
year = int(input("연도를 입력하세요: "))

# 윤년 조건 확인
is_leap_year = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

if is_leap_year == True:
    print(f"{year}년은 윤년입니다.")
else:    
    print(f"{year}년은 윤년이 아닙니다.")