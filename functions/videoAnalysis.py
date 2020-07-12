import cv2
from skimage.measure import compare_ssim as ssim

cols = ['video', 'mean_color', 'std_color', 'mean_adj',
        'std_adj', 'mean_adj_abs', 'std_adj_abs', 'mean_ssi', 'std_ssi', 'fps', 'ssi_valus', 'img_color']
results = []


class VideoAnalysis:
    def __init__(self, file):
        self.file = file
        self.vidcap = cv2.VideoCapture(file)
        self.fps = int(self.vidcap.get(cv2.CAP_PROP_FPS))

    # helping function
    def sortedFrames(listFrames):
        listFrames = [x.split('.')[0] for x in listFrames]
        listFrames = sorted(listFrames, key=lambda x: int(x))
        listFrames = [x + '.jpg'for x in listFrames]
        return listFrames

    # features extraction

    def extractFrames(self, time):
        count = 0
        success = True
        while success:
            success, image = self.vidcap.read()
            if count % (time*self.fps) == 0:
                cv2.imwrite('%d.jpg' % count, image)
            count += 1

    def image_colorfulness(image):
        try:
            # split the image into its respective RGB components
            (B, G, R) = cv2.split(image.astype("float"))

            # compute rg = R - G
            rg = np.absolute(R - G)

            # compute yb = 0.5 * (R + G) - B
            yb = np.absolute(0.5 * (R + G) - B)

            # compute the mean and standard deviation of both `rg` and `yb`
            (rbMean, rbStd) = (np.mean(rg), np.std(rg))
            (ybMean, ybStd) = (np.mean(yb), np.std(yb))

            # combine the mean and standard deviations
            stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
            meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))

            # derive the "colorfulness" metric and return it
            return stdRoot + (0.3 * meanRoot)
        except Exception as e:
            print(str(e))


def get_frames(video):
    vidcap = cv2.VideoCapture(video)
    count = 0
    success = True

    # get fps count
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))

    while success:
        success, image = vidcap.read()

        if count % (1*fps) == 0:
            # write frames to temprorary folder
            cv2.imwrite('frame%d.jpg' % count, image)
        count += 1

# caculations

    img_color = []
    diff_color_adj = []
    diff_color_adj_abs = []
    ssi_valus = []

    # you need to change this so it get the frame as they added
    imgs = [f for f in glob.glob("*.jpg") if os.path.getsize(f) != 0]

    for img in imgs:
        img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        img_color.append(image_colorfulness(img))

    for f1, f2 in zip(imgs, imgs[1:]):
        f1 = cv2.imread(f1, cv2.IMREAD_UNCHANGED)
        f2 = cv2.imread(f2)

        width = int(f1.shape[1])
        height = int(f1.shape[0])
        dim = (width, height)
        # resize image
        f2 = cv2.resize(f2, dim, interpolation=cv2.INTER_AREA)


#         # ssi needs two imgs of the same size so we need to make the two frames of the same size
#         (H, W, _) = f1.shape
#         f2 = cv2.resize(f2, (W, H))

        img1_color = image_colorfulness(f1)
        img2_color = image_colorfulness(f2)

        diff_color_adj.append(img1_color - img2_color)
        diff_color_adj_abs.append(abs(img1_color - img2_color))

        # takes two paramters, f1, and f2
        ssi = ssim(f1, f2, multichannel=True)
        ssi_valus.append(ssi)

   # caculate and add all results
    mean_color = np.mean(img_color)
    std_color = np.std(img_color)

    mean_adj = np.mean(diff_color_adj)
    std_adj = np.std(diff_color_adj)

    mean_adj_abs = np.mean(diff_color_adj_abs)
    std_adj_abs = np.std(diff_color_adj_abs)

    mean_ssi = np.mean(ssi_valus)
    std_ssi = np.std(ssi_valus)

    results.append([video, mean_color, std_color, mean_adj, std_adj, mean_adj_abs, std_adj_abs, mean_ssi,
                    std_ssi, fps, ssi_valus, img_color])

    results = []
    vid = 'AL1.mp4'
    cap = cv2.VideoCapture(vid)
    videoName = vid.split(".")[0]

    # stores the presence/absence of object in the present frame. -1 for absent and 1 for present
    statusList = [None, None]
    times = []  # stores timestamps of the entry and exit of object
    movingDurtionDifference = []  # store durations of movement of each object
    movingDurtionAll, movingDurtionAll_ms, startTime = 0, 0, 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps
    minutes = int(duration/60)
    seconds = duration % 60

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        if frame1 is not None:
            frame1 = cv2.resize(frame1, (frame_width, frame_height))
        if frame2 is not None:
            frame2 = cv2.resize(frame1, (frame_width, frame_height))

        ssi = ssim(frame1, frame2, multichannel=True)

        img1_color = image_colorfulness(f1)
        img2_color = image_colorfulness(f2)

        frame1 = frame2
        ret, frame2 = cap.read()
        if frame2 is None:
            break

        if cv2.waitKey(40) == 27:
            break

    # add features to results
    results.append([ssi])

    cv2.destroyAllWindows()
    cap.release()
