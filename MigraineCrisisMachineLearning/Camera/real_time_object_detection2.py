# USAGE
# python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import Ordenar
import Distancia
import Tamano
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--prototxt", required=True,
	#help="path to Caffe 'deploy' prototxt file")
#ap.add_argument("-m", "--model", required=True,
	#help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
Color_selection = [0,0,150]
Color_no_selection = [150,0,0]
#COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
lista = []

# load our serialized model from disk
print("[INFO] loading model...")
#net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")

# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()
person_number = 1
z = 0
ID_final = 0

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	count = -1
	listaX = []
	listaY = []
	listaEndX = []
	listaEndY = []
	idxlist = []
	prueba = []	
	

	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# grab the frame dimensions and convert it to a blob
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)

	# pass the blob through the network and obtain the detections and
	# predictions
	net.setInput(blob)
	detections = net.forward()

	# loop over the detections
	for i in np.arange(0, detections.shape[2]):

		# extract the confidence (i.e., probability) associated with
		# the prediction
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > args["confidence"]:
			# extract the index of the class label from the
			# `detections`, then compute the (x, y)-coordinates of
			# the bounding box for the object
			idx = int(detections[0, 0, i, 1])
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# draw the prediction on the frame
			if CLASSES[idx] == "person":
				count = count + 1	
				idxlist.append(idx)				
				listaX.append(startX)
				listaY.append(startY)
				listaEndX.append(endX)
				listaEndY.append(endY)
				longitud = len(listaX)
				#print "StartX"
				#print startX
				#print "Lista"
				#print listaX
				(prueba, listaY, listaEndX, listaEndY) = Ordenar.Ordenar_vectores(listaX, listaY, listaEndX, listaEndY)
				"""if z == 0:
					nuevoTamano=Tamano.nuevo_tamano(prueba, listaY, listaEndX, listaEndY, person_number)
					if nuevoTamano == None:
						break
				elif z== 1:
					ID1, ID2 = Tamano.calculo_tamano(prueba, listaY, listaEndX, listaEndY, nuevoTamano)
	 				ID_final,puntos_mediosX, puntos_mediosY = Distancia.calculo_distancias(startX, startY, endX, endY,puntos_mediosX, puntos_mediosY ,ID1, ID2)
					tamano_anterior = Tamano.nuevo_tamano(prueba, listaY, listaEndX, listaEndY, ID_final)

				else:
					ID1, ID2 = Tamano.calculo_tamano(prueba, listaY, listaEndX, listaEndY, tamano_anterior)
	 				ID_final,puntos_mediosX, puntos_mediosY = Distancia.calculo_distancias(startX, startY, endX, endY,puntos_mediosX, puntos_mediosY ,ID1, ID2)
					tamano_anterior = Tamano.nuevo_tamano(prueba, listaY, listaEndX, listaEndY, ID_final)
					print "ID_FINAL", ID_final"""
				#for j in range(0, longitud):
				#startX2 = listaX(count)
				#startY2 = listaY(count)
				#endX2 = listaEndX(count)
				#endY2 = listaEndY(count)
				
				
				#count = count + 1
				#label = "Detectado"
				"""cv2.rectangle(frame, (startX, startY), (endX, endY),
				COLORS[idx], 2)
				y = startY - 15 if startY - 15 > 15 else startY + 15
				cv2.putText(frame, label, (startX, y),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)"""
				z = z + 1
				print "ZETA",z
			
			else:
				break

	for j in range (0, len(idxlist)):	
		if count !=-1 and count >= 0 and idxlist[j] == 15:
			print "ESTOY DETECTANDO A ", len(idxlist)
			#if z == 1:
			ID_final = j			
			#if ID_final > len(prueba):
			#	ID_final = (len(prueba)-1)
			print ID_final
			startX2 = prueba[ID_final]
			print startX2
			startY2 = listaY[ID_final]
			endX2 = listaEndX[ID_final]
			endY2 = listaEndY[ID_final]
			#label = "{}: {:.2f}%".format(CLASSES[idx],
				#confidence * 100)
				#count)		
			if ID_final == person_number:
				cv2.rectangle(frame, (startX2, startY2), (endX2, endY2),
				Color_selection, 2)
			else:
				cv2.rectangle(frame, (startX2, startY2), (endX2, endY2),
				Color_no_selection, 2)
			y = startY2 - 15 if startY2 - 15 > 15 else startY2 + 15
			#cv2.putText(frame, label, (startX2, y),
			#cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)	

		else:
			continue 

	# if the `q` key was pressed, break from the loop
	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF	
	if key == ord("q"):
		break

	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
