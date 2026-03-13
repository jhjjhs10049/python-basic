# 온라인 쇼핑 최종 금액 계산
print("=== 온라인 쇼핑 결제 계산기 ===")

# 입력
product_price = int(input("상품 가격: "))
quantity = int(input("수량: "))
shipping_fee = int(input("배송비: "))
coupon_discount = int(input("쿠폰 할인액: "))

# 계산 (우선순위에 주의)
subtotal = product_price * quantity  # 상품 금액
total_before_discount = subtotal + shipping_fee  # 배송비 포함
final_price = total_before_discount - coupon_discount  # 쿠폰 할인

# 무료 배송 조건 확인 (50,000원 이상)
if subtotal >= 50000:
    final_price -= shipping_fee
    free_shipping = True
else:
    free_shipping = False

# 결과 출력
print(f"\n상품 금액: {subtotal:,}원")
print(f"배송비: {shipping_fee:,}원")
print(f"쿠폰 할인: {coupon_discount:,}원")
print(f"무료 배송: {free_shipping}")
print(f"최종 결제 금액: {final_price:,}원")