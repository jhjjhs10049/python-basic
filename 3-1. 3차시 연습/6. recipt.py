# 영수증 출력 프로그램
print("=== 영수증 생성기 ===")

# 상점 정보
store_name = "python mart"
store_address = "daegu, dalseo-gu, 123-45"

# 구매 정보 입력
product_name = input("product_name : ")
unit_price = int(input("product_price : "))
quantity = int(input("quantity : "))

# 계산
total_price = unit_price * quantity

# 영수증 출력
line = "=" * 50
print("\n" + line)
print(store_name.center(50))  # 중앙 정렬
print(store_address.center(50))
print(line)
print("product_name".ljust(20) + "quantity".rjust(10) + "unit_price".rjust(20))
print(line)
print(product_name.ljust(20) + str(quantity).rjust(10) + f"{unit_price:,}won".rjust(20))
print(line)
print("total_price".ljust(30) + f"{total_price:,}won".rjust(20))
print(line)
print("\nthank you!".center(50))
print(line)