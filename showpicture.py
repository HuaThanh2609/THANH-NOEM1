import cv2

def read_and_display_image(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)
    
    # Kiểm tra xem ảnh có được đọc thành công không
    if image is None:
        print(f"Không thể đọc ảnh từ đường dẫn '{image_path}'")
        return

    # Hiển thị ảnh
    cv2.imshow('Image', image)
    
    # Đợi cho đến khi một phím bất kỳ được nhấn
    cv2.waitKey(0)
    
    # Đóng cửa sổ hiển thị ảnh
    cv2.destroyAllWindows()

# Đường dẫn đến tệp tin ảnh
image_path = r'E:\\iphone\\202404__\\IMG_4727.JPG'

# Đọc và hiển thị ảnh
read_and_display_image(image_path)
                                                                                                                                                                                                                                                                                                                                                                