# 질병 코드 딕셔너리
diseases = {
    "K20": "식도염",
    "K21": "위-식도역류병",
    "K22": "식도의 기타 질환",
    "K23": "달리 분류된 질환에서의 식도의 장애",
    "K25": "위궤양",
    "K26": "십이지장궤양",
    "K27": "상세불명 부위의 소화성 궤양",
    "K28": "위공장궤양",
    "K29": "위염 및 십이지장염",
    "K30": "기능성 소화불량",
    "K31": "위 및 십이지장의 기타 질환"
}

# 환자 정보 입력
patients = {}
for i in range(5):
    name = input(f"{i+1}번째 환자 이름을 입력하세요 : ")
    code = input(f"{i+1}번째 환자의 질병 코드를 입력하세요 : ")
    patients[name] = code

# 환자 조회
search_name = input("질병을 조회할 환자 이름을 입력하세요: ")
if search_name in patients:
    disease_code = patients[search_name]
    print(f"{search_name}님의 질병: {disease_code}, 질병명: {diseases[disease_code]}")
else:
    print("해당 환자가 없습니다.")

# 질병 코드로 환자 조회
search_code = input("조회할 질병 코드를 입력하세요: ")
for name, code in patients.items():
    if code == search_code:
        print(f"환자 이름: {name}, 질병 코드: {code}, 질병명: {diseases[code]}")
