import pyvirtualcam
import cv2
import sys
import utils

def main(path):
    frame = cv2.imread(path)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = utils.add_padding(frame)
    width = frame.shape[1]
    height = frame.shape[0]
    cam = pyvirtualcam.Camera(width=width, height=height, fps=20)
    while True:
        cam.send(frame)
        cam.sleep_until_next_frame()
    
if __name__ == "__main__":
    path = "example.png"
    if len(sys.argv) == 2 :
        path = sys.argv[1]
    print(path)
    main(path)
    
    