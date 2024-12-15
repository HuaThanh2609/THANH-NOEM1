import sys
from time import sleep

def print_lyric():
    lines = [
        ("yêu thương sao cho vừa", 0.05, 1.0),
        ("hay anh đang lo thừa", 0.05, 1.0),
        ("cho anh mong như cơm bữa", 0.05, 1.2),
        ("em đừng xinh như thế nữa", 0.05, 0.5),
        ("Loạn nhịp cả tim lên rồi", 0.05, 0.08),
        ("Đầu này toàn là em mà thôi",0.05, 1.0),
        ("yeah - eh, ee-yeah, ee-yeah",0.05, 0.8),
        ("Nỗi nhớ em cầu kỳ Nên chẳng biết lý d o là gì",0.08,1.0),
        ("Hao tốn hơn nhiều GB Nên cần dùng thêm USB",0.05,1.5),
        ("Nỗi nhớ em cầu kỳ Nên chẳng biết lý do là gì",0.05,1.0),
        ("Hao tốn hơn nhiều GB Nên cần dùng thêm D O M I C",0.05,2.3),
        ("Tràn ngập bộ nhớ nhớ nhớ nhớ em",0.06,1.5),
        ("Cho anh cảm giác không sao quên được",0.08,1.2),
        ("Tràn ngập bộ nhớ nhớ nhớ nhớ em",0.1, 1.0),
        ("Nhưng anh mong có cảm giác này mãi",0.08,1.5),
    ]
    
    for line, char_delay, pause_after_line in lines:
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        sleep(pause_after_line)
        print('')

print_lyric()
