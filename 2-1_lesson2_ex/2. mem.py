# 쇼핑몰 가격 계산 프로그램
print("=== 온라인 쇼핑 계산기 ===")

# 사용자 입력 (input()은 항상 문자열 반환)
product_name = input("상품명을 입력하세요: ")
price_input = input("상품 가격을 입력하세요: ")
quantity_input = input("구매 수량을 입력하세요: ")

# 문자열을 숫자로 변환
price = int(price_input)
quantity = int(quantity_input)

# 총 금액 계산
total_price = price * quantity

# 결과 출력
print("\n=== 구매 내역 ===")
print(f"상품명: {product_name}")
print(f"단가: {price:,}원")
print(f"수량: {quantity}개")
print(f"총 금액: {total_price:,}원")