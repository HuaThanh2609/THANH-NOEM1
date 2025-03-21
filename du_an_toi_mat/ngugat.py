import cv2
import mediapipe as mp
import numpy as np
import time
import threading
import pygame  # Dùng để phát âm thanh từ file

# --- 1. Khởi tạo Mediapipe ---
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1, refine_landmarks=True,
    min_detection_confidence=0.5, min_tracking_confidence=0.5
)

# --- 2. Load âm thanh cảnh báo ---
ALERT_SOUND = "D:\Downloads\p.mp3"  # Thay bằng đường dẫn file âm thanh của bạn
pygame.mixer.init()

# --- 3. Hàm phát âm thanh ---
def play_alarm():
    pygame.mixer.music.load(ALERT_SOUND)
    pygame.mixer.music.play(-1)  # Lặp vô hạn cho đến khi tắt

def stop_alarm():
    pygame.mixer.music.stop()

# --- 4. Hàm tính khoảng cách Euclidean ---
def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

# --- 5. Hàm tính tỷ lệ mở mắt (EAR) ---
def calculate_EAR(landmarks, eye_indices, frame_width, frame_height):
    points = [np.array([int(landmarks[idx].x * frame_width), int(landmarks[idx].y * frame_height)]) for idx in eye_indices]
    A = euclidean_distance(points[1], points[5])
    B = euclidean_distance(points[2], points[4])
    C = euclidean_distance(points[0], points[3])
    return (A + B) / (2.0 * C), points

# --- 6. Ngưỡng & biến ---
EAR_THRESHOLD = 0.25  # Ngưỡng để xác định mắt nhắm
WARNING_TIME = 10      # Thời gian tối đa nhắm mắt trước cảnh báo (giây)
frame_rate = 30        # Giả định FPS của camera
CONSEC_FRAMES = WARNING_TIME * frame_rate

frame_counter = 0
start_time = None
alert_triggered = False

# --- 7. Mở Camera ---
cap = cv2.VideoCapture(0)  # Hoặc 2,3 nếu không nhận



while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Lật ngang lại để giống gương
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)
    frame_height, frame_width = frame.shape[:2]

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Chỉ vẽ mắt
            left_eye_indices = [33, 160, 158, 133, 153, 144]
            right_eye_indices = [362, 385, 387, 263, 373, 380]

            left_ear, left_eye_pts = calculate_EAR(face_landmarks.landmark, left_eye_indices, frame_width, frame_height)
            right_ear, right_eye_pts = calculate_EAR(face_landmarks.landmark, right_eye_indices, frame_width, frame_height)
            ear = (left_ear + right_ear) / 2.0

            # --- Vẽ mắt lên khung hình ---
            for pt in left_eye_pts + right_eye_pts:
                cv2.circle(frame, tuple(pt), 2, (0, 255, 0), -1)

            cv2.putText(frame, f"EAR: {ear:.2f}", (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # --- Kiểm tra buồn ngủ ---
            if ear < EAR_THRESHOLD:
                if start_time is None:
                    start_time = time.time()
                elapsed_time = time.time() - start_time

                cv2.putText(frame, f"Drowsy! {elapsed_time:.1f}s", (30, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                frame_counter += 1
                if frame_counter >= CONSEC_FRAMES and not alert_triggered:
                    alert_triggered = True
                    threading.Thread(target=play_alarm, daemon=True).start()
            else:
                frame_counter = 0
                start_time = None
                if alert_triggered:
                    alert_triggered = False
                    stop_alarm()

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
