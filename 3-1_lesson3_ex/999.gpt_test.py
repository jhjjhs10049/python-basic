# 원가 50000원인 상품에 20% 할인을 적용한 후, 10% 부가세를 추가한 최종 가격

# basic_price = 50000
# discount_per = 20
# vat_per = 10

# after_discount = int(basic_price - (basic_price * (discount_per/100)))
# after_vat = int(after_discount + (after_discount * (vat_per/100)))

# print(f"원가 : {basic_price}")
# print(f"할인률 : {discount_per}")
# print(f"할인 후 금액 : {after_discount}")
# print(f"부가세 : {vat_per}")
# print(f"부가세 적용 후 금액 : {after_vat}")

#==============================================================================

#total = 0에서 시작해서 +=를 사용해 85, 92, 78을 차례로 누적하고, 총점과 평균을 출력하시오.

# total = 0
# total += 85
# total += 92
# total += 78

# print(f"총점은 {total}점 입니다.")
# print(f"평균은 {total/3}점 입니다.")


#==============================================================================

# 정수 하나를 변수에 저장한 뒤,
# 그 수가 짝수인지 / 홀수인지를 %와 ==를 사용해서 판별하는 코드 작성해줘.

# input_num = int(input("정수를 입력해주세요 : "))
# if input_num%2 == 0:
#     print(f"입력하신 수는 짝수입니다.")
# else:
#     print(f"입력하신 수는 홀수입니다.")

#==============================================================================

# 사용자로부터 원가와 할인율(%)을 input()으로 입력받아
# 할인 금액, 할인 적용가를 계산하고,
# 5만원 이상이면 배송비 무료 / 아니면 3000원 적용해서
# 최종 결제 금액을 출력하는 프로그램을 작성해줘.

# basic_price = int(input("원가를 입력해 주세요 : "))
# discount_per = int(input("할인율(%)를 입력해 주세요 : "))

# after_discount_price = int(basic_price-(basic_price*discount_per/100))

# if after_discount_price >= 50000:
#     delivery_price = 0
# else:
#     delivery_price = 3000

# final_price = after_discount_price + delivery_price

# print(f"원가 : {basic_price}")
# print(f"할인율 : {discount_per}")
# print(f"할인 후 금액 : {after_discount_price}")
# print(f"배송비 : {delivery_price}")
# print(f"최종 금액 : {final_price}")

#==============================================================================

# 사용자로부터 연도를 입력받아 윤년인지 판별하는 프로그램을 작성하시오.
# 조건은 한 줄 조건식으로:

# 4로 나누어떨어지고 100으로는 나누어떨어지지 않거나

# 400으로 나누어떨어지는 해

year = int(input("연도를 입력해주세요 : "))

if year%4 == 0 and not year%100 == 0 or year%400 == 0:
    print(f"윤년입니다.")
else:
    print(f"윤년이 아닙니다.")


