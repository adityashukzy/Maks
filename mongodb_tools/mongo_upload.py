import os
import dns
from pymongo import MongoClient
from aws_tools import aws_upload
from dotenv import load_dotenv
from datetime import datetime

def make_violator_entry_in_db(
	confidence_pred,
	img_buffer
	):
	"""
	Inserts entry into MongoDB collection of link to image of violator, confidence scores and timestamp.

	Returns: None
	"""

	## Getting mongo string from .env
	load_dotenv()
	mongo_string = os.getenv('MONGODB_AUTH_URI')

	## Initilizing Mongo client
	client = MongoClient(mongo_string)
	print(client["Maks-Cluster"]) # Debugging convenience; to be removed in production code

	## Uploading image to AWS and getting link of uploaded image
	uploaded_img_link = aws_upload.upload_image(img_buffer=img_buffer)

	## Preparing timestamp of time of violation
	now = datetime.now()
	date_string = now.strftime("%d/%m/%Y %H:%M:%S")

	## Pulling DB variables
	database = client['User-Credentials'] # Picking database from our Mongo client
	coll = database['violators'] # Picking collection from the database

	record = {
		"timestamp": date_string,
		"confidence-of-prediction": confidence_pred,
		"link-to-image": uploaded_img_link,
		"email": os.getenv('EMAIL_ADDRESS')
	}

	coll.insert_one(record)

if __name__ == "__main__":
	pass