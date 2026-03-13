# 회원 정보 입력 프로그램
print("=== 회원 정보 입력 ===")

# 회원 정보 저장
member_id = 1001
member_name = "홍길동"
age = 25
height = 178.5
weight = 72.3
is_premium = True

# 정보 출력
print(f"회원 번호: {member_id} (타입: {type(member_id).__name__})")
print(f"이름: {member_name} (타입: {type(member_name).__name__})")
print(f"나이: {age} (타입: {type(age).__name__})")
print(f"키: {height}cm (타입: {type(height).__name__})")
print(f"몸무게: {weight}kg (타입: {type(weight).__name__})")
print(f"프리미엄 회원: {is_premium} (타입: {type(is_premium).__name__})")