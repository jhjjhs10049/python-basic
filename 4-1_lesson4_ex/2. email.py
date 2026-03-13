# 이메일 주소 분석 프로그램
print("=== 이메일 주소 분석기 ===")

email = input("이메일 주소를 입력하세요: ")

# @ 기호의 위치 찾기
at_position = email.find("@")

# 아이디와 도메인 분리
user_id = email[:at_position]
domain = email[at_position + 1:]

# 도메인에서 최상위 도메인 추출
dot_position = domain.rfind(".")  # 마지막 점의 위치(메일에선 .이 1개 밖에 없기에 rfind나 find나 결과는 동일)
top_level_domain = domain[dot_position + 1:]

# 결과 출력
print(f"\n전체 이메일: {email}")
print(f"아이디: {user_id}")
print(f"도메인: {domain}")
print(f"최상위 도메인: {top_level_domain}")
print(f"이메일 길이: {len(email)}자")