import shutil

def move_folder(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Đã di chuyển thư mục từ '{source}' sang '{destination}'")
    except FileNotFoundError:
        print(f"Thư mục '{source}' không tồn tại.")
    except PermissionError:
        print(f"Không có quyền di chuyển thư mục '{source}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Đường dẫn đến thư mục nguồn và thư mục đích
source_folder = 'E:/thanhdeptrai'
destination_folder = 'D:/thanhdeptrai'

# Di chuyển thư mục
move_folder(source_folder, destination_folder)
