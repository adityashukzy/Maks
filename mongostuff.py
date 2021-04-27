import dns
from pymongo import MongoClient
from aws_tools import aws_upload
from datetime import datetime

def make_violator_entry_in_db(
	confidence_pred,
	file_path,
	mongo_string="mongodb+srv://admin-account:admin-password@maks-cluster.noror.mongodb.net/Test-DB?retryWrites=true&w=majority"
	):
	"""
	Inserts entry into MongoDB collection of link to image of violator, confidence scores and timestamp.

	Returns: None
	"""

	## Initilizing Mongo client
	client = MongoClient()
	print(client["Maks-Cluster"]) # Debugging convenience; to be removed in production code

	## Uploading image to AWS and getting link of uploaded image
	uploaded_img_link = aws_upload.upload_image(file_path=file_path)

	## Preparing timestamp of time of violation
	now = datetime.now()
	date_string = now.strftime("%d/%m/%Y %H:%M:%S")

	## Pulling DB variables
	database = client['Test-DB'] # Picking database from our Mongo client
	table = database['Test-Collection'] # Picking table from the database

	record = {
		"timestamp": date_string,
		"confidence-of-prediction": confidence_pred,
		"link-to-image": uploaded_img_link,
	}

	table.insert_one(record)