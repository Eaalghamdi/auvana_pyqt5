
# this function compute motion based on changes in pixle vlaues and drwa contours on 
# moving objects and log times of  their entry and exit. Based on this info, it compute
# several features related to motion 

import numpy as np
import cv2, time, pandas
import glob
from statistics import mean, variance, stdev

videos = [i for i in glob.glob("*.avi")]


cols = ['video', 'number of moving objects', 'moving duration(ms)', 'ratio of movingObjects(n/s)',
        'ratio of movingObjects(n/m)','movingDurtionDifference_mean', 'movingDurtionDifference_varaince',
        'movingDurtionDifference_sd',' ratio of movingDurtion(t/s)', 'ratio of movingDurtion(t/m)',
        'satrt-end times']
results = []

def safe_divide(numerator, denominator):
    if denominator == 0:
        index = 0
    else: index = numerator/denominator
    return index

def motionEstimation(vid):

    cap = cv2.VideoCapture(vid)
    videoName = vid.split(".")[0]

    statusList=[None,None] #stores the presence/absence of object in the present frame. -1 for absent and 1 for present
    times=[] #stores timestamps of the entry and exit of object
    movingDurtionDifference = [] # store durations of movement of each object
    movingDurtionAll, movingDurtionAll_ms, startTime = 0,0,0
    fps = cap.get(cv2.CAP_PROP_FPS)    
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps
    minutes = int(duration/60)
    seconds = duration%60
 

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height =int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        if frame1 is not None:
            status=0 #initialise status variable. This stores the presence/absence of object in the current frame
            frame1 = cv2.resize(frame1,(frame_width,frame_height))
        if  frame2 is not None:
            frame2 = cv2.resize(frame2,(frame_width,frame_height))
            
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            # gussain blur kernal, it should be possitve and odd (small n removes more noise)
            blur = cv2.GaussianBlur(gray, (5,5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                if cv2.contourArea(contour) < 1000:
                    continue
                status=1
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

            
            statusList.append(status)
            statusList=statusList[-2:]

            #Detecting the entry and exit of objects
            #Every entry/exit is identified by a sign change of the last two elements in our list, hence product is -1
            if statusList[-1]==1 and statusList[-2]==0:
                startTime =  cap.get(cv2.CAP_PROP_POS_MSEC)
                times.append(cap.get(cv2.CAP_PROP_POS_MSEC))
            if statusList[-1]==0  and statusList[-2]==1:
                endTime = cap.get(cv2.CAP_PROP_POS_MSEC)
                times.append(cap.get(cv2.CAP_PROP_POS_MSEC))
                movingDurtion = endTime - startTime
                movingDurtionDifference.append(movingDurtion)
                movingDurtionAll_ms = movingDurtion + movingDurtionAll # in miliseconds
    # get out of the loop to cacluate the following 
            movingDurtionAll_s = movingDurtionAll_ms/1000 # convert to ms to seconds
            movingDurtion_s = safe_divide(movingDurtionAll_s, seconds)
    
            movingDurtionAll_m  = movingDurtion_s/60
            movingDurtion_m = safe_divide(movingDurtionAll_m,minutes)
            
            frame1 = frame2
            ret, frame2 = cap.read()
            if frame2 is None:
                break
            
            if cv2.waitKey(40) == 27:
                break

    
    # global features compution
    numberOfMovingObjects = len(times)
    movingObjects_s = safe_divide(numberOfMovingObjects, seconds) # ratio of moving objects in ss
    movingObjects_m = safe_divide(numberOfMovingObjects, minutes)
    if len(movingDurtionDifference) > 1:
        movingDurtionDifference_mean = mean(movingDurtionDifference)
        movingDurtionDifference_varaince = variance(movingDurtionDifference)
        movingDurtionDifference_sd = stdev(movingDurtionDifference)
    else:
        movingDurtionDifference_mean = 0
        movingDurtionDifference_varaince = 0
        movingDurtionDifference_sd = 0
        

    # add features to results
    results.append([videoName, numberOfMovingObjects, movingDurtionAll_ms, movingObjects_s,
                    movingObjects_m, movingDurtionDifference_mean, movingDurtionDifference_varaince, 
                    movingDurtionDifference_sd, movingDurtion_s, movingDurtion_m, times])



    cv2.destroyAllWindows()
    cap.release()

for v in videos:
    motionEstimation(v)

df = pandas.DataFrame(results, columns=cols)
df.to_csv("Motion_Results.csv")