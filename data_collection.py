import os
import cv2

DATA_DIR = "./data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

classes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
dataset_size = 100

capture = cv2.VideoCapture(0)

for letter in classes:
    if not os.path.exists(os.path.join(DATA_DIR, letter)):
        os.makedirs(os.path.join(DATA_DIR, letter))
        
    print(f"Collecting data for {letter}")
    
    done = False
    while True:
        ret, frame = capture.read()
        cv2.putText(frame, f'Ready? Press "{letter}"!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord(letter):
            break
        
    counter = 0
    while counter < dataset_size:
        ret, frame = capture.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(letter), '{}.jpg'.format(counter)), frame)

        counter += 1
        
capture.release()
cv2.destroyAllWindows()
