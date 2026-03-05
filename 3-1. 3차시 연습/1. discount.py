# 쇼핑몰 할인 계산 프로그램
print("=== 쇼핑몰 할인 계산기 ===")

# 상품 정보 입력
original_price = int(input("원가를 입력하세요: "))
discount_rate = int(input("할인율을 입력하세요 (예: 20): "))

# 할인 금액 계산
discount_amount = original_price * discount_rate / 100

# 최종 가격 계산
final_price = original_price - discount_amount

# 결과 출력
print(f"\n원가: {original_price:,}원")
print(f"할인율: {discount_rate}%")
print(f"할인 금액: {discount_amount:,.0f}원")
print(f"최종 가격: {final_price:,.0f}원")