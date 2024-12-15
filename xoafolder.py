import shutil

def delete_folder(folder):
    try:
        shutil.rmtree(folder)
        print(f"Thư mục '{folder}' đã được xóa thành công")
    except FileNotFoundError:
        print(f"Thư mục '{folder}' không tồn tại.")
    except PermissionError:
        print(f"Không có quyền xóa thư mục '{folder}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Đường dẫn đến thư mục cần xóa
folder_to_delete = 'D:/PROJECT_Group_5_Merge_Sort'

# Xóa thư mục
delete_folder(folder_to_delete)
