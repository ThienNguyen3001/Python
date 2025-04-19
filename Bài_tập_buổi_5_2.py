from math import *






n = int(input('Nhap so phan tu:'))
a = []
for i in range(n):
    a.append(int(input(f"Nhap phan tu thu {i+1}: ")))

def menu():
    print('Menu:')
    print('============================================================================================')
    print('1. In ra danh sách vừa tạo.')
    print('2. In đảo ngược danh sách.')
    print('3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).')
    print('4. tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.')
    print('5. đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.')
    print('6. In ra vị trí các phần tử là số nguyên tố.')
    print('7. tìm các số duy nhất (không trùng lặp) trong danh sách.')
    print('8. liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.')
    print('9. In ra các đoạn con trong danh sách giảm liên tiếp.')
    print('============================================================================================')

menu()
def menu1(a: list):
    print(a)

def menu2(a: list):
    print(a.reverse())

def menu3(a: list):
    print(sorted(a))

def menu4(a: list):
    max = a[0]
    i_max = 0
    for i in range(a):
        if a[i] >= max:
            max = a[i]
            i_max = i
    print('Gia tri lon nhat:',max)
    print('Vi tri lon nhat:',i_max)

def menu5(a: list, x: int):
    cnt = 0
    for i in a:
        if i == x:
            cnt += 1
    print(cnt)

def menu6(a: list):
    def prime(x: int):
        for i in range(int(sqrt(n))+1):
            if x % i == 0:
                return True
        return False

    for i in range(a):
        if prime(a[i]):
            print(i)

def menu7(a: list):
    return a

def menu8(a: list):
    dic = {}
    for i in range(a):
        if a[i] not in dic:
            dic[a[i]] += 1

    for i in dic:
        print(i)

def menu9(a: list):
    return a


menu8(a)


