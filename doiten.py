import os

def rename_folder(old_name, new_name):
    try:
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"Thư mục '{old_name}' đã được đổi tên thành '{new_name}'")
        else:
            print(f"Thư mục '{old_name}' không tồn tại.")
    except PermissionError:
        print(f"Không có quyền đổi tên thư mục '{old_name}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Đặt tên thư mục cũ và mới
old_folder_name = 'D:/huathethanh'
new_folder_name = 'D:/thanhdeptrai'

# In danh sách các file và thư mục trong thư mục hiện tại
print("Nội dung thư mục hiện tại:")
for item in os.listdir('D:/'):
    print(item)

# Đổi tên thư mục
rename_folder(old_folder_name, new_folder_name)
