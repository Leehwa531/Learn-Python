# 사용자 입력
name = input("이름을 입력하세요: ")
gender = input("성별을 입력하세요 (남자/여자): ")
waist = float(input("허리둘레(cm)를 입력하세요: "))
hip = float(input("엉덩이 둘레(cm)를 입력하세요: "))
height = float(input("신장(cm)를 입력하세요: "))
weight = float(input("체중(kg)을 입력하세요: "))

# WHP와 BMI 계산
WHP = waist / hip
BMI = weight / ((height / 100) ** 2)

# 비만 여부 판단
if gender == "남자" and WHP > 0.9:
    obesity = "비만"
elif gender == "여자" and WHP > 0.85:
    obesity = "비만"
else:
    obesity = "정상"

# BMI 판정
if BMI < 20:
    bmi_result = "재측정"
elif 20 <= BMI <= 24.9:
    bmi_result = "정상"
elif 25 <= BMI <= 29.9:
    bmi_result = "과체중"
else:
    bmi_result = "비만"

# 결과 출력
print(f"{name}님의 WHP는 {WHP:.2f}, BMI는 {BMI:.2f}입니다.")
print(f"성별에 따른 비만 여부: {obesity}, BMI 결과: {bmi_result}")
