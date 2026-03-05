# 주요 이스케이프 문자
# print("첫 번째 줄\n두 번째 줄")  # \n: 줄바꿈
# print("탭\t간격\t조정")  # \t: 탭
# print("큰따옴표 출력: \"Hello\"")  # \": 큰따옴표
# print("작은따옴표 출력: \'Hi\'")  # \': 작은따옴표
# print("백슬래시 출력: \\")  # \\: 백슬래시

# 문자열 슬라이싱
text = "Hello, Python!"

# 기본 슬라이싱
print(text[0:5])    # Hello (인덱스 0부터 4까지)
print(text[7:13])   # Python (인덱스 7부터 12까지)

# 시작 또는 끝 생략
print(text[:5])     # Hello (처음부터 4까지)
print(text[7:])     # Python! (7부터 끝까지)
print(text[:])      # Hello, Python! (전체)

# 음수 인덱스 사용
print(text[-7:])    # Python! (뒤에서 7번째부터 끝까지)
print(text[:-2])    # Hello, Python (마지막 2문자 제외)

# 간격 지정
print(text[::2])    # Hlo yhn (2칸씩 건너뛰기)
print(text[::-1])   # !nohtyP ,olleH (문자열 뒤집기)