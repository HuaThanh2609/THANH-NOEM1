import cv2
import numpy as np
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Không thể mở camera!")
    exit()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils  

canvas = None  
prev_x, prev_y = None, None  

# Danh sách màu (RGB)
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0)]
color_names = ["Red", "Green", "Blue", "Yellow", "White", "Black", "Eraser"]
current_color = (0, 0, 255)  # Mặc định là màu đỏ
eraser_mode = False  # Chế độ xóa

# Vị trí menu màu (góc trái)
menu_x, menu_y, menu_size = 10, 50, 50  

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Không thể đọc frame từ camera!")
        break

    frame = cv2.flip(frame, 1)  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if canvas is None:
        canvas = np.zeros_like(frame, dtype=np.uint8)

    # Vẽ menu màu ở góc trái
    for i, color in enumerate(colors):
        cv2.rectangle(frame, (menu_x, menu_y + i * menu_size), 
                      (menu_x + menu_size, menu_y + (i + 1) * menu_size), color, -1)
        cv2.rectangle(frame, (menu_x, menu_y + i * menu_size), 
                      (menu_x + menu_size, menu_y + (i + 1) * menu_size), (255, 255, 255), 2)

        # Hiển thị tên màu
        cv2.putText(frame, color_names[i], (menu_x + menu_size + 10, menu_y + i * menu_size + 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Nút "Xóa toàn bộ"
    clear_x, clear_y, clear_w, clear_h = 10, menu_y + len(colors) * menu_size + 10, 80, 40
    cv2.rectangle(frame, (clear_x, clear_y), (clear_x + clear_w, clear_y + clear_h), (200, 200, 200), -1)
    cv2.rectangle(frame, (clear_x, clear_y), (clear_x + clear_w, clear_y + clear_h), (255, 255, 255), 2)
    cv2.putText(frame, "CLEAR", (clear_x + 10, clear_y + 25), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    result = hands.process(rgb_frame)
    can_draw = True  

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x_index, y_index = int(hand_landmarks.landmark[8].x * frame.shape[1]), int(hand_landmarks.landmark[8].y * frame.shape[0])
            x_thumb, y_thumb = int(hand_landmarks.landmark[4].x * frame.shape[1]), int(hand_landmarks.landmark[4].y * frame.shape[0])

            distance = math.sqrt((x_index - x_thumb) ** 2 + (y_index - y_thumb) ** 2)
            if distance < 50:
                can_draw = False  

            # Kiểm tra nếu tay chạm vào bảng màu
            for i in range(len(colors)):
                if menu_x < x_index < menu_x + menu_size and menu_y + i * menu_size < y_index < menu_y + (i + 1) * menu_size:
                    if i == len(colors) - 1:  # Nếu chọn "Eraser"
                        eraser_mode = True
                        current_color = (0, 0, 0)  # Đổi sang màu nền để xóa
                    else:
                        eraser_mode = False
                        current_color = colors[i]
                    can_draw = False  
                    print(f"🖌️ Đã chọn: {color_names[i]}")

            # Kiểm tra nếu tay chạm vào nút "CLEAR"
            if clear_x < x_index < clear_x + clear_w and clear_y < y_index < clear_y + clear_h:
                canvas = np.zeros_like(frame, dtype=np.uint8)
                can_draw = False  
                print("🗑️ Đã xóa toàn bộ canvas!")

            if can_draw:
                thickness = 30 if eraser_mode else 10  # Nếu là bút xóa thì nét to hơn
                if prev_x is not None and prev_y is not None:
                    cv2.line(canvas, (prev_x, prev_y), (x_index, y_index), current_color, thickness)  
                else:
                    cv2.circle(canvas, (x_index, y_index), thickness // 2, current_color, -1)

                prev_x, prev_y = x_index, y_index  
            else:
                prev_x, prev_y = None, None  

    blended = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow("Air Canvas - Vẽ + Bút xóa", blended)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
