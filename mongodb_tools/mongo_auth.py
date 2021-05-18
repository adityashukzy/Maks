import os
import dns
import bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient

def verifyLogin(
	email,
	password
	):
	# Loading mongodb uri from the environment
	load_dotenv()
	mongo_string = os.getenv('MONGODB_AUTH_URI')
	client = MongoClient(mongo_string)

	database = client["User-Credentials"]
	coll = database["users"]

	creds = coll.find_one({"email": email})
	hashed_pwd = creds["password"]

	# Returning if provided plain-text password is same as hashed pwd saved in db
	return bcrypt.checkpw(password.encode('utf8'), hashed_pwd.encode('utf8'))

if __name__ == "__main__":
	if verifyLogin(email="adityashukzy@gmail.com", password="letsmake381dents"):
		print("Login authenticated!")
	else:
		print("Wrong credentials!")