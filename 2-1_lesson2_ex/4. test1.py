'''사용자로부터 이름, 키(cm), 몸무게(kg)를 입력받아 BMI(체질량지수)를 계산하는 프로그램을 작성하세요. 
BMI 공식은 다음과 같습니다:
BMI = 몸무게(kg) ÷ (키(m))²
'''
print("BMI(체질량지수) 계산 프로그램입니다.")
user_name=input("이름을 입력해주세요 (글자) : ")
user_height=int(input("키를 입력해주세요 (정수) : "))
user_kg=float(input("몸무게를 입력해주세요 (소수점) : "))
user_bmi=round(user_kg / ((user_height / 100) ** 2),2)
print(f"{user_name}님의 BMI = {user_bmi}")