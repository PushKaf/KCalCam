import cv2 
import numpy as np


frameThickness = 2
font = cv2.FONT_HERSHEY_PLAIN
fontSize = 2
fontThickness = 2

def readClasses():
	classes = []
	with open("coco.names", "r") as f:
		classes = [line.strip() for line in f.readlines()]	

	return classes

def main(imgName="detect.png", write="detected.png"):
	classes = readClasses()
	print("Loading YOLO...")

	net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
		
	layersNames = net.getLayerNames()
	outputLayers = [layersNames[i[0] -1] for i in net.getUnconnectedOutLayers()]
	colors = np.random.uniform(0, 255, size=(len(classes), 3))

	print("Loading Image...")
	img = cv2.imread(imgName)
	cv2.resize(img, None, fx=0.4, fy=0.4) 
	height, width, _ = img.shape

	print("Detecting Objects...")
	blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0,0,0), True, crop=False)

	net.setInput(blob)
	outs = net.forward(outputLayers)

	classIds = []
	confidences = []
	boxes = []

	for out in outs:
		for detection in out:
			scores = detection[5:]
			classId = np.argmax(scores)
			confidence = scores[classId]
			if(confidence > 0.5):
				print("Objected Detected")
				centerX = int(detection[0] * width)
				centerY = int(detection[1] * height)
				w = int(detection[2] * width)
				h = int(detection[3] * height)

				x = int(centerX - w / 2)
				y = int(centerY - h / 2)

				boxes.append([x,y,w,h])
				confidences.append(float(confidence))
				classIds.append(classId)

	
	clasifs = []
	indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
	for i in range(len(boxes)):
		if i in indexes:
			x,y,w,h = boxes[i]
			label =classes[classIds[i]]
			confidence = int(confidences[i] * 100)
			color = colors[i]
			cv2.rectangle(img, (x,y), (x+w, y+h), color, frameThickness)
			cv2.putText(img, label, (x,y +30), font, fontSize, color, fontThickness)
			cv2.putText(img, f"{str(confidence)}%", (x+w-69,y+30), font, fontSize, color, fontThickness)

			clasifs.append([label, confidence])
			

	cv2.imwrite(write, img)
	# print(clasifs[0][0])
	return clasifs

if __name__ == '__main__':
	print(main())
