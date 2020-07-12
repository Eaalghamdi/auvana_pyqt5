
import subprocess
import os
import glob
import time
os.chdir('/Users/user/Desktop/all_videos/Video_indexer/videos/videos_avi/trimed_30/')

videos = [i for i in glob.glob("*.avi") if i.startswith('trimed')]

# prossessedvideos = [i for i in videos if i.startswith('H265_')]
# prossessedvideos = [i.strip('H265_') for i in prossessedvideos]
# allvideos = [i.strip('H265_') for i in videos]
# unprocessed = [i for i in allvideos if i not in prossessedvideos]


def videoConv(video, encoder, codec, crf, fps, vformat):
    # paramters:
    # encoder options 'libx264', libx265, libvpx-vp9
    # codec options: 'vp9' , 'mpeg4',
    # Constant Rate Factor (CRF) (-crf 23)
    # video format (vp9 > webm), (libx264, libx265 > mp4),

    file_name = video.split(".")[0]
    video_out = codec + "_" + file_name + "." + vformat
    cmds = ['nice', '-5', 'ffmpeg', '-i', video, '-c:v', encoder,  '-an', '-vf',
            'scale=320:240', '-crf',  crf, '-r', fps, '-hide_banner', video_out]

    # notes:
    # '-preset', 'ultrafast' for faster processing but less quality
    # '-an' for not copying the sound
    subprocess.Popen(cmds)

# Create a function called "chunks" with two arguments, l and n:


def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]


videochuncks = list(chunks(unprocessed, 5))

for chunk in videochuncks:
    for vid in chunk:
        videoConv(vid, 'libx265', 'H265', '23', '23', 'mp4')
        time.sleep(5)


# import numpy as np
# import cv2

# cap = cv2.VideoCapture('AL1-Scene-016.mp4')

# fgbg = cv2.createBackgroundSubtractorMOG()

# while(1):
#     ret, frame = cap.read()

#     fgmask = fgbg.apply(frame)

#     cv2.imshow('frame', fgmask)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()
