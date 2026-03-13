# 게임 점수 계산 프로그램
print("=== 게임 점수 시스템 ===")

# 초기값 설정
score = 0
level = 1

# 게임 진행
print("스테이지 1 클리어!")
score += 100
print(f"현재 점수: {score}")

print("\n보너스 아이템 획득!")
score *= 2  # 점수 2배
print(f"현재 점수: {score}")

print("\n스테이지 2 클리어!")
score += 150
print(f"현재 점수: {score}")

# 레벨업 조건 확인 (300점 이상)
if score >= 300:
    level += 1
    print(f"\n레벨업! 현재 레벨: {level}")

print(f"\n최종 점수: {score}")
print(f"최종 레벨: {level}")