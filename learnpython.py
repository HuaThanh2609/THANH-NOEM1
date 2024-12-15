print('hua the thanh', 'thanh chim', sep= '##', end= '!\n')
# hứa thế thành đẹp trai nhất thế giới
'''hứa thế thành đepk trai nhất thế giới'''
a = 100
print(type(a))
b = "hứa thế thành đẹp trai có gì sai"
print(type(b))
d = 67.3589345
print('%.3f' % d)# làm tròn số đằng sau có 2 chữ số  
#số phức
r = 6 - 5j# số phức
print(r.real)#phần thực
print(r.imag)#phần ảo
# giá trị true và false check bằng bool
f = 735395 # nếu mà là giá trị lớn hơn không là trả về true ngược lại bằng 0 thì trả về false
print(bool(f))
print('')
#ép kiểu, ví dụ
v = 4375
d = str(v)
print(type(d))
#hoán vị ví dụ
n1 = 200
n2 = 529
n1, n2 = n2, n1
print(n1, n2)
#nhập xuất dữ liệu
sinput = int(input('mời bạn nhập số : '))# ép kiểu để giá trị đó thành số nguyên, tiếp tục tương tự như float
print('số của bạn vừa nhập là: ', sinput)
print(type(sinput))
# ép một danh sách các kí tự vừa nhập thành số nguyên hoặc số thực
'''a = input('nhâp 3 kí tự : ')
s = a.split()
x, y, z = map(int, s)
print(x,y,z)
n, c, v = map(int, input("mơi bạn nhap chuỗi: ").split())
print(n, c, v)'''
#hãy tính chu vi hình chữ nhật có chiều dài lần lượt là: chiều dài: 43, chiều rộng: 24
a , b = map(int, input('chu vi, diện tích:  ').split())
print("chiều dài là:", 2*(a+b))
print('diện tích là: ', a * b)
print("outsystem")
    



