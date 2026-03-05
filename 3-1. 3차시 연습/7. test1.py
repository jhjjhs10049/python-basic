'''시급, 근무 시간, 야간 근무 시간을 입력받아 총 급여를 계산하는 프로그램을 작성하세요. 야간 근무는 시급의 1.5배를 적용합니다.'''
'''
hourly_wage = int(input("시급: "))
regular_hours = int(input("일반 근무 시간: "))
night_hours = int(input("야간 근무 시간: "))'''

hourly_wage = int(input("시급: "))
regular_hours = int(input("일반 근무 시간: "))
night_hours = int(input("야간 근무 시간: "))

total_wage = (hourly_wage * regular_hours) + (hourly_wage * 1.5 * night_hours)
print(f"일반근무시간 {regular_hours}시간, 야간근무시간 {night_hours}시간 으로 총 급여는 {total_wage}원 입니다.")