import random

while True:
    print('''
     dễ - đoán tối đa 9 lần (Nhập số 1)
     vừa - đoán tối đa 6 lần (Nhập số 2)
     khó - đoán tối đa 4 lần (Nhập số 3)
     ''')
    level = int(input('Nhập cấp độ game:'))
    player_num = int(input('Nhập số của người chơi (1-100):'))
    comp_num = random.randint(1,101)
    if level == 1:
        for i in range(0,9):
            if player_num == comp_num:
                print('OK bạn thắng')
                break
            else:
                if comp_num > player_num:
                    print('Đoán lại, số bạn đoán nhỏ hơn của tôi')
                elif comp_num < player_num:
                    print('Đoán lại, số bạn đoán lớn hơn của tôi')
                player_num = int(input('Nhập số của người chơi (1-100):'))
        print('Bạn vượt quá số lần đoán rồi')
    if level == 2:
        for i in range(0,6):
            if player_num == comp_num:
                print('OK bạn thắng')
                break
            else:
                if comp_num > player_num:
                    print('Đoán lại, số bạn đoán nhỏ hơn của tôi')
                elif comp_num < player_num:
                    print('Đoán lại, số bạn đoán lớn hơn của tôi')
                player_num = int(input('Nhập số của người chơi (1-100):'))
        print('Bạn vượt quá số lần đoán rồi')
    if level == 3:
        for i in range(0,4):
            if player_num == comp_num:
                print('OK bạn thắng')
                break
            else:
                if comp_num > player_num:
                    print('Đoán lại, số bạn đoán nhỏ hơn của tôi')
                elif comp_num < player_num:
                    print('Đoán lại, số bạn đoán lớn hơn của tôi')
                player_num = int(input('Nhập số của người chơi (1-100):'))
        print('Bạn vượt quá số lần đoán rồi')


    play_again = input('Có muốn chơi tiếp không (Y/N):').lower()
    if play_again == 'n':
        break
    elif play_again == 'y':
        continue
    else:
        print('Nhập không hợp lệ')