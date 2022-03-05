		# extract the ROI of the face region as a separate image
		(x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
		roi = image[y:y + h, x:x + w]
		roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)
		# show the particular face part
		cv2.imshow("ROI", roi)
		cv2.imshow("Image", clone)
        
        key = cv2.waitKey(1) & 0xFF
 		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
		cv2.waitKey(0)
	# visualize all facial landmarks with a transparent overlay
	output = face_utils.visualize_facial_landmarks(image, shape)
	cv2.imshow("Image", output)
	cv2.waitKey(0)