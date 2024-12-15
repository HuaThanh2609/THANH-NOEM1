import os

def count_files_in_directory(directory_path):
    try:
        # Đếm số lượng tệp tin trong thư mục
        file_count = sum([len(files) for r, d, files in os.walk(directory_path)])
        return file_count
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return 0

# Đường dẫn tới thư mục
directory_path = 'E:/iphone/202404__'

# Đếm số lượng tệp tin
file_count = count_files_in_directory(directory_path)
print(f"Số lượng tệp tin trong thư mục '{directory_path}' là: {file_count}")
