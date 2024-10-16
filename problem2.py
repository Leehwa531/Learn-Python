import random

choices = ["가위", "바위", "보"]
user_wins, draws, total_games = 0, 0, 0

while True:
    user_choice = input("가위, 바위, 보 중 하나를 선택하세요 (종료: 0): ")
    if user_choice == "0":
        break

    computer_choice = random.choice(choices)
    print(f"컴퓨터 선택: {computer_choice}")

    if user_choice == computer_choice:
        print("무승부!")
        draws += 1
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        print("사용자 승!")
        user_wins += 1
    else:
        print("컴퓨터 승!")

    total_games += 1

print(f"총 게임 횟수: {total_games}, 사용자 전적: {user_wins}승 {total_games-user_wins-draws}패 {draws}무")
