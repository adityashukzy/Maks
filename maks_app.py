from botocore.vendored.six import BytesIO
import cv2
import time
import keras
import numpy as np
import playsound
from PIL import Image
import tensorflow as tf
from tensorflow.keras import layers
from mongodb_tools.mongo_upload import make_violator_entry_in_db

def load_model(model_path):
	"""
	Loads model from provided model path.

	Returns: Keras SavedModel object
	"""
	model = keras.models.load_model(model_path)
	return model

def makePrediction(frame, model):
	"""
	Passes webcam image to model and returns prediction score.

	Returns: Float value of prediction
	"""
	prediction = np.squeeze(model.predict(frame))
	return prediction

def videoCapture(model_path="/Users/adityashukla/Documents/GitHub/facemask-model", camera="webcam"):
	"""
	Captures video from webcam using OpenCV; if person appearing in image is found to not be wearing a mask for more than 3 frames, they are assessed as a violator. Call to MongoDB database managing utility is made to upload image of violator to database.

	Returns: None
	"""
	if camera == "webcam":
		cam = cv2.VideoCapture(0)
	cv2.namedWindow("Maks ~ safety, simplified.")

	# Loading model
	model = load_model(model_path)

	# Initializing helper variables
	count = 0
	previousViolations = 0

	while True:
		ret, frame = cam.read()
		count += 1
		
		if not ret:
			# Debugging convenience
			# print("Failed to grab frame! Restart Maks!")
			break

		# Flipping the video
		frame = cv2.flip(frame, 1)

		# Adding rectangle to guide face placement
		frame = cv2.rectangle(frame, (450, 100), (850, 600), (187, 9, 232), 3)
		cv2.putText(frame, "Position face inside the rectangle!", (520, 92), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)

		cv2.imshow("Maks ~ safety, simplified.", frame)

		if count % 100 == 0:
			# Preprocessing frame before passing to model
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			
			img_height = img_width = 256
			img = cv2.resize(frame, (img_height, img_width))
			img = tf.expand_dims(img, 0)

			# Running inference on clicked frame
			prediction = makePrediction(img, model)
			if prediction < 0.5:
				result = "Wearing mask"
			elif prediction >= 0.5:
				result = "Not wearing mask!"
				if previousViolations == 5:
					# Play sound
					playsound.playsound("/Users/adityashukla/Documents/GitHub/Maks/dependencies/audio.wav")

					# Make db-uploading calls
					img_buffer = BytesIO() # initializing an image buffer
					frameImage = Image.fromarray(frame)
					frameImage.save(img_buffer, format='png') # saving image as the image buffer
					img_buffer.seek(0) # seeking to the start

					# passing the confidence value and the image buffer to the mongodb utility
					make_violator_entry_in_db(float(prediction), img_buffer)

					# Reset violations to 0 after sending violator's info to DB
					previousViolations = 0
				
				previousViolations += 1
			
			print(result)

		k = cv2.waitKey(1)
		if k % 256 == 27:
			# ESC pressed
			print("Escape hit, closing Maks...")
			break
		elif k % 256 == 32:
			# SPACE pressed
			cv2.imwrite("img_name", frame)

	cam.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	videoCapture()