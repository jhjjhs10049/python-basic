# 이름 카드 출력 프로그램
print("=== 이름 카드 생성기 ===")

# 정보 입력
name = input("이름: ")
company = input("회사명: ")
position = input("직책: ")
phone = input("전화번호: ")
email = input("이메일: ")

# 카드 너비 설정
width = 40
line = "=" * width

# 이름 카드 출력
print("\n" + line)
print(name.upper().center(width))  # 이름을 대문자로 중앙 정렬
print(position.center(width))  # 직책 중앙 정렬
print(line)
print(f"회사: {company}")
print(f"전화: {phone}")
print(f"이메일: {email}")
print(line)

# 추가 정보
print(f"\n이름 길이: {len(name)}자")
print(f"이메일 도메인: {email.split('@')[1]}")
print(f"이니셜: {name[0].upper()}")