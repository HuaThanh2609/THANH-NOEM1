import math
print("máy tính")
a = float(input("nhập số nguyên a: "))
b = float(input("nhập số nguyên b: "))
c = (input("nhập 1 toán tử: "))

if c == '+':
    print ("kết quả bằng: " ,a + b)
if c == '-':
    print ("kết quả bằng: ", a - b)
if c == '*':
    print ("kết quả bằng: ", a * b)
if c == '/':
    if a != 0 or b != 0:
        print("lỗi không thể chia!!")
    else: print("kết quả bằng: ", a / b)
