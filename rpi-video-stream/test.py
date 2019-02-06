import cv2
import subprocess as sp
import numpy

FFMPEG_BIN = "ffmpeg"
command = [ FFMPEG_BIN,
        '-i', 'fifo264',
        'pix_fmt', 'bgr24',
        '-vcodec', 'rawvideo',
        '-an', '-sn',
        '-f', 'image2pipe', '-' ]
pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10*9)

while True:
  #Capture image frame by frame
  raw_image = pipe.stdout.read(640*480*3)
  #Transform into a numpy array
  image = numpy.fromstring(raw_image, dtype='uint8')
  image = image.reshape((480,640,3))
  if image is not None:
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.imshow('Video', image)
    
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

pipe.stdout.flush()
cv2.destroyAllWindows()
