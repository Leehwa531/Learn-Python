import random
import numpy as np

# 사용자 입력
user_numbers = [int(input(f"{i+1}번째 100 이하의 정수를 입력하세요: ")) for i in range(5)]

# 컴퓨터 무작위 생성
computer_numbers = [random.randint(1, 100) for _ in range(5)]

# 합계, 평균, 분산, 표준편차 계산
user_sum = np.sum(user_numbers)
user_mean = np.mean(user_numbers)
user_variance = np.var(user_numbers)
user_std_dev = np.std(user_numbers)

computer_sum = np.sum(computer_numbers)
computer_mean = np.mean(computer_numbers)
computer_variance = np.var(computer_numbers)
computer_std_dev = np.std(computer_numbers)

# 결과 출력
print(f"사용자 값 - 합계: {user_sum}, 평균: {user_mean}, 분산: {user_variance}, 표준편차: {user_std_dev}")
print(f"컴퓨터 값 - 합계: {computer_sum}, 평균: {computer_mean}, 분산: {computer_variance}, 표준편차: {computer_std_dev}")
