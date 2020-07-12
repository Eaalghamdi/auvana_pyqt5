import pandas as pd
import cv2
import glob



imgs = [i for i in glob.glob("*.jpg")]

cols = ['frame', 'canny_size']
results = []

def cannyImg(img, width, height):
  file_name = "canny"+ img
  img = cv2.imread(img,0)
  dim = (width, height)
  fream_resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
  edges = cv2.Canny(fream_resized,100,150)

  cv2.imwrite(file_name, edges)

    
  canny_size = os.path.getsize(file_name)
    
  results.append([file_name, canny_size])
 
  os.remove(file_name)