# records GoPro

import numpy as np
import os
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

# open the webcam video stream
gopro = cv2.VideoCapture(0)

# open output video file stream
output = VideoWriter('recording.avi', VideoWriter_fourcc(*'MP42'), 15.0, (1920, 1080))


# boolean that will run the infinite loop
run_program = True

while run_program:
    # get the frame from the webcam
    stream_ok, frame = gopro.read()

    if stream_ok:
        # display the current frame if the stream is ok
        cv2.imshow('GoPro', frame)

        # write frame to the video out file
        output.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close windows
cv2.destroyAllWindows()

# release gopro stream
gopro.release()

# release video output file
output.release()
