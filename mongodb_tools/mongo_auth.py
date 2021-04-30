import dns
# import bcrypt
from pymongo import MongoClient

def verifyLogin(
	email,
	password,
	mongo_string="mongodb+srv://admin-account:admin-password@maks-cluster.noror.mongodb.net/Test-DB?retryWrites=true&w=majority"
	):
	client = MongoClient(mongo_string)

	database = client["User-Credentials"]
	coll = database["Email-Password-Credentials"]

	creds = coll.find_one({"email": email})
	hashed_pwd = creds["password"]

	# Returning if provided plain-text password is same as hashed pwd saved in db
	# return bcrypt.checkpw(password, hashed_pwd)
	return password == hashed_pwd

if __name__ == "__main__":
	if verifyLogin(email="adityashukzy@gmail.com", password="sample-pwd"):
		print("Login authenticated!")
	else:
		print("Wrong credentials!")