import os
import boto3
import random
import datetime
from dotenv import load_dotenv

def upload_image(
	img_buffer,
	bucket_name="maks-images-aws-bucket",
	region_name="ap-south-1"
	):
	"""
	Uploads image at passed file-path to AWS and returns link of uploaded image on AWS cloud.

	Returns: URL of image uploaded to S3 bucket.
	"""

	## Initializing s3 resource and bucket with provided name
	load_dotenv() # loading AWS keys from .env
	s3 = boto3.resource(
		"s3",
		region_name=region_name,
		aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
		aws_secret_access_key=os.getenv('AWS_ACCESS_KEY_SECRET')
	)
	bucket = s3.Bucket(bucket_name)

	## Creating unique file name for image
	# 1. Generating a unique timestamp
	timenow = datetime.datetime.now()
	timestamp = str(timenow.year) + str(timenow.month) + str(timenow.day) + str(timenow.hour) + str(timenow.minute) + str(timenow.second)

	# 2. Putting together the unique filename
	image_file_name = f"violator-at-{timestamp}.png"

	## Uploading file at file_path to provided bucket with the name image_file_name.png
	# bucket.upload_file(
	# 	Filename=file_path,
	# 	Key=image_file_name,
	# 	ExtraArgs={'ContentType': 'image/png', 'ACL': 'public-read'})
	
	bucket.put_object(
		Key=image_file_name,
		Body=img_buffer,
		ContentType='image/png',
		ACL='public-read'
	)

	## URL of uploaded image
	url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{image_file_name}"
	print(f"URL of uploaded image: {url}")

	return url

if __name__ == "__main__":
	upload_image(bucket_name="maks-images-aws-bucket", region_name="ap-south-1")