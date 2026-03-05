# 나이 확인 프로그램
print("=== 나이 확인 시스템 ===")

age = int(input("나이를 입력하세요: "))

# 성인 여부 확인
is_adult = age >= 18

print(f"\n입력하신 나이: {age}세")
print(f"성인 여부: {is_adult}")

if is_adult:
    print("성인입니다. 모든 콘텐츠에 접근할 수 있습니다.")
else:
    print("미성년자입니다. 일부 콘텐츠가 제한됩니다.")