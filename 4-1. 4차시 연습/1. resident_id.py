# 주민등록번호 정보 추출
print("=== 주민등록번호 분석기 ===")

# 주민등록번호 입력 (예: 990101-1234567)
resident_id = input("주민등록번호를 입력하세요 (예: 990101-1234567): ")

# 정보 추출 (슬라이싱 사용)
year = resident_id[0:2]  # 년도 (앞 2자리)
month = resident_id[2:4]  # 월
day = resident_id[4:6]  # 일
gender_code = resident_id[7]  # 성별 코드 (7번째 문자)

# 결과 출력
print(f"\n생년월일: {year}년 {month}월 {day}일")
print(f"성별 코드: {gender_code} (1,3: 남성 / 2,4: 여성)")
print(f"뒷자리: {resident_id[7:]}")