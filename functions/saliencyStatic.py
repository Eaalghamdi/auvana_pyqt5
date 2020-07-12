## salincy of images 
# the idea of counting contors of salient objects is not accurate becuase they are too many contours 
# use img size after finding salincy

import cv2

def SpectralResidual(image):
    imgName = image.split('.')[0]
	img =cv2.imread(image)
	saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
	(success, saliencyMap) = saliency.computeSaliency(img)
	saliencyMap = (saliencyMap * 255).astype("uint8")

	# threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,
	# 	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	# # using trheshold map to draw contours and count them
	# contours, h = cv2.findContours(threshMap, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	# print(len(contours))
	# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

	# cv2.imshow("Image", img)
	# cv2.imshow("Output", saliencyMap)
	oname = "./outputs/" + 'SpectralResidual_'+ imgName + ".jpg"
	cv2.imwrite(oname, saliencyMap)
	SpectralResidual_keyframeSize = os.path.getsize(oname)
    os.remove(oname)
    return SpectralResidual_keyframeSize
	


def SaliencyFineGrained (image):
    imgName = image.split('.')[0]
	img =cv2.imread(image)
	saliency = cv2.saliency.StaticSaliencyFineGrained_create()
	(success, saliencyMap) = saliency.computeSaliency(img)

	# if we would like a *binary* map that we could process for contours,
	# compute convex hull's, extract bounding boxes, etc., we can
	# additionally threshold the saliency map
	# threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,
	# 	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	# # using trheshold map to draw contours and count them
	# contours, h = cv2.findContours(threshMap, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	# print(len(contours))
	# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

 
	# show the images
	# cv2.imshow("Image", img)
	# cv2.imshow("Output", saliencyMap)
	# cv2.imshow("Thresh", threshMap)
	
	oname = "./outputs/" + 'SaliencyFineGrained_'+ imgName + ".jpg"
	cv2.imwrite(oname, saliencyMap)
	SaliencyFineGrained_keyframeSize = os.path.getsize(oname)
    os.remove(oname)
    return SaliencyFineGrained_keyframeSize



## Finding countros in images
# img = cv2.imread('faces.jpeg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(gray,127,255,1)
# contours,h = cv2.findContours(thresh,1,2)
# for cnt in contours:
#   cv2.drawContours(img,[cnt],0,(0,0,255),1)
# print(len(contours))
# cv2.imshow("Thresh", img)
# cv2.waitKey(0)