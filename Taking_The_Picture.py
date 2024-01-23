import cv2
import os

# Define the directory where you want to save the images
save_dir1 = "YOUR_DESIRED_LOCATION"
save_dir2 = "YOUR_DESIRED_LOCATION"

# Create the directory if it doesn't exist
save_dirs = [save_dir1, save_dir2]

# Create each directory with exist_ok=True
for directory in save_dirs:
    os.makedirs(directory, exist_ok=True)

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('t'):
        while True:
            img_name = os.path.join(save_dir1, "Terang_Frame_{}.png".format(terang_counter))
            if not os.path.exists(img_name):
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                terang_counter += 1
                break
            else:
                terang_counter += 1

    elif key == ord('g'):
        while True:
            img_name = os.path.join(save_dir2, "Gelap_Frame_{}.png".format(gelap_counter))
            if not os.path.exists(img_name):
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                gelap_counter += 1
                break
            else:
                gelap_counter += 1

    elif key == ord('e'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()