# 학점 판정 시스템
print("=== 학점 판정 시스템 ===")

# 학생 정보 입력
attendance_rate = int(input("출석률을 입력하세요 (0-100): "))
exam_score = int(input("시험 점수를 입력하세요 (0-100): "))

# 합격 조건: 출석률 80% 이상 AND 시험 점수 60점 이상
passed = attendance_rate >= 80 and exam_score >= 60

# 우수 학생: 출석률 95% 이상 AND 시험 점수 90점 이상
excellent = attendance_rate >= 95 and exam_score >= 90

# 재수강 대상: 출석률 80% 미만 OR 시험 점수 60점 미만
retake = attendance_rate < 80 or exam_score < 60

# 결과 출력
print(f"\n출석률: {attendance_rate}%")
print(f"시험 점수: {exam_score}점")
print(f"합격 여부: {passed}")
print(f"우수 학생: {excellent}")
print(f"재수강 대상: {retake}")

if excellent:
    print("축하합니다! 우수 학생입니다.")
elif passed:
    print("합격입니다.")
else:
    print("재수강이 필요합니다.")