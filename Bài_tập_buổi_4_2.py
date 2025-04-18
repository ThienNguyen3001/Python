import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def get_result(d1, d2):
    total = d1 + d2
    if total == 5:
        return '5'
    elif total > 5:
        return 'Tài'
    else:
        return 'Xỉu'

def play_game():
    money = 100000
    win_count = 0

    print(f"Bạn bắt đầu với {money} VNĐ. Mỗi ván cược mất tiền.")

    while money > 0:
        print(f"\nTiền hiện tại: {money} VNĐ")
        bet = int(input("Nhập số tiền muốn cược (Nhỏ nhất là 10000): "))
        if bet <= 10000 or bet > money:
            print("Số tiền cược không hợp lệ.")
            continue

        user_choice = input("Chọn cược (Tài / Xỉu / 5): ").strip().capitalize()
        if user_choice not in ['Tài', 'Xỉu', '5']:
            print("Lựa chọn không hợp lệ.")
            continue

        d1, d2 = roll_dice()
        result = get_result(d1, d2)
        print(f"Xúc xắc ra: {d1} + {d2} = {d1 + d2} → {result}")

        if user_choice == result:
            if result == '5':
                reward = bet * 3
                print(f"Trúng lớn! Bạn thắng {reward} VNĐ")
            else:
                reward = bet
                print(f"Bạn đoán đúng! Nhận {reward} VNĐ")
            money += reward
            win_count += 1
        else:
            print(f"Bạn đoán sai. Mất {bet} VNĐ")
            money -= bet

        if money <= 0:
            print("Game over.")
            break

        cont = input("Chơi tiếp không? (y/n): ").strip().lower()
        if cont != 'y':
            break

    print("Thống kê:")
    print(f"Số tiền còn lại: {money} VNĐ")
    print(f"Số ván thắng: {win_count}")

if __name__ == "__main__":
    play_game()
